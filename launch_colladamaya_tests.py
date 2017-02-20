from common.util import *
from argparse import ArgumentParser
from common.opencollada import OpenCOLLADA
from colladamaya.maya import Maya
from common.test_runner import TestRunner

# Runs this python file to launch Maya tests.

# TODO factorize with launch_colladamax_tests.py
# launch_tests.py --tool=maya --version=2015
# launch_tests.py --tool=max --version=2017

if __name__ != '__main__':
    sys.exit(1)

parser = ArgumentParser(description="COLLADAMaya tests")
parser.add_argument("version", help="Maya version (2015, 2017...)")
options = parser.parse_args()

print "Testing COLLADAMaya " + options.version + " x64"

maya = Maya(options.version)

print 'Using OpenCOLLADA path=' + OpenCOLLADA.path()
print 'Using Maya path=' + maya.path()

# install COLLADAMaya plugin
print 'Installing COLLADAMaya plugin...'
maya.install_plugin()

# run tests
res = 0
test_runner = TestRunner(maya)
res |= test_runner.run_export_test()
# res |= test_runner.test_import()

if res == 0:
    print "COLLADAMaya Tests SUCCEEDED"
else:
    print "COLLADAMaya Tests FAILED"

sys.exit(res)
