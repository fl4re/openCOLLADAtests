import os
import sys

import site
site.addsitedir(sys.path[0] + os.sep + 'Core')

from FCommon import *
from FColladaTest import *



#################################################################################################
#																								#
#     This will recursively search for all .ma in DATASET directory and launch TEST for THEM	#
#		Result will be created in TEST_PROCEDURE with the same hierarchy						#
#			TEST is composed of 2 Parts : IMPORT TEST and EXPORT TEST							#
#																								#
#																								#
#			EXPORT = IMPORT DAE FILE / EXPORT DAE / VALIDATE DAE/ LAUNCH SPECIFIC UNIT_TEST		#
#################################################################################################


class FTest_Exporter (FColladaTest):

	def __init__(self, input_filename):

		# print("FTest_Exporter init")	
	
		FColladaTest.__init__(self, input_filename)

		self.options = 'bakeTransforms=1;exportLights=0'
		self._mayaFilesList = []

		
	def RetrieveFiles(self, path=None,ext='.mb'):
		if not path: 
			path=os.getcwd()
			# print path
		if os.path.isdir(path): 
			lst = os.listdir(path)   
			if lst: 
				for each in lst:  
					spath=path+'/'+each  
					if os.path.isfile(spath):   
						# file type must be exactly matched
						if spath.endswith(ext):
							self._mayaFilesList.append(spath) 
					self.RetrieveFiles(spath, ext)
		# print self._mayaFilesList
	
	
	
	def DoProcess(self):

		# print("--DO PROCESS FTest_Exporter")	
		FColladaTest.DoProcess(self)
				
		if not os.path.exists(self.configDict["directory"] + RESULT_DIR):
			os.makedirs(self.configDict["directory"] + RESULT_DIR)
		
	
		## retrieve all directory with .ma in DATASET
		self.RetrieveFiles(self.configDict["directory"] + DATA_SET)
	
		index = 0
		
		for maya_file in self._mayaFilesList:
			
			
			## retrieve UnitTest according to .ma selected
			temp = self._mayaFilesList[index].replace(DATA_SET, TEST_PROCEDURE)
			self.output_filename = temp[0:temp.rfind(".")]

			directory =  temp[0:temp.rfind("/")]
			
			
			if not os.path.exists(directory):
				os.makedirs(directory)
			
			unitTestDir = self._mayaFilesList[index][0:self._mayaFilesList[index].rfind("/")+1]
			index += 1
			
			
			
			
			########################
			# CHECK EXPORT COLLADA #
			########################
			
			
			# LOAD MAYA FILE / EXPORT / VALIDATE
			self.DoExport(maya_file, self.output_filename, self.options)
			# print ('>>>>> MAYA FILE LOADED >>>>>>>>>>>>>>>>>>' + maya_file)
			# print ('>>>>> DAE FILE EXPORTED >>>>>>>>>>>>>>>>>>' + self.output_filename + '.' + DAE_EXT)
				
			logFile = directory + '/validation' + '.' + LOG_EXT
			output_filename = self.output_filename + '.' + DAE_EXT
			self.DoValidate(output_filename, logFile)

			# UNIT TEST
			self.DoUnitTest(output_filename, unitTestDir, directory + '/unitTest.' + XML_EXT)
			# print ('>>>>> FOLDER USED FOR UNIT TEST >>>>>>>>>>>>>>>>>>' + unitTestDir)
			# print ('>>>>> DAE FILE USED FOR UNIT TEST >>>>>>>>>>>>>>>>>>' + output_filename)
