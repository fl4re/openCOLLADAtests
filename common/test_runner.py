import importlib
from opencollada import OpenCOLLADA
from opencolladatests import OpenCOLLADATests
import shutil
import unittest
from unittest_result_converter import UnitTestResult
from unittest_result_converter import UnitTestResultConverter
from util import *


#
# Launches tests for given software.
#
class TestRunner:
    def __init__(self, tool):
        self.tool = tool

    # Public methods #

    # Runs export test.
    #
    # This recursively parses test folder for any source files and unit test files.
    # Each source file is loaded into corresponding software and exported to DAE.
    # DAE is validated with DAEValidator tool and potential unit tests are executed.
    def run_export_test(self):
        res_path = self._test_results_path()

        if os.path.exists(res_path):
            shutil.rmtree(res_path)

        if not os.path.exists(res_path):
            os.makedirs(res_path)

        res = 0
        inputs = self._list_inputs(self.tool.tests_path())
        for input in inputs:
            res |= self._run_export_test_on_input(input)
        return res

    # Private methods #

    # List source files with extensions supported by current tool in 'root' directory, recursively or not.
    def _list_inputs(self, root):
        return list_files(root, self.tool.get_extensions(), recursive=True)

    # List unit test files in given directory.
    @staticmethod
    def _list_test_files(dir):
        # TODO ignore __init__.py files
        return list_files(dir, ['.py'], recursive=False)

    # Compute output directory from source file or unit test file.
    @staticmethod
    def _output_dir_from_input_file(input):
        dir_path = os.path.dirname(os.path.normpath(input))
        if dir_path.find(OpenCOLLADATests.path()) != 0:
            raise Exception(input + ' is not in a subdirectory of ' + OpenCOLLADATests.path())
        # +1 to consume slash/backslash
        return os.path.join(TestRunner._test_results_path(), dir_path[len(OpenCOLLADATests.path()) + 1:])

    # Compute output DAE path from source file path.
    @staticmethod
    def output_dae_from_input(input):
        return os.path.join(TestRunner._output_dir_from_input_file(input), os.path.splitext(os.path.basename(input))[0] + '.dae')

    # Compute test result xml file path from unit test file path.
    @staticmethod
    def _output_xml_from_unit_test(input):
        return os.path.join(TestRunner._output_dir_from_input_file(input), os.path.splitext(os.path.basename(input))[0] + '.xml')

    # Returns test results folder path.
    @staticmethod
    def _test_results_path():
        return os.path.join(OpenCOLLADATests.path(), 'test_results')

    # Returns module base path from python file path.
    #
    # Example:
    # Python file:
    # C:\OpenCOLLADAtests\colladamaya\tests\camera\TestCamera.py
    # Module base path:
    # colladamaya.tests.camera
    @staticmethod
    def _base_module_path(python_file):
        dir_path = os.path.dirname(os.path.normpath(python_file))
        if dir_path.find(OpenCOLLADATests.path()) != 0:
            raise Exception(python_file + ' is not in a subdirectory of ' + OpenCOLLADATests.path())
        # +1 to consume slash/backslash
        base_module_path = dir_path[len(OpenCOLLADATests.path()) + 1:]
        return base_module_path.replace(os.path.sep, '.')

    # Returns export options from source file path.
    # If input.export_options file does not exist then default export options for current tool are returned.
    def _export_options_from_input(self, input):
        export_options_file = os.path.splitext(input)[0] + '.export_options'
        if os.path.exists(export_options_file):
            s = open(export_options_file, 'r').read()
            try:
                options = eval(s)
                return options
            except SyntaxError:
                print export_options_file + ' content cannot be evaluated by Python.'
                raise
        # Default options
        return self.tool.default_export_options()

    # Runs export test on given source file.
    def _run_export_test_on_input(self, input):
        output = self.output_dae_from_input(input)
        options = self._export_options_from_input(input)
        # Make sure output dir exists.
        out_dir = os.path.split(output)[0]
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        if self.tool.export_file(input, output, options) != 0:
            print 'Export FAILED'
            return 1

        res = 0

        # Validate .dae
        res |= OpenCOLLADA.validate(output)

        # Run potential unit tests
        input_dir = os.path.dirname(input)
        test_files = self.__class__._list_test_files(input_dir)
        for test_file in test_files:
            res |= self._run_test_cases(test_file)

        return res

    # Runs unit tests found in test_file.
    def _run_test_cases(self, test_file):
        res = 0
        base_module_path = self._base_module_path(test_file)
        module_name = os.path.splitext(os.path.basename(test_file))[0]
        module = importlib.import_module('.' + module_name, base_module_path)
        # Test methods must start with 'test_' string
        suite = unittest.TestLoader().loadTestsFromModule(module)
        if suite.countTestCases() > 0:
            results = unittest.TextTestRunner(verbosity=1, resultclass=UnitTestResult).run(suite)
            if not results.wasSuccessful():
                res |= 1
            UnitTestResultConverter(results).to_junit_xml_file(module_name, self._output_xml_from_unit_test(test_file))
        return res
