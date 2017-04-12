# Be sure no maya.py file exists at the same level of this file

import sys
import maya.standalone as std
import maya.cmds as cmds
import maya.mel as mel
std.initialize(name='python')

plugin_name = sys.argv[1]
input_filename = sys.argv[2]
output_filename = sys.argv[3]
option = sys.argv[4]

# name of the 'exporter'
exporter = 'OpenCOLLADA exporter'


def export_file(plugin_name, input_filename, ouput_filename, option):

    source_dir = input_filename
    source_dir = source_dir.replace('\\', '/')
    last_sep = source_dir.rfind('/')
    source_dir = source_dir[0:last_sep]
    mel.eval('setProject "' + source_dir + '"')

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


export_file(plugin_name, input_filename, output_filename, option)
