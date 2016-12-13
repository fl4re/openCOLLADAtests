from argparse import ArgumentParser

from Script.FTest_Exporter import FTest_Exporter
from Script.FTest_Exporter_Import import FTest_Exporter_Import
from Script.FTest_Coherency import FTest_Coherency
from Script.FTest_Validate import FTest_Validate
from Core.FColladaTest import FColladaTest
from Core.Common.Util import *

parser = ArgumentParser(description="OpenCOLLADATests")
parser.add_argument("--export-test", dest="doExportTest", action="store_true",
                    help="Run export tests.")
parser.add_argument("--export-import-test", dest="doExportImportTest", action="store_true",
                    help="Run export/import tests.")
parser.add_argument("--coherency-test", dest="doCoherencyTest", nargs=1,
                    help="Run coherency test on given DAE file.")
parser.add_argument("--validation-test", dest="doValidationTest", nargs=1,
                    help="Run schema validation test on given DAE file.")
parser.add_argument("--unit-test", dest="doUnitTest", nargs=3,
                    help="Run unit tests with specified DAE file, unit test directory and xml result file.")
parser.add_argument("--option", dest="doOption", nargs=1,
                    help="options.")

options = parser.parse_args()

error = 0

if options.doOption:
    option = options.doOption[0]
else:
    option = None

if options.doExportTest:
    myTest = FTest_Exporter(option, "")
    error |= myTest.DoProcess()

if options.doExportImportTest:
    myTest = FTest_Exporter_Import(option, "")
    error |= myTest.DoProcess()

if options.doCoherencyTest is not None:
    myTest = FTest_Coherency(options.doCoherencyTest[0])
    error |= myTest.DoProcess()

if options.doValidationTest is not None:
    myTest = FTest_Validate(options.doValidationTest[0])
    error |= myTest.DoProcess()

if options.doUnitTest is not None:
    myTest = FColladaTest(options.doUnitTest[0])
    error |= myTest.DoUnitTest(options.doUnitTest[0], options.doUnitTest[1], options.doUnitTest[2])

sys.exit(error)
