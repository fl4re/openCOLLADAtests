import subprocess
from FCommon import *

class FValidator:


	def __init__(self, configDict):
			
		self.configDict = configDict
		self.logFilename = self.configDict["directory"] + RESULT_DIR + '/mylogValidator.txt'

		#Validator
		self.validatorExe = self.configDict["directory"] + self.configDict["schemaValidatePath"]
		self.xsdFile = self.configDict["directory"] + SCHEMA_LOCATION
		self.xdsNamespace = SCHEMA_NAMESPACE
			
			
	#output_filename = name of the DAE exported that will be validated
	def DoValidate(self, output_filename, logName): 

		print('--DO VALIDATE')
		
		self.logFilename = None
		if (self.logFilename == None):
			log = None
		else:
			log = open(logFilename, "a")
		
		
		validator = self.validatorExe + ' {} {} {} {}'
		
		cmd = validator.format(output_filename, self.xsdFile, self.xdsNamespace, logName)
		validate = subprocess.Popen(cmd, stdout = log, stderr = subprocess.STDOUT)
	
		out,err = validate.communicate()
		exitcode = validate.returncode
		
		if str(exitcode) != '0':
			print(err)
			print 'error validating: %s' % (output_filename)
		else:
			print '%s validated' % (output_filename)