import common.test_case_base


class Test_CgFx(common.test_case_base.TestCaseBase):
    def setUp(self):
        super(self.__class__, self).setUp()
        self.load_dae(__file__, 'CgFx.ma')

    def test_cgfx_1(self):
        nodes = self.get_elements_by_tag(self.doc.getroot(), 'collada:library_effects/collada:effect')

        node = nodes[5]
        self.assertEqual(node.attrib['id'], 'mat_test-fx')

        include = self.get_element_by_tag(node, 'collada:profile_CG/collada:include')
        self.assertEqual(include.attrib['url'], './CgFx/valhallaPhysBasedCrossBlend.cgfx')
