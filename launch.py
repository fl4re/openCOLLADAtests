from argparse import ArgumentParser
from colladamaya.maya import Maya
from colladamax.max import Max
from common.opencollada import OpenCOLLADA
from common.test_runner import TestRunner
from common.util import *

# Runs this python file to launch tests.

if __name__ != '__main__':
    sys.exit(1)

# Register tools here.
tools = [
    Maya(),
    Max()
]

plugins_str = ''
first = True
for tool in tools:
    if not first:
        plugins_str += ', '
    plugins_str += tool.tool_name()
    first = False

parser = ArgumentParser(description='OpenCOLLADA plugins tests')
parser.add_argument('--tool', default='Maya', help='Tool to test (' + plugins_str + ')')
parser.add_argument('--version', default='2015', help='Tool version (2015, 2017...)')
options = parser.parse_args()

tested_tool = None
for tool in tools:
    if tool.tool_name() == options.tool:
        tested_tool = tool
        tested_tool.set_version(options.version)
        break

if tested_tool is None:
    print 'Unsupported tool: ' + options.tool
    sys.exit(1)

print 'Testing ' + tested_tool.plugin_name() + ' ' + options.version + " x64"

print 'Using OpenCOLLADA path=' + OpenCOLLADA.path()
print 'Using ' + tested_tool.tool_name() + ' path=' + tested_tool.path()

# Install plugin.
print 'Installing ' + tested_tool.plugin_name() + ' plugin...'
tested_tool.install_plugin()

# Run tests.
res = 0
test_runner = TestRunner(tested_tool)
res |= test_runner.run_export_test()
# res |= test_runner.test_import()

if res == 0:
    print tested_tool.plugin_name() + ' tests SUCCEEDED'
else:
    print tested_tool.plugin_name() + ' tests FAILED'

sys.exit(res)
