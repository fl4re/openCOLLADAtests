from util import *
from opencolladatests import OpenCOLLADATests
import importlib
import inspect
import unittest
from unittest_result_converter import UnitTestResult
from unittest_result_converter import UnitTestResultConverter


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
        inputs = self._list_inputs(self.tool.data_set_path())
        for input in inputs:
            res |= self._run_export_test_on_input(input)
        return res

    # Private methods
    def _list_inputs(self, root):
        return list_files(root, self.tool.get_extensions(), recursive=True)

    @staticmethod
    def _list_test_cases(dir):
        return list_files(dir, ['.py'], recursive=False)

    def _output_dae_from_input(self, input):
        return os.path.join(self._test_results_path(), os.path.splitext(os.path.basename(input))[0] + '.dae')

    def _output_xml_from_unit_test(self, input):
        return os.path.join(self._test_results_path(), os.path.splitext(os.path.basename(input))[0] + '.xml')

    def _test_results_path(self):
        return os.path.join(os.path.join(OpenCOLLADATests.path(), 'test_results'), self.tool.name())

    @staticmethod
    def _export_options_from_input(input):
        # TODO
        # TODO CAD tool dependent...
        return 'bakeTransforms=1;exportLights=0'

    def _run_export_test_on_input(self, input):
        output = self._output_dae_from_input(input)
        options = self.__class__._export_options_from_input(input)
        if self.tool.export_file(input, output, options) != 0:
            return 1
        input_dir = os.path.dirname(input)
        test_cases = self.__class__._list_test_cases(input_dir)
        res = 0
        for test_case in test_cases:
            res |= self._run_test_cases(os.path.splitext(os.path.basename(test_case))[0])
        return res

    def _run_test_cases(self, test_cases):
        res = 0
        # TODO proper path
        module = importlib.import_module('.' + test_cases, 'colladamaya.data_set.camera')
        for c in module.__dict__.values():
            if inspect.isclass(c) and issubclass(c, unittest.TestCase) and c.__name__ != unittest.TestCase.__name__:
                suite = unittest.TestLoader().loadTestsFromTestCase(c)
                results = unittest.TextTestRunner(verbosity=1, resultclass=UnitTestResult).run(suite)
                if not results.wasSuccessful():
                    res |= 1
                # TODO correct output path
                UnitTestResultConverter(results).to_junit_xml_file(
                    test_cases, self._output_xml_from_unit_test(test_cases))
        return res
