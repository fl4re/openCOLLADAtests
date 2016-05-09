import os

from Core.FCommon import *
from Core.FColladaTest import FColladaTest


class FTest_Validate(FColladaTest):
    def __init__(self, input_filename):
        # print("INIT FTest_Validate")
        FColladaTest.__init__(self, input_filename)

    def DoProcess(self):
        # print("--DO PROCESS FTest_Validate")
        FColladaTest.DoProcess(self)

        if not os.path.exists(self.configDict["directory"] + RESULT_DIR):
            os.makedirs(self.configDict["directory"] + RESULT_DIR)

        # validate
        logFile = self.configDict["directory"] + RESULT_DIR + 'validation' + '.log'
        self.DoValidate(self.input_filename, logFile)
