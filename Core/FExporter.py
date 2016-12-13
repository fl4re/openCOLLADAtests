import subprocess
import os
from FCommon import *
from Common.Util import *


class FExporter:
    def __init__(self, config):

        self.config = config
        self.scriptExportPath = os.path.join(self.config["opencolladatests_path"],
                                             'Core' + os.path.sep + 'FExportCmd.py')

    # input_filename = Maya filename .ma
    # output_filename = DAE filename
    def DoExport(self, input_filename, output_filename, option):

        print("--DO EXPORT")
        print '%s = output_filename' % (output_filename + '.' + DAE_EXT)

        newinput = input_filename.replace('\\', '/')
        newoutput = output_filename.replace('\\', '/')


        pluginName = "COLLADAMaya.mll"
        exporter = 'OpenCOLLADA exporter'

        #Can override export options with option.txt file included in specific folder in DataSet
        optionfile = newinput + '\\..\\' + "option.txt"
        optionfile = optionfile.replace('\\', '/')
        if os.path.isfile(optionfile):
            option = open(optionfile).read()

        # Launch Maya.exe with -script melFile option
        # this mel script file is created here
        melScript = output_filename + '\\..\\'
        melScript = melScript.replace('\\', '/')
        melScript = melScript + "/script.mel"
		
        file = open(melScript, "w")
        file.write('loadPlugin')
        file.write(' "' + pluginName + '";\n')
        file.write('string $opencollada_test_dir;\n')
        file.write('$opencollada_test_dir=`pwd`;\n')
        file.write('setProject $opencollada_test_dir;\n')
        file.write('file -f -o')
        file.write(' "' + newinput + '";\n' )
        file.write('refresh;\n')
        file.write('file -f -type')
        file.write(' "' + exporter + '"')
        file.write(' -op')
        file.write(' "' + option + '"')
        file.write(' -ea ')
        file.write('"' + newoutput + '.dae";\n' )
        file.write('quit -f -a;\n')
        file.close()

        exitcode = run(
            '"' + self.config["maya_path"] + '"' +
            ' -script' +  ' ' + melScript + ' '
        )


        if str(exitcode) != '0':
            print 'error exporting: %s' % input_filename
        else:
            print '%s exported' % input_filename

        return exitcode
