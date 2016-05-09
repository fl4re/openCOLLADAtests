import sys
import maya.standalone as std

std.initialize(name='python')
import maya.cmds as cmds

plugin_name = sys.argv[1]
input_filename = sys.argv[2]
output_filename = sys.argv[3]

# name of the 'importer'
importer = 'OpenCOLLADA importer'


def importFile(plugin_name, input_filename, output_filename):
    try:
        # Load colladaMaya plugin
        cmds.loadPlugin(plugin_name)

        # import with colladaMaya plugin
        cmds.file(input_filename, i=1, type=importer, force=True)

        # save the scene in .ma
        cmds.file(rename=output_filename)
        cmds.file(save=True, type='mayaAscii')

    except Exception, e:
        sys.stderr.write(str(e))
        sys.exit(-1)


importFile(plugin_name, input_filename, output_filename)
