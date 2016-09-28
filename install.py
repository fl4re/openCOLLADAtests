import os
import sys

from subprocess import call
from Core.Common.Util import *

import platform

# MacOSX:
# sudo -H python install.py

def main(argv):
    # install PIP
    if call(["python", "Install/get-pip.py"]):
        sys.exit(0)

    # set PATH with PIP
    os.environ["PATH"] += os.pathsep + sys.executable[0:sys.executable.rfind("\\")] + "\Scripts"

    # install Pytest package
    if call(["pip", "install", "-U", "pytest"]):
        sys.exit(0)

    # install Numpy package https://pypi.python.org/pypi/numpy
    if get_platform() == 'macosx':
        package = "numpy-1.11.2rc1-cp27-cp27m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl"
    elif platform.architecture()[0] == "64bit":
        package = "numpy-1.11.0-cp27-none-win_amd64.whl"
    else:
        package = "numpy-1.11.0-cp27-none-win32.whl"

    if call(["pip", "install", "Install/" + package]):
        sys.exit(0)

    sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])
