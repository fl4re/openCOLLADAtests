from opencolladatests import OpenCOLLADATests
from util import *


class OpenCOLLADA:
    opencolla_path = None
    validator_path = None

    @staticmethod
    def path():
        if OpenCOLLADA.opencolla_path is None:
            OpenCOLLADA.opencolla_path = os.environ.get('OPENCOLLADA_PATH')
            if OpenCOLLADA.opencolla_path is None:
                OpenCOLLADA.opencolla_path = os.path.normpath(os.path.join(OpenCOLLADATests.path(), '..' + os.path.sep + 'OpenCOLLADA'))
        return OpenCOLLADA.opencolla_path

    @staticmethod
    def validate(self, dae):
        if OpenCOLLADA.validator_path is None:
            validator_exe_name = 'DAEValidator'
            if get_platform() == 'windows':
                validator_exe_name += '.exe'
            OpenCOLLADA.validator_path = find_file(OpenCOLLADA.path(), validator_exe_name, "Release")
        return OpenCOLLADA.validator_path
