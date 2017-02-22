from abc import ABCMeta, abstractmethod


#
# Base class to implement to support new software to test.
#
class Tool(object):
    __metaclass__ = ABCMeta

    registered_tools = []

    def __init__(self):
        super(Tool, self).__init__()
        Tool.registered_tools.append(self)

    # Set tool version. (2015, 2017, ...)
    @abstractmethod
    def set_version(self, version):
        raise NotImplementedError('not implemented')

    # Returns plugin name. (COLLADAMaya, COLLADAMax, ...)
    @abstractmethod
    def plugin_name(self):
        raise NotImplementedError('not implemented')

    # Returns tool name. (Maya, 3DSMax, ...)
    @abstractmethod
    def tool_name(self):
        raise NotImplementedError('not implemented')

    # Returns path to root folder containing source files and unit tests.
    @abstractmethod
    def tests_path(self):
        raise NotImplementedError('not implemented')

    # Returns source file extensions supported by this tool. (['.ma', '.mb'], ['.max'], ...)
    @abstractmethod
    def get_extensions(self):
        raise NotImplementedError('not implemented')

    # Exports source file to DAE with given options.
    @abstractmethod
    def export_file(self, input_file, output_file, options):
        raise NotImplementedError('not implemented')

    # Imports DAE.
    @abstractmethod
    def import_file(self, input_file):
        raise NotImplementedError('not implemented')

    # Returns default export options as a string.
    @abstractmethod
    def default_export_options(self):
        raise NotImplementedError('not implemented')
