from common.util import *
from argparse import ArgumentParser
from common.opencollada import OpenCOLLADA
from colladamax.max import Max
from common.test_runner import TestRunner

if __name__ != '__main__':
    sys.exit(1)

if get_platform() != 'windows':
    sys.exit(1)

parser = ArgumentParser(description="COLLADAMax tests")
parser.add_argument("version", help="3DSMax version (2015, 2017...)")
options = parser.parse_args()

print "Testing COLLADAMax " + options.version + " x64"

smax = Max(options.version)

print 'Using OpenCOLLADA path=' + OpenCOLLADA.path()
print 'Using 3DSMax path=' + smax.path()

# install COLLADAMax plugin
print 'Installing COLLADAMax plugin...'
smax.install_plugin()

# run tests
res = 0
test_runner = TestRunner(smax)
res |= test_runner.test_export()
# res |= test_runner.test_import()

if res == 0:
    print "COLLADAMax Tests SUCCEEDED"
else:
    print "COLLADAMax Tests FAILED"

sys.exit(res)
