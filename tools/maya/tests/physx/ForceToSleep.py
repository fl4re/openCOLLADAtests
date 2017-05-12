from common.test_case_base import TestCaseBase


class ForceToSleepEnabledTestSuite(TestCaseBase):
    def setUp(self):
        super(self.__class__, self).setUp()
        self.dae = self.load_dae(__file__, 'ForceToSleep.ma')

    def test_force_to_sleep(self):
        physics_model = self.dae.getroot().find(".//collada:physics_model", TestCaseBase.namespaces)
        sphere = physics_model.find(".//collada:rigid_body[@sid='pSphere4RigidBody1']", TestCaseBase.namespaces)
        cube = physics_model.find(".//collada:rigid_body[@sid='pCube2RigidBody1']", TestCaseBase.namespaces)
        force_to_sleep_sphere = sphere.find(".//collada:force_to_sleep", TestCaseBase.namespaces)
        force_to_sleep_cube = cube.find(".//collada:force_to_sleep", TestCaseBase.namespaces)
        self.assertIsNotNone(force_to_sleep_sphere)
        self.assertIsNone(force_to_sleep_cube)
        self.assertEquals("1", force_to_sleep_sphere.text)
