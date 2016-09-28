import subprocess
import os
from FCommon import *


class FImporter:
    def __init__(self, config):

        self.config = config
        self.scriptImportPath = os.path.join(self.config["opencolladatests_path"],
                                             'Core' + os.path.sep + 'FImportCmd.py')
        self.logFilename = os.path.join(self.config["opencolladatests_path"],
                                        RESULT_DIR + os.path.sep + 'mylogImport.txt')

    def DoImport(self, input_filename, output_maya_file):

        print("--DO IMPORT")
        print '%s = output_maya_file' % output_maya_file

        self.logFilename = None
        if self.logFilename is None:
            log = None
        else:
            log = open(self.logFilename, "a")

        importP = subprocess.Popen(
            self.config["mayapy_path"] + ' ' + self.scriptImportPath + ' ' + '"' + self.config[
                "colladamaya_path"] + '"' + ' ' + input_filename + ' ' + output_maya_file + ' ', stdout=log,
            stderr=subprocess.PIPE)
        out, err = importP.communicate()
        exitcode = importP.returncode

        if str(exitcode) != '0':
            print(err)
            print 'error importing: %s' % input_filename
        else:
            print '%s imported' % input_filename

        return exitcode
