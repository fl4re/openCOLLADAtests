# Be sure no maya.py file exists at the same level of this file

import sys
import maya.standalone as std
import maya.cmds as cmds
std.initialize(name='python')

plugin_name = sys.argv[1]
input_filename = sys.argv[2]
output_filename = sys.argv[3]
option = sys.argv[4]

# name of the 'exporter'
exporter = 'OpenCOLLADA exporter'


def exportFile(plugin_name, input_filename, ouput_filename, option):
    try:

        # Load colladaMaya plugin
        cmds.loadPlugin(plugin_name)

        # Open .ma
        cmds.file(input_filename, o=1, f=1)

        # export with colladaMaya plugin
        cmds.file(ouput_filename, op=option, type=exporter, pr=True, ea=True, force=True)

    except Exception, e:
        sys.stderr.write(str(e))
        sys.exit(-1)


exportFile(plugin_name, input_filename, output_filename, option)
