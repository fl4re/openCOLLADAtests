import subprocess
from FCommon import *


class FRenderer:
    def __init__(self, configDict):

        self.configDict = configDict
        self.outputDir = self.configDict["directory"] + RESULT_DIR
        self.imageName = 'img'
        self.logFilename = self.configDict["directory"] + RESULT_DIR + '/mylogRenderer.txt'

    # input_filename = name of the maya file saved the imported DAE
    def DoRender(self, input_filename):

        print('DO RENDER')

        if self.logFilename is None:
            log = None
        else:
            log = open(self.logFilename, "a")

        cmd = ' -cam "|testCamera" -r ctfHw -x 512 -y 512 -ard 1.0 -s 1 -e 1 -b 1 -of png'
        export = subprocess.Popen(
            self.configDict["renderExe"] + ' ' + '-rd' + ' ' + self.outputDir + ' ' + cmd + ' ' +
            '-im' + ' ' + self.imageName + ' ' + input_filename, stdout=log, stderr=subprocess.STDOUT)
        # export = subprocess.Popen('C:\\Program Files\\Autodesk\\Maya2015\\bin\\Render -rd "F:\Dev\COLLADA-CTS\_Test"
        #  -cam "|testCamera" -r ctfHw -x 512 -y 512 -ard 1.0 -s 1 -e 1 -b 1 -of png  -im "foot"
        # "F:\Dev\COLLADA-CTS\_Test\Cube.mb"', stdout = log, stderr = subprocess.STDOUT)

        out, err = export.communicate()
        exitcode = export.returncode
        if str(exitcode) != '0':
            print(err)
            print 'error rendering: %s' % input_filename
        else:
            print '%s rendered' % input_filename
