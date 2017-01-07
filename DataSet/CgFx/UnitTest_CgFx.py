###################################################################################
# from FTest_Camera import *
# myTestCamera = FTest_Camera()

from Core.Common.DOMParser import *
from Core.FColladaTest import FColladaTest
from numpy import *


###################################################################################


def resource_a_setup():
    print('resources_a_setup()')


def resource_a_teardown():
    print('resources_a_teardown()')

class Test_CgFx:
    @classmethod
    def setup_class(cls):
        # print ('\nsetup_class()')
        resource_a_setup()

    @classmethod
    def teardown_class(cls):
        # print ('\nteardown_class()')
        resource_a_teardown()

    def test_cgfx_1(self):
        #
        tagNodeLst = ['library_effects', 'effect']
        xmlNodesList = FColladaTest.GetElementsByTags(FColladaTest.GetRoot(), tagNodeLst)

        xmlNode = xmlNodesList[5]
        assert (GetAttriByEle(xmlNode, 'id') == 'mat_test-fx')

        tagNodeLst = ['profile_CG' , 'include']
        include = FColladaTest.GetElementsByTags(xmlNode, tagNodeLst)
        assert (GetAttriByEle(include[0], 'url') == './CgFx/valhallaPhysBasedCrossBlend.cgfx')

        print('\nTest_CgFx:test_cgfx_1()')
