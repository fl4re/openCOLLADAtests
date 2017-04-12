import common.test_case_base
from urlparse import urlparse


class SourceDataDefaultTestSuite(common.test_case_base.TestCaseBase):
    def setUp(self):
        super(self.__class__, self).setUp()
        self.load_dae(__file__, 'source_data_default.mb')

    def test_source_data_default(self):
        source_data = self.get_element_by_tag(self.doc.getroot(), 'collada:source_data')
        self.assertIsNotNone(source_data)
        parts = urlparse(source_data.text)
        self.assertEqual(parts.path, './source_data_default.mb')
