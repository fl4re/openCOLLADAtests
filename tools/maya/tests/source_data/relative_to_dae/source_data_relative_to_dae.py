import common.test_case_base
from urlparse import urlparse


class SourceDataRelativeToDAETestSuite(common.test_case_base.TestCaseBase):
    def setUp(self):
        super(self.__class__, self).setUp()
        self.load_dae(__file__, 'source_data_relative_to_dae.mb')

    def test_source_data_relative_to_dae(self):
        source_data = self.get_element_by_tag(self.doc.getroot(), 'collada:source_data')
        self.assertIsNotNone(source_data)
        parts = urlparse(source_data.text)
        self.assertEqual(parts.path, '../../../../../../tools/maya/tests/source_data/relative_to_dae/source_data_relative_to_dae.mb')