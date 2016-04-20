import subprocess

from FCommon import *


class FImporter:

	def __init__(self, configDict):
		
		self.configDict = configDict
		self.scriptImportPath = self.configDict["directory"] + 'Core/FImportCmd.py'
		self.logFilename = self.configDict["directory"] + RESULT_DIR + '/mylogImport.txt'
		
		
	def DoImport(self, input_filename, output_maya_file):

		print("--DO IMPORT")	
		print '%s = output_maya_file' % (output_maya_file)
	
		self.logFilename = None
		if (self.logFilename == None):
			log = None
		else:
			log = open(logFilename, "a")
			
	
		importP = subprocess.Popen(self.configDict["mayaPath"] + ' ' + self.scriptImportPath + ' ' + self.configDict["mayaColladaPluginName"] + ' ' + input_filename + ' ' + output_maya_file + ' ', stdout = log, stderr=subprocess.PIPE)
		out,err = importP.communicate()
		exitcode = importP.returncode
		
		if str(exitcode) != '0':
			print(err)
			print 'error importing: %s' % (input_filename)
		else:
			print '%s imported' % (input_filename)