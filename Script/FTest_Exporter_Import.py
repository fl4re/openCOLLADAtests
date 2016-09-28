import os

from Core.FCommon import *
from Core.FColladaTest import FColladaTest


#################################################################################################
#																								#
#     This will recursively search for all .ma in DATASET directory and launch TEST for THEM	#
#		Result will be created in TEST_PROCEDURE with the same hierarchy						#
#			TEST is composed of 2 Parts : IMPORT TEST and EXPORT TEST							#
#																								#
#																								#
#			IMPORT = LOAD MA FILE / EXPORT DAE / VALIDATE DAE/ LAUNCH SPECIFIC UNIT_TEST		#
#			EXPORT = IMPORT DAE FILE / EXPORT DAE / VALIDATE DAE/ LAUNCH SPECIFIC UNIT_TEST		#
#################################################################################################


class FTest_Exporter_Import(FColladaTest):
    def __init__(self, input_filename):

        # print("FTest_Exporter_Import init")

        FColladaTest.__init__(self, input_filename)

        self.options = 'bakeTransforms=0;exportLights=0'
        self._mayaFilesList = []

    def RetrieveFiles(self, path=None, ext='.mb'):
        if not path:
            path = os.getcwd()
        # print path
        if os.path.isdir(path):
            lst = os.listdir(path)
            if lst:
                for each in lst:
                    spath = path + os.path.sep + each
                    if os.path.isfile(spath):
                        # file type must be exactly matched
                        if spath.endswith(ext):
                            self._mayaFilesList.append(spath)
                    self.RetrieveFiles(spath, ext)
                # print self._mayaFilesList

    def DoProcess(self):

        # print("--DO PROCESS FTest_Exporter_Import")
        error = FColladaTest.DoProcess(self)

        if not os.path.exists(os.path.join(self.config["opencolladatests_path"], RESULT_DIR)):
            os.makedirs(os.path.join(self.config["opencolladatests_path"], RESULT_DIR))

        # retrieve all directory with .ma in DATASET
        self.RetrieveFiles(os.path.join(self.config["opencolladatests_path"], DATA_SET))

        index = 0

        for maya_file in self._mayaFilesList:

            # retrieve UnitTest according to .ma selected
            temp = self._mayaFilesList[index].replace(DATA_SET, TEST_PROCEDURE)
            self.output_filename = temp[0:temp.rfind(".")]

            directory = temp[0:temp.rfind(os.path.sep)]

            if not os.path.exists(directory):
                os.makedirs(directory)

            unitTestDir = self._mayaFilesList[index][0:self._mayaFilesList[index].rfind(os.path.sep) + 1]
            index += 1

            ########################
            # CHECK EXPORT COLLADA #
            ########################

            # LOAD MAYA FILE / EXPORT / VALIDATE
            error |= self.DoExport(maya_file, self.output_filename, self.options)
            # print ('>>>>> MAYA FILE LOADED >>>>>>>>>>>>>>>>>>' + maya_file)
            # print ('>>>>> DAE FILE EXPORTED >>>>>>>>>>>>>>>>>>' + self.output_filename + '.' + DAE_EXT)

            logFile = os.path.join(directory, 'validation' + '.' + LOG_EXT)
            output_filename = self.output_filename + '.' + DAE_EXT
            error |= self.DoValidate(output_filename, logFile)

            # UNIT TEST
            error |= self.DoUnitTest(output_filename, unitTestDir, os.path.join(directory, 'unitTest.' + XML_EXT))
            # print ('>>>>> FOLDER USED FOR UNIT TEST >>>>>>>>>>>>>>>>>>' + unitTestDir)
            # print ('>>>>> DAE FILE USED FOR UNIT TEST >>>>>>>>>>>>>>>>>>' + output_filename)

            ########################
            # CHECK IMPORT COLLADA #
            ########################

            # IMPORT
            error |= self.DoImport(self.output_filename + '.' + DAE_EXT, self.ouput_maya_file)
            # print ('>>>>> DAE FILE IMPORTED >>>>>>>>>>>>>>>>>>' + self.output_filename + '.' + DAE_EXT)

            # LOAD MAYA FILE / EXPORT / VALIDATE
            i = 0

            for option in OPTIONS:
                name = self.output_filename + str(i)
                self.DoExport(self.ouput_maya_file, name, option)
                # print ('>>>>> MAYA FILE LOADED >>>>>>>>>>>>>>>>>>' + self.ouput_maya_file)
                # print ('>>>>> DAE FILE EXPORTED >>>>>>>>>>>>>>>>>>' + name)

                logFile = os.path.join(directory, 'validation' + str(i) + '.' + LOG_EXT)
                output_filename = self.output_filename + str(i) + '.' + DAE_EXT + ' '
                error |= self.DoValidate(output_filename, logFile)

                # UNIT TEST
                error |= self.DoUnitTest(output_filename, unitTestDir, os.path.join(directory, 'unitTest' + str(i) + '.' + XML_EXT))
                # print ('>>>>> FOLDER USED FOR UNIT TEST >>>>>>>>>>>>>>>>>>' + unitTestDir)
                # print ('>>>>> DAE FILE USED FOR UNIT TEST >>>>>>>>>>>>>>>>>>' + output_filename)

                i += 1

        return error
