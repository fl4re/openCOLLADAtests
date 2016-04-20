## TEST	##	


import os
import sys
import site
site.addsitedir(sys.path[0] + os.sep + 'Script')

### Main TEST
from FTest_Exporter import *	
myTest = FTest_Exporter(input_filename)
myTest.DoProcess()


###Coherency Test
# from FTest_Coherency import *
# myTest = FTest_Coherency(input_filename)
# myTest.DoProcess()
	
###Validation test
# from FTest_Validate import *	
# myTest = FTest_Validate(input_filename)
# myTest.DoProcess()

### Unit Test with pyTest
# input_filename = sys.argv[1]
# UnitTestFile = sys.argv[2]
# xmlResult = sys.argv[3]
# from FTest_UnitTest import *	
# myTest = FTest_UnitTest(input_filename)
# myTest.DoUnitTest(UnitTestFile, xmlResult)

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




