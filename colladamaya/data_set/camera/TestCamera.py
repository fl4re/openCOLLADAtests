from unittest import TestCase


class CameraTest(TestCase):
    def test_montest(self):
        #ListResult = []

        ListName = ['yfov', 'aspect_ratio', 'znear', 'zfar', 'horizontal_aperture', 'vertical_aperture', 'focal_length',
                    'lens_squeeze', 'film_fit', 'film_fit_offset', 'film_offsetX', 'film_offsetY']
        #ListValue = ['28.8416', '0.6666667', '0.1', '10000', '2.4', '3.6', '70', '1', '0', '0', '0', '0']

        self.assertEquals(ListName[0], 'yfov')
