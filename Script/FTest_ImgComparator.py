import os

from Core.FCommon import *
from Core.FColladaTest import FColladaTest


class FTest_ImgComparator(FColladaTest):
    def __init__(self, input_filename):
        # print("INIT FTest_ImgComparator")
        FColladaTest.__init__(self, input_filename)

    def DoProcess(self, input_filename, input_filename2):
        # print("--DO PROCESS FTest_ImgComparator")
        error = FColladaTest.DoProcess(self)

        if not os.path.exists(self.config["opencolladatests_path"] + RESULT_DIR):
            os.makedirs(self.config["opencolladatests_path"] + RESULT_DIR)

        return error | self.imageComparator.CompareImages(input_filename, input_filename2) is False