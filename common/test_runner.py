import importlib
import inspect
from opencollada import OpenCOLLADA
from opencolladatests import OpenCOLLADATests
import unittest
from unittest_result_converter import UnitTestResult
from unittest_result_converter import UnitTestResultConverter
from util import *


#
# Launch tests for given software.
#
class TestRunner:
    def __init__(self, tool):
        self.tool = tool

    # Public methods
    def run_export_test(self):
        res_path = self._test_results_path()
        if not os.path.exists(res_path):
            os.makedirs(res_path)

        res = 0
        inputs = self._list_inputs(self.tool.tests_path())
        for input in inputs:
            res |= self._run_export_test_on_input(input)
        return res

    # Private methods
    def _list_inputs(self, root):
        return list_files(root, self.tool.get_extensions(), recursive=True)

    @staticmethod
    def _list_test_files(dir):
        # TODO ignore __init__.py files
        return list_files(dir, ['.py'], recursive=False)

    @staticmethod
    def _output_dir_from_input_file(input):
        dir_path = os.path.dirname(os.path.normpath(input))
        if dir_path.find(OpenCOLLADATests.path()) != 0:
            raise AssertionError(input + ' is not in a subdirectory of ' + OpenCOLLADATests.path())
        # +1 to consume slash/backslash
        return os.path.join(TestRunner._test_results_path(), dir_path[len(OpenCOLLADATests.path()) + 1:])

    @staticmethod
    def _output_dae_from_input(input):
        return os.path.join(TestRunner._output_dir_from_input_file(input), os.path.splitext(os.path.basename(input))[0] + '.dae')

    @staticmethod
    def _output_xml_from_unit_test(input, class_name):
        return os.path.join(TestRunner._output_dir_from_input_file(input), os.path.splitext(os.path.basename(input))[0] + '.' + class_name + '.xml')

    @staticmethod
    def _test_results_path():
        return os.path.join(OpenCOLLADATests.path(), 'test_results')

    @staticmethod
    def _base_module_path(python_file):
        dir_path = os.path.dirname(os.path.normpath(python_file))
        if dir_path.find(OpenCOLLADATests.path()) != 0:
            raise AssertionError(python_file + ' is not in a subdirectory of ' + OpenCOLLADATests.path())
        # +1 to consume slash/backslash
        base_module_path = dir_path[len(OpenCOLLADATests.path()) + 1:]
        return base_module_path.replace(os.path.sep, '.')

    def _export_options_from_input(self, input):
        export_options_file = os.path.splitext(input)[0] + '.export_options'
        if os.path.exists(export_options_file):
            s = open(export_options_file, 'r').read()
            try:
                options = eval(s)
                return options
            except SyntaxError:
                print export_options_file + ' content cannot be evaluated by Python.'
                pass
        # Default options
        return self.tool.default_export_options()

    def _run_export_test_on_input(self, input):
        output = self._output_dae_from_input(input)
        options = self._export_options_from_input(input)
        # Make sure output dir exists.
        out_dir = os.path.split(output)[0]
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        if self.tool.export_file(input, output, options) != 0:
            return 1
        input_dir = os.path.dirname(input)
        test_files = self.__class__._list_test_files(input_dir)
        res = 0
        res |= OpenCOLLADA.validate(output)
        for test_file in test_files:
            res |= self._run_test_cases(test_file)
        return res

    def _run_test_cases(self, test_file):
        res = 0
        base_module_path = self._base_module_path(test_file)
        module_name = os.path.splitext(os.path.basename(test_file))[0]
        module = importlib.import_module('.' + module_name, base_module_path)
        for c in module.__dict__.values():
            if inspect.isclass(c) and issubclass(c, unittest.TestCase) and c.__name__ != unittest.TestCase.__name__:
                suite = unittest.TestLoader().loadTestsFromTestCase(c)
                results = unittest.TextTestRunner(verbosity=1, resultclass=UnitTestResult).run(suite)
                if not results.wasSuccessful():
                    res |= 1
                UnitTestResultConverter(results).to_junit_xml_file(
                    module_name + '.' + c.__name__, self._output_xml_from_unit_test(test_file, c.__name__))
        return res
