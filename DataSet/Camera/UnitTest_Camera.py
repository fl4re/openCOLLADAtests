
###################################################################################
# from FTest_Camera import *
# myTestCamera = FTest_Camera()

from FColladaTest import *

###################################################################################


def resource_a_setup():
    print('resources_a_setup()')
 
def resource_a_teardown():
    print('resources_a_teardown()')

	
class Test_Camera:
 
    @classmethod 
    def setup_class(cls):
        # print ('\nsetup_class()')
        resource_a_setup()
 
    @classmethod 
    def teardown_class(cls):
        # print ('\nteardown_class()')
        resource_a_teardown()
		
		
		
    def test_camera_1(self):

		ListResult = []
		
		ListName = ['yfov', 'aspect_ratio', 'znear', 'zfar', 'horizontal_aperture', 'vertical_aperture', 'focal_length', 'lens_squeeze', 'film_fit', 'film_fit_offset', 'film_offsetX', 'film_offsetY']
		ListValue = ['28.8416', '0.6666667', '0.1', '10000', '2.4', '3.6' , '70', '1', '0', '0', '0', '0']
	
		xmlNode = FColladaTest.GetElementByID(FColladaTest.GetRoot(), '_camera1_cameraShape1')
		
		
		if xmlNode != None:
			# tag = xmlNode.nodeName
			id = xmlNode.attributes['name'].value
			# ListResult.append(id)
			
		for eachInput in ListName:
			if len(FColladaTest.GetElementsByTags(FColladaTest.GetRoot(), [eachInput])) > 0:
				ListResult.append(FColladaTest.GetElementsByTags(FColladaTest.GetRoot(), [eachInput])[0].childNodes[0].nodeValue)
	
	
		# [ListName, ListValue, ListResult] = myTestCamera.testCameraElement();
		
		i = 0
		for element in ListResult:
			assert ListResult[i] == ListValue[i], ListName[i]
			i = i + 1
			
		print('\nTest_Camera:test_camera_1()')