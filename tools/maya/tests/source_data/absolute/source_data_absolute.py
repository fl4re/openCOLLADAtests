import common.test_case_base
from urlparse import urlparse


class SourceDataAbsoluteTestSuite(common.test_case_base.TestCaseBase):
    def setUp(self):
        super(self.__class__, self).setUp()
        self.load_dae(__file__, 'source_data_absolute.mb')

    @staticmethod
    def is_absolute(path):
        return path.startswith('/')

    def test_source_data_absolute(self):
        source_data = self.get_element_by_tag(self.doc.getroot(), 'collada:source_data')
        self.assertIsNotNone(source_data)
        parts = urlparse(source_data.text)
        self.assertEqual(parts.scheme, "file")
        self.assertTrue(self.__class__.is_absolute(parts.path))
        self.assertTrue(parts.path.endswith('/tools/maya/tests/source_data/absolute/source_data_absolute.mb'))
