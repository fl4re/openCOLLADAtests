import subprocess
import os
from FCommon import *


class FExporter:
    def __init__(self, config):

        self.config = config
        self.scriptExportPath = os.path.join(self.config["opencolladatests_path"],
                                             'Core' + os.path.sep + 'FExportCmd.py')

    # input_filename = Maya filename .ma
    # output_filename = DAE filename
    def DoExport(self, input_filename, output_filename, option):

        print("--DO EXPORT")
        print '%s = output_filename' % (output_filename + '.' + DAE_EXT)

        export = subprocess.Popen(
            self.config["mayapy_path"] + ' ' + self.scriptExportPath + ' ' + '"' + self.config[
                "colladamaya_path"] + '"' + ' ' + input_filename + ' ' + output_filename + '.dae' + ' ' + option + ' ',
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = export.communicate()
        exitcode = export.returncode
        if str(exitcode) != '0':
            print(err)
            print 'error exporting: %s' % input_filename
        else:
            print '%s exported' % input_filename

        return exitcode
