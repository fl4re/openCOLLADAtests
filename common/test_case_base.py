from common.test_runner import TestRunner
import os
import unittest
import xml.etree.ElementTree as Et


class TestCaseBase(unittest.TestCase):
    namespaces = {
        "collada": "http://www.collada.org/2005/11/COLLADASchema"
    }

    def load_dae(self, unittest_file_path, source_file_name):
        dae = TestRunner.output_dae_from_input(
            os.path.join(os.path.normpath(os.path.dirname(unittest_file_path)), source_file_name))
        self.doc = Et.parse(dae)

    @staticmethod
    def get_element_by_id(root, id):
        return root.find(".//*[@id='" + id + "']")

    @staticmethod
    def get_element_by_tag(root, tag):
        return root.find(".//" + tag, TestCaseBase.namespaces)

    @staticmethod
    def get_elements_by_tag(root, tag):
        return root.findall(".//" + tag, TestCaseBase.namespaces)