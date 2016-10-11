from Core.Common.Util import *

currentDirectory = os.path.dirname(os.path.realpath(__file__))

maya_path = os.environ.get('MAYA_PATH2015_X64')
if maya_path is None:
    if get_platform() == 'windows':
        os.environ['MAYA_PATH2015_X64'] = 'C:\\Program Files\\Autodesk\\Maya2015'
    elif get_platform() == 'macosx':
        os.environ['MAYA_PATH2015_X64'] = '/Applications/Autodesk/maya2015'

opencollada_path = os.environ.get('OPENCOLLADA_PATH')
if opencollada_path is None:
    os.environ['OPENCOLLADA_PATH'] = os.path.normpath(
        os.path.join(currentDirectory, '..' + os.path.sep + 'OpenCOLLADA'))

print 'using OPENCOLLADA_PATH=' + os.environ['OPENCOLLADA_PATH']
print 'using MAYA_PATH2015_X64=' + os.environ['MAYA_PATH2015_X64']

if not os.path.exists(os.environ['MAYA_PATH2015_X64']):
    print "Error: " + os.environ['MAYA_PATH2015_X64'] + " doesn't exist."
    sys.exit(1)

if not os.path.exists(os.environ['OPENCOLLADA_PATH']):
    print "Error: " + os.environ['OPENCOLLADA_PATH'] + " doesn't exist."
    sys.exit(1)

exitcode = 0

# install COLLADAMaya plugin
exitcode |= run('python install_plugin.py', currentDirectory)

# run tests
exitcode |= run('python main.py --export-test', currentDirectory)

sys.exit(exitcode)