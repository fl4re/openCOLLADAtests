import os

from Core.FCommon import *
from Core.FColladaTest import FColladaTest


class FTest_Validate(FColladaTest):
    def __init__(self, input_filename):
        # print("INIT FTest_Validate")
        FColladaTest.__init__(self, input_filename)

    def DoProcess(self):
        # print("--DO PROCESS FTest_Validate")
        error = FColladaTest.DoProcess(self)

        if not os.path.exists(self.config["opencolladatests_path"] + RESULT_DIR):
            os.makedirs(self.config["opencolladatests_path"] + RESULT_DIR)

        # validate
        logFile = self.config["opencolladatests_path"] + RESULT_DIR + 'validation' + '.log'
        error |= self.DoValidate(self.input_filename, logFile)
        return error
