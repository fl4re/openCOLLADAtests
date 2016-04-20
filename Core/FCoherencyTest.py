
import sys
import os
import time

from FCommon import *


class FCoherencyTest:


	def __init__(self, configDict):
				
		self.configDict = configDict
		
		# Coherency Test options
		self.coherency_options = [
						("SCHEMA", True),                # Check Schema 
						("CIRCULR_REFERENCE", True),     # Check for Circular References
						("UNIQUE_ID", True),             # Check for Unique IDs", 
						("COUNTS", True),                # Check Counts
						("FILES", True),                 # Check Files
						("FLOAT_ARRAY", True),           # Check Floats
						("LINKS", True),                 # Check Links
						("SKIN", True),                  # Check Skin Usage
						("TEXTURE", True)                # Check Texture Usage
						]



		# Should delete the old error log, or add to it?
		self.remove_old_error_log = True
		
		self.coherency_path = self.configDict["directory"] + self.configDict["coherencyPath"]


	def doublecheck(self, x, in_settings):
		
		# Change working directory to the COLLADA file's path
		os.chdir(os.path.dirname(x))
		# Run coherency test on it
		os.popen("\"" + self.coherency_path + "\""+ os.path.basename(x) +"\""+ in_settings+"\"")
		# Change back the working directory
		os.chdir(self.prev_cwd)
		
		
	def DoCoherencyTest(self, input_filename, logName): 

		# Backup the error log before executing commands
		if os.path.exists(logName):
			if self.remove_old_error_log:
				os.remove(logName)

		# Check if coherencytest exists... if not, report the problem.
		if not os.path.exists(self.coherency_path):
			print "Error: Cannot find Coherency Test at config.txt's listed path:\n"
			print self.coherency_path
			time.sleep(3)
			print "\nQuitting script..."
			time.sleep(1)
			sys.exit()

		# Extract the test settings
		settings = ""
		ignore_all = True

		for option in self.coherency_options:
			flag = option[1]
			
			if flag:
				if ignore_all:
					settings = (settings + " -check")
					ignore_all = False
				settings = (settings + " " + option[0])
				
		if ignore_all:
			settings = (settings + " -ignore")
			for option in self.coherency_options:
				settings = (settings + " " + option[0])

		print "----------------------------------------------------------"
		print "Running script with the following Coherency Test commands:"
		print "----------------------------------------------------------"
		for x in self.coherency_options:
			print x[0],"=",str(x[1])
		print "----------------------------------------------------------"

		# Prep settings before execution
		self.coherency_path = "\""+os.path.abspath(self.coherency_path)+"\" "
		settings = settings + " -log \""+os.path.abspath(logName)+"\""
		self.prev_cwd = os.getcwd()
		
		# Run coherency test
		for x in input_filename:
			self.doublecheck(x, settings) 
			
		print
		print "----------------------------------------------------------"
		print "Doublecheck script completed!"



	


