from Core.Common.Util import *
from shutil import copy

maya_path = os.environ.get('MAYA_PATH2015_X64')
if maya_path is None:
    print 'MAYA_PATH2015_X64 environment variable is not set. It must point to Maya2015 installation folder.'
    sys.exit(1)

opencollada_path = os.environ.get('OPENCOLLADA_PATH')
if opencollada_path is None:
    print 'OPENCOLLADA_PATH environment variable is not set. It must point to OpenCOLLADA folder.'
    sys.exit(1)

if get_platform() == 'windows':
    maya_plugins_path = os.path.join(maya_path, 'bin' + os.path.sep + 'plug-ins')
    maya_scripts_path = os.path.join(maya_path, 'scripts' + os.path.sep + 'others')
    collada_maya_path = os.path.join(opencollada_path, 'COLLADAMaya')
    mll_path = os.path.join(collada_maya_path,
                            'bin' + os.path.sep + 'win' + os.path.sep + 'x64' + os.path.sep + 'ReleasePlugin2015' +
                            os.path.sep + 'COLLADAMaya.mll')
    scripts_path = os.path.join(collada_maya_path, 'scripts')
    exporter_mel_path = os.path.join(scripts_path, 'openColladaExporterOpts.mel')
    importer_mel_path = os.path.join(scripts_path, 'openColladaImporterOpts.mel')
    print 'copying ' + mll_path + ' to ' + maya_plugins_path
    copy(mll_path, maya_plugins_path)
    print 'copying ' + exporter_mel_path + ' to ' + maya_scripts_path
    copy(exporter_mel_path, maya_scripts_path)
    print 'copying ' + importer_mel_path + ' to ' + maya_scripts_path
    copy(importer_mel_path, maya_scripts_path)

elif get_platform() == 'macosx':
    maya_plugins_path = os.path.join(maya_path, 'plug-ins' + os.path.sep + 'OpenCOLLADA')
    bundle_path = os.path.join(opencollada_path,
                               'COLLADAMaya' + os.path.sep + 'Build' + os.path.sep + 'Release 2015' + os.path.sep +
                               'COLLADAMaya.bundle')
    print 'copying ' + bundle_path + ' to ' + maya_plugins_path
    copy(bundle_path, maya_plugins_path)
