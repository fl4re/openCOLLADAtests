import subprocess
import os
from FCommon import *


class FValidator:
    def __init__(self, config):

        self.config = config
        self.logFilename = os.path.join(self.config["opencolladatests_path"],
                                        RESULT_DIR + os.path.sep + 'mylogValidator.txt')

        # Validator
        self.validatorExe = self.config["validator_path"]

    # output_filename = name of the DAE exported that will be validated
    def DoValidate(self, output_filename, logName):

        print('--DO VALIDATE')

        self.logFilename = None
        if self.logFilename is None:
            log = None
        else:
            log = open(self.logFilename, "a")

        cmd = self.validatorExe + ' ' + output_filename
        validate = subprocess.Popen(cmd, stdout=log, stderr=subprocess.STDOUT)

        out, err = validate.communicate()
        exitcode = validate.returncode

        if str(exitcode) != '0':
            print(err)
            print 'error validating: %s' % output_filename
        else:
            print '%s validated' % output_filename

        return exitcode