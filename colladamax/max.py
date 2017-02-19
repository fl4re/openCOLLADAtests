from common.util import *
from common.cad_tool import CADTool
from common.opencollada import OpenCOLLADA
from common.opencolladatests import OpenCOLLADATests
from shutil import copy


class Max(CADTool):
    def __init__(self, version):
        self.version = version
        self.smax_path = os.environ.get('ADSK_3DSMAX_x64_' + version)
        if self.smax_path is None:
            self.smax_path = 'C:\\Program Files\\Autodesk\\3ds Max ' + version

        # TODO

        #self.export_script_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'maya_export_script.py')
        bin_path = os.path.join(self.smax_path, 'bin')
        plugins_path = os.path.join(bin_path, 'plug-ins')
        self.colladasmax_path = os.path.join(plugins_path, 'COLLADAMaya')
        #self.mayapy_path = os.path.join(bin_path, "mayapy")
        if get_platform() == 'windows':
            self.mayapy_path += '.exe'
            self.colladasmax_path += '.mll'

    def name(self):
        return 'colladamax'

    def path(self):
        return self.smax_path

    def data_set_path(self):
        return os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data_set')

    def install_plugin(self):
        # TODO
        maya_plugins_path = os.path.join(self.smax_path, 'bin' + os.path.sep + 'plug-ins')
        maya_scripts_path = os.path.join(self.smax_path, 'scripts' + os.path.sep + 'others')
        collada_smax_path = os.path.join(OpenCOLLADA.path(), 'COLLADAMaya')
        mll_path = os.path.join(collada_smax_path,
                                'bin' + os.path.sep + 'win' + os.path.sep + 'x64' + os.path.sep +
                                'ReleasePlugin' + self.version + os.path.sep + 'COLLADAMaya.mll')
        scripts_path = os.path.join(collada_smax_path, 'scripts')
        exporter_mel_path = os.path.join(scripts_path, 'openColladaExporterOpts.mel')
        importer_mel_path = os.path.join(scripts_path, 'openColladaImporterOpts.mel')
        print 'copying ' + mll_path + ' to ' + maya_plugins_path
        copy(mll_path, maya_plugins_path)
        print 'copying ' + exporter_mel_path + ' to ' + maya_scripts_path
        copy(exporter_mel_path, maya_scripts_path)
        print 'copying ' + importer_mel_path + ' to ' + maya_scripts_path
        copy(importer_mel_path, maya_scripts_path)

    def get_extensions(self):
        return ['.max']

    def export_file(self, input_file, output_file, options):
        # TODO
        return run('', '')

    def import_file(self, input_file):
        # TODO
        raise NotImplementedError('not implemented')
