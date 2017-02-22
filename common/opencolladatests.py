import os


#
# Use this class to access openCOLLADAtests related stuff.
#
class OpenCOLLADATests:
    opencolladatests_path = None

    # Returns path to openCOLLADAtests root directory.
    @staticmethod
    def path():
        if OpenCOLLADATests.opencolladatests_path is None:
            OpenCOLLADATests.opencolladatests_path = os.path.normpath(os.path.join(os.path.dirname(os.path.realpath(
                __file__)), '..'))
        return OpenCOLLADATests.opencolladatests_path