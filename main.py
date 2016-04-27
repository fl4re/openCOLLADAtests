## TEST	##	


import os
import sys
import site
site.addsitedir(sys.path[0] + os.sep + 'Script')

site.addsitedir(sys.path[0] + os.sep + 'Core')
from FCommon import *


for op in OPERATIONS:

	###Coherency Test
	if op == "COHERENCY_TEST":
		from FTest_Coherency import *
		myTest = FTest_Coherency(input_filename)
		myTest.DoProcess()
		
	###Validation test
	if op == "VALIDATE_TEST":
		from FTest_Validate import *	
		myTest = FTest_Validate(input_filename)
		myTest.DoProcess()

	### Main TEST
	if op == "IMPORT_EXPORT_TEST":
		from FTest_Exporter import *	
		myTest = FTest_Exporter(input_filename)
		myTest.DoProcess()

	### Unit Test with pyTest	
	if op == "UNIT_TEST":
		input_filename = sys.argv[1]
		unitTestDir = sys.argv[2]
		xmlResultFile = sys.argv[3]

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




