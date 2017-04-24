from common.util import *
from common.tool import Tool
#from common.opencollada import OpenCOLLADA
from common.opencolladatests import OpenCOLLADATests
from shutil import copy
import ast

class Mobu(Tool):
    def __init__(self, version=None):
        super(Mobu, self).__init__()
        self.version = None
        self.mobu_path = None
        self.mobu_exe_path = None
        self.export_script_path = None
        if version is not None:
            self.set_version(version)

    def set_version(self, version):
        self.version = version
        self.mobu_path = os.environ.get('MOTIONBUILDER_PATH_' + version)
        if self.mobu_path is None:
            self.mobu_path = 'C:\\Program Files\Autodesk\MotionBuilder 20' + version

        bin_path = os.path.join(self.mobu_path, 'bin' + os.path.sep + 'x64')
        self.mobu_exe_path = os.path.join(bin_path, 'motionbuilder.exe')
        self.export_script_path = os.path.join(os.path.dirname(os.path.normpath(__file__)),
                                               'scripts' + os.path.sep + 'mobu_export_script.py')

    def plugin_name(self):
        return 'FCOLLADAMobu'

    def tool_name(self):
        return 'Mobu'

    def path(self):
        return self.mobu_path

    def tests_path(self):
        return os.path.join(os.path.dirname(os.path.normpath(os.path.realpath(__file__))), 'tests')

    def install_plugin(self):
        mobu_plugins_path = os.path.join(self.mobu_path, 'bin' + os.path.sep + 'x64' + os.path.sep + 'plugins')
        collada_mobu_path = os.path.normpath(os.path.join(OpenCOLLADATests.path(), '..' + os.path.sep + 'COLLADAMobu'))

        pyd_path = os.path.join(collada_mobu_path,
                                'ColladaMotionBuilder' + os.path.sep + 'x64' + os.path.sep + 'MB' + self.version + '.0 Release' + os.path.sep + 'ColladaMotionBuilder.pyd')

        print 'copying ' + pyd_path + ' to ' + mobu_plugins_path
        copy(pyd_path, mobu_plugins_path)

    def get_extensions(self):
        return ['.fbx']

    def export_file(self, input_file, output_file, options):

        export_boneList = options.get('boneList')
        if export_boneList is None:
            export_boneList = self.default_export_options()['boneList']

        export_indexTake = options.get('indexTake')
        if export_indexTake is None:
            export_indexTake = self.default_export_options()['indexTake']

        script_path = os.path.splitext(output_file)[0] + '.py'
        f = open(script_path, 'w')

        f.write('from pyfbsdk import *\n')
        f.write('from ColladaMotionBuilder import *\n')
        f.write('NO_LOAD_UI_DIALOG = False\n')
        f.write('OPTION_USED_FOR_LOADING = True\n')
        f.write('app = FBApplication()\n')
        f.write('options = FBFbxOptions(OPTION_USED_FOR_LOADING)\n')

        f.write('input =  "' + input_file.replace('\\', '/') + '";\n')
        f.write('output =  "' + output_file.replace('\\', '/') + '";\n')
        f.write('app.FileOpen(input, False, options)\n')

        list = ast.literal_eval(export_boneList)
        f.write('boneList = ["' + '","'.join(str(x) for x in list) + '"];\n')

        f.write('indexTake = ' + str(export_indexTake) + ';\n')

        f.write('MobuColladaExporter(output, indexTake, boneList, False, True) \n')
        f.write('app.FileExit()\n')
        f.close()

        res = run(
            '"' + self.mobu_exe_path + '"' +
            ' "' + script_path + '"'
        )
        os.remove(script_path)
        return res

    def import_file(self, input_file):
        # TODO
        raise NotImplementedError('not implemented')

    def default_export_options(self):
        return {
            'boneList': 'Hips',
            'indexTake': 0
        }

    def is_supported(self):
        return get_platform() == 'windows'
