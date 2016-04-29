import sys
import os

import site
site.addsitedir(sys.path[0] + os.sep + 'Core')
site.addsitedir(sys.path[0] + os.sep + 'Core/Common')

from FExporter import *
from FRenderer import *
from FCommon import *
from FImporter import *
from FValidator import *
from FCoherencyTest import *
from FImageComparator import *
from FUnitTest import *
from FColladaParser import *


from DOMParser import *
from CheckingModule import *
from NodeInsCheck import *


class FColladaTest:

	def __init__(self, input_filename):

		# print("INIT FColladaTest")	
		
		# Read in and parse the configuration file.
		configDict1 = {}
		
		myPath = os.path.dirname(os.path.abspath(__file__))
		configDict1["directory"] = myPath + "/../"

		# myPath = os.getcwd()
		# myPath = myPath.replace("\\", "/")
		# print myPath
		# configDict1["directory"] = os.getcwd() 
		
		if (os.path.isfile(CONFIGURATION_FILE)):
			f = open(CONFIGURATION_FILE)
			line = f.readline()
			while (line):
				while (line.count("\t\t") > 0):
					line = line.replace("\t\t", "\t")
				key, value = line.split("\t",1)
				if (configDict1.has_key(key)):
					print ("Warning: Ignoring redefinition of configuration " +
						   "key: " + key + ".")
					continue
				
				# print("key" + key + ";value  " + value.strip())	
				configDict1[key] = value.strip() # remove \n
				line = f.readline()
			f.close
		
		
		
		self.configDict = configDict1
		
		#name of the maya saved from the imported DAE 
		self.ouput_maya_file = self.configDict["directory"] + RESULT_DIR + MAYA_FILE_MA

		
		#name of the DAE to be imported
		self.input_filename = input_filename
		
		
		self.importer = FImporter(self.configDict)
		self.exporter = FExporter(self.configDict)
		self.renderer = FRenderer(self.configDict)
		self.validator = FValidator(self.configDict)
		self.coherencyTest = FCoherencyTest(self.configDict)
		self.imageComparator = FImageComparator(self.configDict)
		self.unitTest = FUnitTest(self.configDict)
		self.colladaParser = FColladaParser(self.configDict)


#######################################################################################		
	@staticmethod
	def GetRoot():
		return FColladaParser.GetRoot()
		
	@staticmethod
	def GetElementByID(daeElement, strId):
		return FColladaParser.GetElementByID(daeElement, strId)
	
	@staticmethod
	def GetElementsByTags(daeElement, tagLst):
		return FColladaParser.GetElementsByTags(daeElement, tagLst)
#######################################################################################

	
	
	def DoCoherencyTest(self, inputfile, logFile):
		self.coherencyTest.DoCoherencyTest(inputfile, logFile)
	
	def DoRender(self, input_filename):
		self.renderer.DoRender(input_filename)
	
	def DoImport(self, input_filename, output_maya_file):
		self.importer.DoImport(input_filename, output_maya_file)
	
	def DoExport(self, Maya_filename, DAE_filename, option):
		self.exporter.DoExport(Maya_filename, DAE_filename, option)
	
	
	# UnitTest
	def DoUnitTest(self, DAE_filename, unitTestDir, xmlResultFile):
		self.colladaParser.ParseDOM(DAE_filename)
		self.unitTest.DoUnitTest(unitTestDir, xmlResultFile)
		
	def DoValidate(self, output_filename, logName):
		self.validator.DoValidate(output_filename, logName)	
	
	
	def DoProcess(self):

		print("--DO PROCESS FColladaTest")
		if not os.path.exists(self.configDict["directory"] + RESULT_DIR):
			os.makedirs(self.configDict["directory"] + RESULT_DIR)