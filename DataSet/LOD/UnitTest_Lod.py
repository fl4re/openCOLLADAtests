
###################################################################################
# from FTest_Camera import *
# myTestCamera = FTest_Camera()

from FColladaTest import *
from numpy import *
from xml.dom.minidom import parse, parseString

###################################################################################


def resource_a_setup():
	print('resources_a_setup()')
 
def resource_a_teardown():
	print('resources_a_teardown()')

def checkMatrixValue(matrix, ListValue):

	resParse2 = ParseEleAsFloat(matrix)
		
	i = 0
	for element in resParse2[1]:
		assert(isclose(float(element), float(ListValue[i]), atol=1e-04, rtol=0))
		i += 1
	
	
	
	
class Test_Lod:
 
	@classmethod
	def setup_class(cls):
		# print ('\nsetup_class()')
		resource_a_setup()
 
	@classmethod
	def teardown_class(cls):
		# print ('\nteardown_class()')
		resource_a_teardown()
		
	def test_lod_1(self):
		
		########
		tagNodeLst = ['library_nodes', 'node']
		xmlNodesList = FColladaTest.GetElementsByTags(FColladaTest.GetRoot(), tagNodeLst)
		assert(len(xmlNodesList) == 4)
		
		######## NODE 0
		xmlNode = xmlNodesList[0]
		assert(GetAttriByEle(xmlNode, 'id') == '_lodGroup1_pCylinder1_LOD2')
		matrix = xmlNode.childNodes[1]
		ListValue = [1, 0, 0, 6.664345, 0, 1, 0, 2.236402, 0, 0, 1, 2.918081, 0, 0, 0, 1]
		checkMatrixValue(matrix, ListValue)
		
		tagNodeLst = ['instance_geometry']
		instance_geometry = FColladaTest.GetElementsByTags(xmlNode, tagNodeLst)
		assert(GetAttriByEle(instance_geometry[0], 'url') == '#pCylinder1_LODShape2')
		
		
		######## NODE 1
		xmlNode = xmlNodesList[1]
		assert(GetAttriByEle(xmlNode, 'id') == '_lodGroup1_pCube1_LOD1')
		matrix = xmlNode.childNodes[1]
		ListValue = [1, 0, 0, -0.7439139, 0, 1, 0, 1.945068, 0, 0, 1, 3.083594, 0, 0, 0, 1]
		checkMatrixValue(matrix, ListValue)
		
		tagNodeLst = ['instance_geometry']
		instance_geometry = FColladaTest.GetElementsByTags(xmlNode, tagNodeLst)
		assert(GetAttriByEle(instance_geometry[0], 'url') == '#pCube1_LODShape1')
		
		######## NODE 2
		xmlNode = xmlNodesList[2]
		assert(GetAttriByEle(xmlNode, 'id') == '_lodGroup1_pSphere1_LOD0')
		matrix = xmlNode.childNodes[1]
		ListValue = [1, 0, 0, -12.10772, 0, 1, 0, 0, 0, 0, 1, 0.8363657, 0, 0, 0, 1]
		checkMatrixValue(matrix, ListValue)
		
		tagNodeLst = ['instance_geometry']
		instance_geometry = FColladaTest.GetElementsByTags(xmlNode, tagNodeLst)
		assert(GetAttriByEle(instance_geometry[0], 'url') == '#pSphere1_LODShape0')
		
		
		######## LOD NODE 0
		xmlNode = xmlNodesList[3]
		assert(GetAttriByEle(xmlNode, 'id') == 'LOD___lodGroup1_pCube1_LOD1')
		
		instance_node = xmlNode.childNodes[1]
		assert(GetAttriByEle(instance_node, 'url') == '#_lodGroup1_pCube1_LOD1')

		tagInputLst = ['proxy']  
		proxy = GetElementsByTags( instance_node, tagInputLst)
		assert(GetAttriByEle(proxy[0], 'url') == '#_lodGroup1_pSphere1_LOD0')
		
		threshold = proxy[0].childNodes[1]
		assert(isclose(float(threshold.childNodes[0].nodeValue), float('52.52614'),atol=1e-04, rtol=0)) 
		
		
		# ######## LOD NODE 1
		# xmlNode = xmlNodesList[4]
		# assert(GetAttriByEle(xmlNode, 'id') == 'LOD___lodGroup1_pSphere1_LOD0')
		# instance_node = xmlNode.childNodes[1]
		# assert(GetAttriByEle(instance_node, 'url') == '#_lodGroup1_pSphere1_LOD0')
		
		

		######## 
		tagNodeLst = ['library_visual_scenes', 'visual_scene', 'instance_node']
		xmlNode = FColladaTest.GetElementsByTags(FColladaTest.GetRoot(), tagNodeLst)
		instance_node = xmlNode[0]
		assert(GetAttriByEle(instance_node, 'url') == '#_lodGroup1_pCylinder1_LOD2')
		
		tagInputLst = ['proxy']  
		proxy = GetElementsByTags( instance_node, tagInputLst)
		assert(GetAttriByEle(proxy[0], 'url') == '#LOD___lodGroup1_pCube1_LOD1')
		
		threshold = proxy[0].childNodes[1]
		assert(isclose(float(threshold.childNodes[0].nodeValue), float('13.13153'),atol=1e-04, rtol=0)) 
		
			
		print('\nTest_Lod:test_lod_1()')