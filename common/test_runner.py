from util import *
from opencolladatests import OpenCOLLADATests
import importlib
import inspect
import unittest


class TestRunner:
    def __init__(self, tool):
        self.tool = tool

    def list_inputs(self, root):
        return list_files(root, self.tool.get_extensions(), recursive=True)

    @staticmethod
    def list_test_cases(dir):
        return list_files(dir, ['.py'], recursive=False)

    def output_from_input(self, input):
        return os.path.join(self.test_results_path(), os.path.splitext(os.path.basename(input))[0] + '.dae')

    def test_results_path(self):
        return os.path.join(os.path.join(OpenCOLLADATests.path(), 'test_results'), self.tool.name())

    @staticmethod
    def export_options_from_input(input):
        # TODO
        return 'bakeTransforms=1;exportLights=0'

    def test_export(self):
        res_path = self.test_results_path()
        if not os.path.exists(res_path):
            os.makedirs(res_path)

        res = 0
        inputs = self.list_inputs(self.tool.data_set_path())
        for input in inputs:
            res |= self.test_export_input(input)
        return res

    def test_export_input(self, input):
        output = self.output_from_input(input)
        options = self.__class__.export_options_from_input(input)
        if self.tool.export_file(input, output, options) != 0:
            return 1
        input_dir = os.path.dirname(input)
        test_cases = self.__class__.list_test_cases(input_dir)
        res = 0
        for test_case in test_cases:
            res |= self.test_test_cases(os.path.splitext(os.path.basename(test_case))[0])
        return res

    def test_test_cases(self, test_case):
        res = 0
        # TODO proper path
        module = importlib.import_module('.' + test_case, 'colladamaya.data_set.camera')
        for c in module.__dict__.values():
            if inspect.isclass(c) and issubclass(c, unittest.TestCase) and c.__name__ != unittest.TestCase.__name__:
                suite = unittest.TestLoader().loadTestsFromTestCase(c)
                results = unittest.TextTestRunner(verbosity=1).run(suite)
                if not results.wasSuccessful():
                    res |= 1
        return res
