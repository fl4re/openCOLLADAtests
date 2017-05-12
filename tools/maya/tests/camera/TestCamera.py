import common.test_case_base


class CameraTestSuite(common.test_case_base.TestCaseBase):
    def setUp(self):
        super(self.__class__, self).setUp()
        self.doc = self.load_dae(__file__, 'Cube.mb')

    def test_camera_values(self):
        tags = ['yfov', 'aspect_ratio', 'znear', 'zfar', 'horizontal_aperture', 'vertical_aperture',
                    'lens_squeeze', 'film_fit', 'film_fit_offset', 'film_offsetX', 'film_offsetY']
        expected_values = ['28.8416', '0.6666667', '0.1', '10000', '2.4', '3.6', '1', '0', '0', '0', '0']
        exported_values = []

        for tag in tags:
            nodes = self.get_elements_by_tag(self.doc.getroot(), 'collada:' + tag)
            self.assertEqual(len(nodes), 1, "can't find " + tag + " element")
            exported_values.append(nodes[0].text)

        for exported, expected, tag in zip(exported_values, expected_values, tags):
            self.assertEqual(exported, expected, "Unexpected value for " + tag)
