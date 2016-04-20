import os
import sys
import subprocess

import site
site.addsitedir(sys.path[0] + os.sep + 'Core')

from FColladaTest import *


class FTest_ImgComparator (FColladaTest):

	def __init__(self, input_filename):
	
		# print("INIT FTest_ImgComparator")
		FColladaTest.__init__(self, input_filename)

	def DoProcess(self, input_filename, input_filename2):

		# print("--DO PROCESS FTest_ImgComparator")	
		FColladaTest.DoProcess(self)
		
		if not os.path.exists(self.configDict["directory"] + RESULT_DIR):
			os.makedirs(self.configDict["directory"] + RESULT_DIR)

		return self.imageComparator.CompareImages(input_filename, input_filename2)
