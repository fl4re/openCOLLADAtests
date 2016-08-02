import os
from Core.FColladaTest import FColladaTest
from Core.FCommon import *


class FTest_Coherency(FColladaTest):
    def __init__(self, input_filename):
        # print("INIT FTest_Coherency")
        FColladaTest.__init__(self, input_filename)

    def DoProcess(self):
        # print("--DO PROCESS FTest_Coherency")
        error = FColladaTest.DoProcess(self)

        if not os.path.exists(self.configDict["directory"] + RESULT_DIR):
            os.makedirs(self.configDict["directory"] + RESULT_DIR)

        # validate
        logFile = os.path.normcase(self.configDict["directory"] + RESULT_DIR + r"error_log.txt")

        inputfile = [self.input_filename]
        error |= self.DoCoherencyTest(inputfile, logFile)
        return error
