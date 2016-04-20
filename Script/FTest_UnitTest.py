


# Unit Test with pyTest
import sys
import os
import site
site.addsitedir(sys.path[0] + os.sep + 'Core')
from FCommon import *

import pytest

from FColladaTest import *


class FTest_UnitTest (FColladaTest):

	def __init__(self, input_filename):

		# print("INIT FTest_UnitTest")
		FColladaTest.__init__(self, input_filename)
		
	def DoUnitTest(self, unitTestDir, xmlResultFile):

		# print("--DO PROCESS FTest_UnitTest")	
		FColladaTest.DoProcess(self)
		FColladaTest.DoUnitTest(self, self.input_filename, unitTestDir, xmlResultFile)