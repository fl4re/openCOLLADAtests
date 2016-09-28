import pytest
from Core.Common.Util import *

class FUnitTest:
    def __init__(self, config):
        # print("INIT UnitTest")
        self.config = config

    def DoUnitTest(self, unitTestDir, xmlResultFile):
        print("--DO UNIT_TEST")

        print '%s = unitTestDir' % unitTestDir
        print '%s = xmlResultFile' % xmlResultFile

        if get_platform() == 'windows':
            # paths with backslashes not supported by pytest
            unitTestDir = unitTestDir.replace('\\', '/')
            xmlResultFile = xmlResultFile.replace('\\', '/')

        return pytest.main('\"' + unitTestDir + '\" ' + '-s --junitxml=\"' + xmlResultFile + '\"')

    # invoque py.test with -v(verbose) option and --junitxml=titi2.xml(creating JUnitXML files)
    # pytest.main("test_sample.py -v --junitxml=titi2.xml")
