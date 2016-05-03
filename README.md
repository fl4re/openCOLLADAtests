# openCOLLADAtests
validation tests for openCOLLADA plug


Python test frameworks enable you to validate openCOLLADA plug.
Five differents tests are available to validate the openCOLLADA plugin:
["COHERENCY_TEST", "VALIDATE_TEST", "EXPORT_IMPORT_TEST", "EXPORT_TEST", "UNIT_TEST"]


			
******************						
HOW TO USE TESTS:*
******************

1/ You need to locate your maya folder in Config.txt file 

2/ You can use one or more tests to validate your plugin
	python.exe main.py ["TEST_1", "TEST_2", ...] Arguments



--------------------------------------------------------------------------------------------------------------------
COHERENCY_TEST : python.exe main.py ["COHERENCY_TEST"] file.dae
- Coherency test is launched with the .dae provided
- result from the coherency test are written in "error_log.txt" in Result folder
--------------------------------------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------------------------------------
VALIDATE_TEST : python.exe main.py ["VALIDATE_TEST"] file.dae
- Validation test is launched with the .dae provided
- Result from the validate test are written in "validation.log" in Result folder
--------------------------------------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------------------------------------
UNIT_TEST :  python.exe main.py ["UNIT_TEST"] file.dae UnitTestDir result.xml
- you need to provide 3 arguments for unit test
	* DAE file you want the unit test to be executed on
	* UnitTestDir is the folder with all unit test you want to be executed
	* result.xml is xml file where results are written
--------------------------------------------------------------------------------------------------------------------
	
	
--------------------------------------------------------------------------------------------------------------------	
EXPORT_TEST : python.exe main.py ["EXPORT_TEST"]
- .mb file are open into Maya 
- .DAE is exported from Maya
- .DAE is validated
- All unit test inside DataSet folder are launched, 
	* results from unitTest are written in TestProcedure folder with the same hierarchy from DataSet folder
--------------------------------------------------------------------------------------------------------------------
	
	
--------------------------------------------------------------------------------------------------------------------	
IMPORT_EXPORT_TEST : python.exe main.py ["IMPORT_EXPORT_TEST"]
- .mb file are open into Maya 
- .DAE is exported from Maya
- .DAE is validated
- All unit test inside DataSet folder are launched, 
	* results from unitTest are written in TestProcedure folder with the same hierarchy from DataSet folder
- DAE is imported into Maya
- DAE is exported from Maya
- .DAE is validated
- All unit test inside DataSet folder are launched, 
	* results from unitTest are written in TestProcedure folder with the same hierarchy from DataSet folder
--------------------------------------------------------------------------------------------------------------------




*************************
HOW TO CREATE UNIT TEST:*
*************************


- You need to provide a .mb file and a unitTest python file in a specified folder into DataSet folder

1/
openCOLLADAtests
		|__ DataSet
				|__ Example_Dir
						|__ file.mb
						|__ UnitTest_Example.py

						
2/ The unitTest file must be UnitTest_**.py format

3/ Your UnitTest_*.py file need some requirement:
	- your class must be named:  Test_*						
	- your differents methods must be named:  def test_*(self):

4/ Have a look to UnitTest_camera.py to understand how to create your unitTest python file
	UnitTest will validate your plugin with DOM parser 
			
	
	