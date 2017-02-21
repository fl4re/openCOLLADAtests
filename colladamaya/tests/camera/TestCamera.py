import common.test_case_base
import unittest


class CameraTestSuite1(common.test_case_base.TestCaseBase):
    def setUp(self):
        super(self.__class__, self).setUp()
        self.load_dae(__file__, 'Cube.mb')

    def test_values(self):
        ListResult = []

        ListName = ['yfov', 'aspect_ratio', 'znear', 'zfar', 'horizontal_aperture', 'vertical_aperture', 'focal_length',
                    'lens_squeeze', 'film_fit', 'film_fit_offset', 'film_offsetX', 'film_offsetY']
        ListValue = ['28.8416', '0.6666667', '0.1', '10000', '2.4', '3.6', '70', '1', '0', '0', '0', '0']

        # xmlNode = FColladaTest.GetElementByID(FColladaTest.GetRoot(), '_camera1_cameraShape1')
        xmlNode = self.get_element_by_id('_testCamera_testCameraShape')

        if xmlNode is not None:
            # tag = xmlNode.nodeName
            id = xmlNode.attrib['name'].value
        # ListResult.append(id)

        for eachInput in ListName:
            if len(FColladaTest.GetElementsByTags(FColladaTest.GetRoot(), [eachInput])) > 0:
                ListResult.append(
                    FColladaTest.GetElementsByTags(FColladaTest.GetRoot(), [eachInput])[0].childNodes[0].nodeValue)

        i = 0
        for element in ListResult:
            assert (isclose(float(ListResult[i]), float(ListValue[i]), atol=1e-04, rtol=0), ListName[i])

            i += 1

        print('\nTest_Camera:test_camera_1()')


class CameraTestSuite2(common.test_case_base.TestCaseBase):
    def test_pass(self):
        #ListResult = []

        ListName = ['yfov', 'aspect_ratio', 'znear', 'zfar', 'horizontal_aperture', 'vertical_aperture', 'focal_length',
                    'lens_squeeze', 'film_fit', 'film_fit_offset', 'film_offsetX', 'film_offsetY']
        #ListValue = ['28.8416', '0.6666667', '0.1', '10000', '2.4', '3.6', '70', '1', '0', '0', '0', '0']

        self.assertEquals(ListName[0], 'yfov')

    def test_fail(self):
        self.assertTrue(False)

    @unittest.skip('Skipped test...')
    def test_skipped_test(self):
        self.assertTrue(False)