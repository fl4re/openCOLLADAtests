from Core.Common.DOMParser import *


class FColladaParser:
    __root = 0

    def __init__(self, configDict):
        self.configDict = configDict
        # print("__INIT__ FColladaParser")

        self.testIO = 0

    # def __del__(self):
    # print("END FColladaParser")
    # self.testIO.Delink()

    @staticmethod
    def GetElementByID(daeElement, strId):
        return GetElementByID(daeElement, strId)

    @staticmethod
    def GetElementsByTags(daeElement, tagLst):
        return GetElementsByTags(daeElement, tagLst)

    @staticmethod
    def GetRoot():
        return FColladaParser.__root

    def ParseDOM(self, input_filename):

        # print("INIT FColladaParser")
        self._files_lst = [input_filename, input_filename]

        self.inputFile = self._files_lst[0]
        self.outputFiles = [self._files_lst[1]]

        self.testIO = DOMParserIO(self.inputFile, self.outputFiles)

        try:
            self.testIO.Init()
        except Exception, info:
            print 'Exception is thrown at line %d in DOMParserTest.py' % sys.exc_traceback.tb_lineno
            print ''
            print info
            return 0

        print '%s DOM parsed' % self.inputFile

        FColladaParser.__root = self.testIO.GetRoot(self.inputFile)
