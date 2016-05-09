import os
import os.path


class FCompareResult:
    def __init__(self):
        self.__result = False

    def SetResult(self, result):
        self.__result = result

    def GetResult(self):
        return self.__result


class FImageComparator:
    def __init__(self, configDict):
        self.configDict = configDict

    def CompareImages(self, input_filename, input_filename2):

        print("--DO CompareImages")

        compareResult = FCompareResult()
        compareResult.SetResult(False)

        filename1 = os.path.normpath(os.path.abspath(input_filename))
        filename2 = os.path.normpath(os.path.abspath(input_filename2))

        if os.path.isfile(filename1):
            if os.path.isfile(filename2):
                # return compareResult
                # else:
                # if (os.path.isfile(filename2)):
                # return compareResult

                # compareResult.SetResult(True)
                # return compareResult

                f1 = open(filename1, "rb")
                f2 = open(filename2, "rb")

                block1 = f1.read(10240)  # 10 KB
                block2 = f2.read(10240)  # 10 KB

                while block1 == block2:
                    if (len(block1) == 0) and (len(block2) == 0):
                        f1.close()
                        f2.close()
                        compareResult.SetResult(True)
                        return compareResult.GetResult()

                    block1 = f1.read(10240)  # 10 KB
                    block2 = f2.read(10240)  # 10 KB

                f1.close()
                f2.close()

        # print ('val1=' + str(compareResult.GetResult()))
        return compareResult.GetResult()
