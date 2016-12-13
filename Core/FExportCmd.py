import sys
import maya.standalone as std
import maya.cmds as cmds
std.initialize(name='python')

pluginFix_name = sys.argv[1]
plugin_name = sys.argv[2]
input_filename = sys.argv[3]
output_filename = sys.argv[4]
option = sys.argv[5]

# name of the 'exporter'
exporter = 'OpenCOLLADA exporter'


def exportFile(pluginFix_name, plugin_name, input_filename, ouput_filename, option):
    try:

        cmds.unloadPlugin("C:\\Program Files\\Autodesk\\Maya2015\\bin\\plug-ins\\cgfxShader.mll")


        cmds.loadPlugin(pluginFix_name)
        cmds.forceCGContext()

        cmds.loadPlugin("C:\\Program Files\\Autodesk\\Maya2015\\bin\\plug-ins\\cgfxShader.mll")


        # Open .ma
        cmds.file(input_filename, o=1, f=1)
       # cmds.forceCgfxShaderFix()
        cmds.forceToCreateCgEffect()

        # Load colladaMaya plugin
        cmds.loadPlugin(plugin_name)

        # export with colladaMaya plugin
        cmds.file(ouput_filename, op=option, type=exporter, pr=True, ea=True, force=True)

    except Exception, e:
        sys.stderr.write(str(e))
        sys.exit(-1)


exportFile(pluginFix_name, plugin_name, input_filename, output_filename, option)
