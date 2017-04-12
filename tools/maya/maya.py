from common.util import *
from common.tool import Tool
from common.opencollada import OpenCOLLADA
from common.opencolladatests import OpenCOLLADATests
from shutil import copy


class Maya(Tool):
    def __init__(self, version=None):
        super(Maya, self).__init__()
        self.version = None
        self.maya_path = None
        self.export_script_path = None
        self.colladamaya_path = None
        self.mayaexe_path = None
        self.mayapy_path = None
        if version is not None:
            self.set_version(version)

    def set_version(self, version):
        self.version = version
        self.maya_path = os.environ.get('MAYA_PATH' + version + '_X64')
        if self.maya_path is None:
            if get_platform() == 'windows':
                self.maya_path = 'C:\\Program Files\\Autodesk\\Maya' + version
            elif get_platform() == 'macosx':
                self.maya_path = '/Applications/Autodesk/maya' + version
            else:
                raise 'platform not supported: ' + get_platform()
        self.export_script_path = os.path.join(os.path.dirname(os.path.normpath(__file__)),
                                               'scripts' + os.path.sep + 'maya_export_script.py')
        if get_platform() == 'windows':
            bin_path = os.path.join(self.maya_path, 'bin')
            plugins_path = os.path.join(bin_path, 'plug-ins')
            self.colladamaya_path = os.path.join(plugins_path, 'COLLADAMaya')
        elif get_platform() == 'macosx':
            bin_path = os.path.join(self.maya_path, "Maya.app" + os.path.sep + "Contents" + os.path.sep + "bin")
            plugins_path = os.path.join(self.maya_path, 'plug-ins')
            self.colladamaya_path = os.path.join(plugins_path, 'OpenCOLLADA' + os.path.sep + 'COLLADAMaya')
        else:
            raise Exception('Unsupported platform: ' + get_platform())
        self.mayaexe_path = os.path.join(bin_path, 'maya')
        self.mayapy_path = os.path.join(bin_path, 'mayapy')
        if get_platform() == 'windows':
            self.mayaexe_path += '.exe'
            self.mayapy_path += '.exe'
            self.colladamaya_path += '.mll'

    def plugin_name(self):
        return 'COLLADAMaya'

    def tool_name(self):
        return 'Maya'

    def path(self):
        return self.maya_path

    def tests_path(self):
        return os.path.join(os.path.dirname(os.path.normpath(os.path.realpath(__file__))), 'tests')

    def install_plugin(self):
        if get_platform() == 'windows':
            maya_plugins_path = os.path.join(self.maya_path, 'bin' + os.path.sep + 'plug-ins')
            maya_scripts_path = os.path.join(self.maya_path, 'scripts' + os.path.sep + 'others')
            collada_maya_path = os.path.join(OpenCOLLADA.path(), 'COLLADAMaya')
            mll_path = os.path.join(collada_maya_path,
                                    'bin' + os.path.sep + 'win' + os.path.sep + 'x64' + os.path.sep +
                                    'ReleasePlugin' + self.version + os.path.sep + 'COLLADAMaya.mll')
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
            maya_plugins_path = os.path.join(self.maya_path, 'plug-ins' + os.path.sep + 'OpenCOLLADA')
            bundle_path = os.path.join(OpenCOLLADA.path(),
                                       'COLLADAMaya' + os.path.sep + 'Build' + os.path.sep + 'Release ' + self.version +
                                       os.path.sep + 'COLLADAMaya.bundle')
            print 'copying ' + bundle_path + ' to ' + maya_plugins_path
            copy(bundle_path, maya_plugins_path)

    def get_extensions(self):
        return ['.ma', '.mb']

    def export_file(self, input_file, output_file, options):
        export_options = options.get('export_options')
        if export_options is None:
            export_options = self.default_export_options()['export_options']

        use_mayapy = options.get('mayapy')
        if use_mayapy is None:
            use_mayapy = self.default_export_options()['mayapy']

        if use_mayapy:
            # Run Maya without UI.
            return run('"' + self.mayapy_path + '"' +
                       ' "' + self.export_script_path + '"' +
                       ' "' + self.colladamaya_path + '"' +
                       ' "' + input_file + '"' +
                       ' "' + output_file + '" ' +
                       ' "' + export_options + '"')
        else:
            # Run Maya with UI (required to use cgfx for example)
            mel_path = os.path.splitext(output_file)[0] + '.mel'

            f = open(mel_path, 'w')
            f.write('loadPlugin')
            f.write(' "' + self.colladamaya_path.replace('\\', '/') + '";\n')
            f.write('string $opencollada_test_dir;\n')
            f.write('$opencollada_test_dir="' + os.path.dirname(input_file).replace('\\', '/') + '";\n')
            f.write('setProject $opencollada_test_dir;\n')
            f.write('file -f -o')
            f.write(' "' + input_file.replace('\\', '/') + '";\n')
            f.write('refresh;\n')
            f.write('file -f -type')
            f.write(' "OpenCOLLADA exporter"')
            f.write(' -op')
            f.write(' "' + export_options + '"')
            f.write(' -ea ')
            f.write('"' + output_file.replace('\\', '/') + '.dae";\n')
            f.write('quit -f -a;\n')
            f.close()

            res = run('"' + self.mayaexe_path + '" -script "' + mel_path + '"')

            os.remove(mel_path)

            return res

    def import_file(self, input_file):
        # TODO
        raise NotImplementedError('not implemented')

    def default_export_options(self):
        return {
            'export_options': 'bakeTransforms=1;exportLights=0',
            'mayapy': True
        }

    def is_supported(self):
        return True
