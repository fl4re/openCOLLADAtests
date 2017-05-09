from opencolladatests import OpenCOLLADATests
from util import *


#
# Use this class to access OpenCOLLADA related stuff.
#
class OpenCOLLADA:
    opencollada_path = None
    validator_path = None

    # Returns path to OpenCOLLADA root directory.
    @staticmethod
    def path():
        if OpenCOLLADA.opencollada_path is None:
            OpenCOLLADA.opencollada_path = os.environ.get('OPENCOLLADA_PATH')
            if OpenCOLLADA.opencollada_path is None:
                OpenCOLLADA.opencollada_path = os.path.normpath(os.path.join(OpenCOLLADATests.path(), '..' + os.path.sep + 'OpenCOLLADA'))
        return OpenCOLLADA.opencollada_path

    # Runs DAEValidator tool against given DAE file.
    @staticmethod
    def validate(dae):
        if OpenCOLLADA.validator_path is None:
            validator_exe_name = 'DAEValidator'
            if get_platform() == 'windows':
                validator_exe_name += '.exe'
            OpenCOLLADA.validator_path = find_file(OpenCOLLADA.path(), validator_exe_name, "Release")
            if OpenCOLLADA.validator_path is None:
                raise Exception('Cannot find ' + validator_exe_name + ' (Release)')
        return run(
            '"' + OpenCOLLADA.validator_path + '"' +
            ' "' + dae + '"')
