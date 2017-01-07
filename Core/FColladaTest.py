from Core.FColladaParser import FColladaParser
from Core.FCommon import *
from Core.FExporter import FExporter
from Core.FImageComparator import FImageComparator
from Core.FImporter import FImporter
from Core.FRenderer import FRenderer
from Core.FUnitTest import FUnitTest
from Core.FValidator import FValidator
from Common.Util import *


def find_file(root_dir, filename, parent_dir_partial_name=''):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if parent_dir_partial_name == '' or dirpath.endswith(parent_dir_partial_name):
            for f in filenames:
                if f == filename:
                    return os.path.join(dirpath, f)
    return ''


class FColladaTest:
    def __init__(self, input_filename):
        # name of the DAE to be imported
        self.input_filename = input_filename

        opencolladatests_path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
        maya_installation_path = os.environ.get("MAYA_PATH2015_X64")
        if maya_installation_path is None:
            if get_platform() == "windows":
                maya_installation_path = "C:\\Program Files\\Autodesk\\Maya2015"
            elif get_platform() == "macosx":
                maya_installation_path = "/Applications/Autodesk/maya2015"

        opencollada_path = os.environ.get("OPENCOLLADA_PATH")
        if opencollada_path is None:
            opencollada_path = os.path.normpath(os.path.join(opencolladatests_path, ".." + os.path.sep + "OpenCOLLADA"))

        self.config = {}

        self.config["opencolladatests_path"] = opencolladatests_path
        self.config["opencollada_path"] = opencollada_path
        self.config["core_path"] = os.path.join(self.config["opencolladatests_path"], "Core")
        self.config["maya_installation_path"] = maya_installation_path
        if get_platform() == 'windows':
            self.config["maya_bin_path"] = os.path.join(self.config["maya_installation_path"], "bin")
            self.config["maya_plugins_path"] = os.path.join(self.config["maya_bin_path"], "plug-ins")
            self.config["colladamaya_path"] = os.path.join(self.config["maya_plugins_path"], "COLLADAMaya")
        elif get_platform() == 'macosx':
            self.config["maya_bin_path"] = os.path.join(self.config["maya_installation_path"], "Maya.app" + os.path.sep + "Contents" + os.path.sep + "bin")
            self.config["maya_plugins_path"] = os.path.join(self.config["maya_installation_path"], "plug-ins")
            self.config["colladamaya_path"] = os.path.join(self.config["maya_plugins_path"], "OpenCOLLADA" + os.path.sep + "COLLADAMaya")
        self.config["mayapy_path"] = os.path.join(self.config["maya_bin_path"], "mayapy")
        self.config["maya_path"] = os.path.join(self.config["maya_bin_path"], "maya")
        self.config["render_path"] = os.path.join(self.config["maya_bin_path"], "Render")

        validator_exe_name = "DAEValidator"

        if get_platform() == "windows":
            self.config["mayapy_path"] += ".exe"
            self.config["maya_path"] += ".exe"
            self.config["render_path"] += ".exe"
            self.config["colladamaya_path"] += ".mll"
            validator_exe_name += ".exe"

        self.config["validator_path"] = find_file(self.config["opencollada_path"], validator_exe_name, "Release")

        # name of the maya saved from the imported DAE
        self.output_maya_file = os.path.join(self.config["opencolladatests_path"], RESULT_DIR + MAYA_FILE_MA)

        self.importer = FImporter(self.config)
        self.exporter = FExporter(self.config)
        self.renderer = FRenderer(self.config)
        self.validator = FValidator(self.config)
        self.imageComparator = FImageComparator(self.config)
        self.unitTest = FUnitTest(self.config)
        self.colladaParser = FColladaParser(self.config)

    #######################################################################################
    @staticmethod
    def GetRoot():
        return FColladaParser.GetRoot()

    @staticmethod
    def GetElementByID(daeElement, strId):
        return FColladaParser.GetElementByID(daeElement, strId)

    @staticmethod
    def GetElementsByTags(daeElement, tagLst):
        return FColladaParser.GetElementsByTags(daeElement, tagLst)

    #######################################################################################

    def DoRender(self, input_filename):
        return self.renderer.DoRender(input_filename)

    def DoImport(self, input_filename, output_maya_file):
        return self.importer.DoImport(input_filename, output_maya_file)

    def DoExport(self, Maya_filename, DAE_filename, option):
        return self.exporter.DoExport(Maya_filename, DAE_filename, option)

    # UnitTest
    def DoUnitTest(self, DAE_filename, unitTestDir, xmlResultFile):
        self.colladaParser.ParseDOM(DAE_filename)
        return self.unitTest.DoUnitTest(unitTestDir, xmlResultFile)

    def DoValidate(self, output_filename, logName):
        return self.validator.DoValidate(output_filename, logName)

    def DoProcess(self):

        print("--DO PROCESS FColladaTest")
        if not os.path.exists(self.config["opencolladatests_path"] + RESULT_DIR):
            os.makedirs(self.config["opencolladatests_path"] + RESULT_DIR)
        return 0
