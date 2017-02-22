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

    @abstractmethod
    def set_version(self, version):
        raise NotImplementedError('not implemented')

    @abstractmethod
    def plugin_name(self):
        raise NotImplementedError('not implemented')

    @abstractmethod
    def tool_name(self):
        raise NotImplementedError('not implemented')

    @abstractmethod
    def tests_path(self):
        raise NotImplementedError('not implemented')

    @abstractmethod
    def get_extensions(self):
        raise NotImplementedError('not implemented')

    @abstractmethod
    def export_file(self, input_file, output_file, options):
        raise NotImplementedError('not implemented')

    @abstractmethod
    def import_file(self, input_file):
        raise NotImplementedError('not implemented')

    @abstractmethod
    def default_export_options(self):
        raise NotImplementedError('not implemented')
