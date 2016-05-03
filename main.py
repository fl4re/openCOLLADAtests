## TEST	##	


import os
import sys
import site
site.addsitedir(sys.path[0] + os.sep + 'Script')

site.addsitedir(sys.path[0] + os.sep + 'Core')
from FCommon import *


if len(sys.argv) < 2:
	print 'Please use at least one of those test : ["COHERENCY_TEST", "VALIDATE_TEST", "EXPORT_IMPORT_TEST", "EXPORT_ONLY_TEST", "UNIT_TEST"]'
else:
	OPERATION_ARG = sys.argv[1]

	OP = []
	for op in OPERATIONS:
		result = OPERATION_ARG.find(op)
		if result != -1:
			OP.append(op)

	for op in OP:

		###Coherency Test
		if op == "COHERENCY_TEST":
		
			if len(sys.argv) < 3:
				print "COHERENCY_TEST need to have a .dae specified"
			else:
				input_filename = sys.argv[2]
				
				from FTest_Coherency import *
				myTest = FTest_Coherency(input_filename)
				myTest.DoProcess()
			
		###Validation test
		if op == "VALIDATE_TEST":
		
			if len(sys.argv) < 3:
				print "VALIDATE_TEST need to have a .dae specified"
			else:
				input_filename = sys.argv[2]
			
				from FTest_Validate import *	
				myTest = FTest_Validate(input_filename)
				myTest.DoProcess()

		###EXPORT_IMPORT test
		if op == "EXPORT_IMPORT_TEST":
			from FTest_Exporter_Import import *	
			myTest = FTest_Exporter_Import("")
			myTest.DoProcess()
		
		###EXPORT test
		if op == "EXPORT_ONLY_TEST":
			from FTest_Exporter import *	
			myTest = FTest_Exporter("")
			myTest.DoProcess()
		
		### Unit Test with pyTest	
		if op == "UNIT_TEST":
		
			if len(sys.argv) < 5:
				print "UNIT_TEST need to have a .dae specified, unitTestDir and xml result file"
			else:
				input_filename = sys.argv[2]
				unitTestDir = sys.argv[3]
				xmlResultFile = sys.argv[4]

				from FColladaTest import *	
				myTest = FColladaTest(input_filename)
				myTest.DoUnitTest(input_filename, unitTestDir, xmlResultFile)

	###Image Comparaison Test
	# from FTest_ImgComparator import *
	# input_filename2 = sys.argv[2]
	# myTest = FTest_ImgComparator(input_filename)
	# result = myTest.DoProcess(input_filename, input_filename2)
	# if result == True:
		# print ('OK')
	# else:
		# print ('BAD')

	###Import/Render/Export/Validation test
	# from FTest import *	
	# myTest = FTest(input_filename)
	# myTest.DoProcess()




