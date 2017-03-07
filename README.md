# openCOLLADAtests
Validation tests for OpenCOLLADA plugins.

Python test framework which allows you to validate OpenCOLLADA plugins for Maya, 3DSMax, MotionBuilder...

# Requirements

Python 2.7
Applications to test (Maya, 3DSMax...)
COLLADA plugin built in Release
DAEValidator built in Release

# Setup

By default, test framework supposes OpenCOLLADA and openCOLLADAtests projects are located in the same directory and that applications (Maya, 3DSMax...) are installed to their default location (usually in C:\Program Files\Autodesk on Windows).

If default paths are not used you can tell where things are located by setting environment variables:

*OPENCOLLADA_PATH* path to OpenCOLLADA project folder
*MAYA_PATHVVVV_X64* path to Maya installation where VVVV is Maya version (2015, 2017...)
*ADSK_3DSMAX_x64_VVVV* path 3DSMax installation where VVVV is 3DSMax version (2017...)

COLLADA plugins must be built in Release prior to running tests. They are automatically installed before running tests. You don't have to install them manually.

DAEValidator tool must be built in Release prior to running tests.

# Running tests

To run tests, go to openCOLLADAtests folder and run the following command:

python launch.py

Options:

*--tool t* Specifies tool to test (Maya, 3DSMax...). Default is Maya.
*--version v* Specifies tool version (Example for Maya: 2015, 2017...). Default is 2015.

# Tests proceedings

Note: currently only exporters are tested.

Test framework first recursively lists all source files in specific folder. A source file has native format of tested application (.ma or .mb files for Maya, .max for 3DSMax)
Each source file is loaded in tested application and exported using OpenCOLLADA plugin.
Each export result file (.dae) is validated with DAEValidator which does schema validation and several coherency tests. See DAEValidator for more details.
Then, if present, unit tests are run.
Unit test results can be found in openCOLLADAtests/test_results subfolders as .xml files using JUnit format.

# Adding unit tests

## Basic steps

- Create a python file in same folder as source file. There is no naming convention.
- Edit python file and add the following code:

```python
import common.test_case_base


class CameraTestSuite(common.test_case_base.TestCaseBase):
    def setUp(self):
        super(self.__class__, self).setUp()
        self.load_dae(__file__, source_file_path)

    def test_testname1(self):
    	...

    def test_testname2(self):
    	...
```

All test suites inherit common.test_case_base.TestCaseBase.
setUp method is reponsible to load exported .dae using helper method load_dae().
Unit test method name must start with 'test_'.

## Export options

Export can be customized and parameterized for each source file by providing an additional file with named 'source_file_name.export_options'.
Content is a map of key/value that can be evaluated by python and is application dependent.

Supported keys and default values:

Maya:
*'export_options': 'bakeTransforms=1;exportLights=0'*
Export options passed to COLLADAMaya exporter.

*'mayapy': True*
If True, use mayapy executable to load and export file. If False, use maya executable (with GUI) to load and export file.
