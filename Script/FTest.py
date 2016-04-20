import os
import sys

import site
site.addsitedir(sys.path[0] + os.sep + 'Core')

from FColladaTest import *


class FTest (FColladaTest):

	def __init__(self, input_filename):

		# print("INIT FTest")	
	
		FColladaTest.__init__(self, input_filename)
				
		#name of the DAE exported
		self.output_filename = self.configDict["directory"] + RESULT_DIR + DAE_EXPORTED_NAME
	
	
	def DoProcess(self):

		# print("--DO PROCESS FTest")	
		FColladaTest.DoProcess(self)
		
		if not os.path.exists(self.configDict["directory"] + RESULT_DIR):
			os.makedirs(self.configDict["directory"] + RESULT_DIR)
		
		#Import
		self.DoImport(self.input_filename, self.ouput_maya_file)
			
		#Render
		self.DoRender(self.ouput_maya_file)
			
		#Export and Validate
		i = 0
		
		for option in OPTIONS:
			
			name = self.output_filename + str(i)
			self.DoExport(self.ouput_maya_file, name, option)
			
			logFile = self.configDict["directory"] + RESULT_DIR + 'validation' + str(i) + '.log'
			output_filename = self.output_filename + str(i) + '.' + DAE_EXT + ' '
			self.DoValidate(output_filename, logFile)
			i += 1