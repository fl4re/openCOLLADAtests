import pytest


class FUnitTest:
    def __init__(self, configDict):
        # print("INIT UnitTest")
        self.configDict = configDict

    def DoUnitTest(self, unitTestDir, xmlResultFile):
        print("--DO UNIT_TEST")

        print '%s = unitTestDir' % unitTestDir
        print '%s = xmlResultFile' % xmlResultFile

        return pytest.main(unitTestDir + ' ' + "-s --junitxml=" + xmlResultFile)

    # invoque py.test with -v(verbose) option and --junitxml=titi2.xml(creating JUnitXML files)
    # pytest.main("test_sample.py -v --junitxml=titi2.xml")
