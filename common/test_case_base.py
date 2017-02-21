from common.test_runner import TestRunner
import os
import unittest
import xml.etree.ElementTree as Et


class TestCaseBase(unittest.TestCase):
    def load_dae(self, unittest_file_path, source_file_name):
        dae = TestRunner.output_dae_from_input(
            os.path.join(os.path.normpath(os.path.dirname(unittest_file_path)), source_file_name))
        self.doc = Et.parse(dae)

    def get_element_by_id(self, id):
        return self.doc.find(".//*[@id='" + id + "']")