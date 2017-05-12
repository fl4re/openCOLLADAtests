from common.test_runner import TestRunner
import os
import unittest
import xml.etree.ElementTree as Et

#
# Base class for unit tests.
# Contains utility methods.
#
class TestCaseBase(unittest.TestCase):
    namespaces = {
        "collada": "http://www.collada.org/2005/11/COLLADASchema"
    }

    # Loads a DAE.
    # DAE path is computed from unit test file path and source file name.
    #
    # Example:
    # Unit test file path:
    # C:\OpenCOLLADAtests\colladamaya\tests\camera\TestCamera.py
    # Source file name:
    # Cube.mb
    # Computed DAE path:
    # C:\OpenCOLLADAtests\test_results\colladamaya\tests\camera\Cube.dae
    @staticmethod
    def load_dae(unittest_file_path, source_file_name):
        dae = TestRunner.output_dae_from_input(
            os.path.join(os.path.normpath(os.path.dirname(unittest_file_path)), source_file_name))
        return Et.parse(dae)

    # Returns first element with attribute 'id'=id.
    @staticmethod
    def get_element_by_id(root, id):
        return root.find(".//*[@id='" + id + "']")

    # Returns first element with given tag.
    @staticmethod
    def get_element_by_tag(root, tag):
        return root.find(".//" + tag, TestCaseBase.namespaces)

    # Returns elements with given tag
    @staticmethod
    def get_elements_by_tag(root, tag):
        return root.findall(".//" + tag, TestCaseBase.namespaces)