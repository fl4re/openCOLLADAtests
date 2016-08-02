# Unit Test with pyTest

from Core.FColladaTest import FColladaTest


class FTest_UnitTest(FColladaTest):
    def __init__(self, input_filename):
        # print("INIT FTest_UnitTest")
        FColladaTest.__init__(self, input_filename)

    def DoUnitTest(self, unitTestDir, xmlResultFile):
        # print("--DO PROCESS FTest_UnitTest")
        error = FColladaTest.DoProcess(self)
        error |= FColladaTest.DoUnitTest(self, self.input_filename, unitTestDir, xmlResultFile)
        return error
