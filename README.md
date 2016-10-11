# openCOLLADAtests
Validation tests for openCOLLADA plugin.

Python test framework which allows you to validate openCOLLADA Maya plugin. Five differents tests are available to validate the openCOLLADA plugin:

- Validation
- Coherency
- Export/Import
- Export only
- Unit tests

# Installation:

This test framework requires "pytest" and "numpy" to be installed. You can either install Anaconda 2 (https://www.continuum.io/downloads) which already include those packages or install them manually.

Manual installation steps if not using Anaconda:

  1. Launch get-pip.py in /Core folder
  2. add pip to your PATH (PATH = C:\Python27\Scripts)
  3. execute in dos: pip install -U pytest   (this will install pytest unitTest framework)
  4. Download numpy-1.11.0-cp27-none-win32.whl or numpy-1.11.0-cp27-none-win_amd64.whl from https://pypi.python.org/pypi/numpy
  5. Copy this file into C:\Python27\Scripts
  6. execute dos command: pip install numpy-1.11.0-cp27-none-win32.whl

# How to launch tests:

  1. First you need to locate your maya folder in Config.txt file
  2. You can then launch tests by executing launch.bat

If needed you can run tests individually:

### Coherency test

python main.py --coherency-test file.dae

Coherency test is launched against provided .dae. Result from the coherency test are written in "error_log.txt" in Result folder.

### Validation test

python main.py --validation-test file.dae

Validation test is launched against provided .dae. Result from the validation test are written in "validation.log" in Result folder.

### Unit tests

python main.py --unit-test file.dae path_to_unit_test_dir result.xml

You need to provide 3 arguments for unit testing:
	- DAE file you want the unit test to be executed on
	- path_to_unit_test_dir is the folder with all unit test you want to be executed
	- result.xml is an xml file where results are written (JUnit format)
	
### Export only test

python.exe main.py --export-test
 - .mb file are opened into Maya 
 - .DAE is exported from Maya
 - .DAE is validated
 - All unit tests inside DataSet folder are launched. Results from unitTest are written in TestProcedure folder with the same hierarchy from DataSet folder.

### Export/Import test
	
python.exe main.py --export-import-test
 - .mb file are opened into Maya 
 - .DAE is exported from Maya
 - .DAE is validated
 - All unit tests inside DataSet folder are launched. Results from unitTest are written in TestProcedure folder with the same hierarchy from DataSet folder.
 - .DAE is imported into Maya
 - .DAE is exported from Maya
 - .DAE is validated
 - All unit tests inside DataSet folder are launched. Results from unitTest are written in TestProcedure folder with the same hierarchy from DataSet folder

# How to create unit tests:

  0. You need to provide a .mb file and a unitTest python file in a specified folder into DataSet folder

  1. 
openCOLLADAtests
		|__ DataSet
				|__ Example_Dir
						|__ file.mb
						|__ UnitTest_Example.py

						
  2. The unitTest file must be UnitTest_**.py format

  3. Your UnitTest_*.py file need some requirement:
	- your class must be named:  Test_*						
	- your differents methods must be named:  def test_*(self):

  4. Have a look to UnitTest_camera.py to understand how to create your unitTest python file
	UnitTest will validate your plugin with DOM parser
	k
