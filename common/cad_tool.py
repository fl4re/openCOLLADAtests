from abc import ABCMeta, abstractmethod


#
# Base class to implement to support new CAD software to test.
#
class CADTool(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def name(self):
        raise NotImplementedError('not implemented')

    @abstractmethod
    def data_set_path(self):
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