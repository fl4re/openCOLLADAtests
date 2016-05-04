import os
import sys
import site

from subprocess import call

import platform


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
	if platform.architecture()[0] == "64bit":
		package = "numpy-1.11.0-cp27-none-win_amd64.whl"
	else:
		package = "numpy-1.11.0-cp27-none-win32.whl"
		
	if call(["pip", "install", "Install/" + package]):
		sys.exit(0)
		

	sys.exit(1)
	
if __name__ == "__main__":
   main(sys.argv[1:])