from common.util import *
from common.tool import Tool
from common.opencollada import OpenCOLLADA
from common.opencolladatests import OpenCOLLADATests
from shutil import copy


class Max(Tool):
    def __init__(self, version=None):
        # 3DSMax is Windows only.
        if get_platform() != 'windows':
            raise Exception('3DSMax is available on Windows only.')
        super(Max, self).__init__()
        self.version = None
        self.smax_path = None
        self.smax_exe_path = None
        self.export_script_path = None
        if version is not None:
            self.set_version(version)

    def set_version(self, version):
        self.version = version
        self.smax_path = os.environ.get('ADSK_3DSMAX_x64_' + version)
        if self.smax_path is None:
            self.smax_path = 'C:\\Program Files\\Autodesk\\3ds Max ' + version
        self.smax_exe_path = os.path.join(self.smax_path, '3dsmax.exe')
        self.export_script_path = os.path.join(os.path.dirname(os.path.normpath(__file__)),
                                               'scripts' + os.path.sep + 'max_export_script.ms')

    def plugin_name(self):
        return 'COLLADAMax'

    def tool_name(self):
        return '3DSMax'

    def path(self):
        return self.smax_path

    def tests_path(self):
        return os.path.join(os.path.dirname(os.path.normpath(os.path.realpath(__file__))), 'tests')

    def install_plugin(self):
        smax_plugins_path = os.path.join(self.smax_path, 'plugins')
        colladamax_path = os.path.join(OpenCOLLADA.path(), 'COLLADAMax')
        dle_path = os.path.join(colladamax_path,
                                'bin' + os.path.sep +
                                'win' + os.path.sep +
                                'x64' + os.path.sep +
                                'Release_Max' + self.version + os.path.sep +
                                'COLLADAMaxNew.dle')
        print 'copying ' + dle_path + ' to ' + smax_plugins_path
        copy(dle_path, smax_plugins_path)

    def get_extensions(self):
        return ['.max']

    def export_file(self, input_file, output_file, options):
        input = input_file.replace('\\', '\\\\')
        output = output_file.replace('\\', '\\\\')
        script_path = os.path.splitext(output_file)[0] + '.ms'
        f = open(script_path, 'w')
        script = 'loadMaxFile "{0}"\n' \
                 'exportFile "{1}" #noPrompt using:OpenCOLLADAExporter\n' \
                 'quitMax #noPrompt'.format(input, output)
        f.write(script)
        f.close()
        res = run(
            '"' + self.smax_exe_path + '"' +
            ' -silent -q -U MAXScript "' + script_path + '"'
        )
        os.remove(script_path)
        return res

    def import_file(self, input_file):
        # TODO
        raise NotImplementedError('not implemented')

    def default_export_options(self):
        return {}
