import common.test_case_base


class LODTestSuite(common.test_case_base.TestCaseBase):
    def setUp(self):
        super(self.__class__, self).setUp()
        self.doc = self.load_dae(__file__, 'GroupLOD.mb')

    def test_lod(self):
        #
        nodes = self.get_elements_by_tag(self.doc.getroot(), 'collada:library_nodes/collada:node')
        self.assertEqual(len(nodes), 4)

        # Node 0
        node = nodes[0]
        self.assertEquals(node.attrib['id'], '_lodGroup1_pCylinder1_LOD2')
        self.assertEqual(node[0].text, "1 0 0 6.664345 0 1 0 2.236402 0 0 1 2.918081 0 0 0 1")
        instance_geometry = self.get_element_by_tag(node, 'collada:instance_geometry')
        self.assertEqual(instance_geometry.attrib['url'], '#pCylinder1_LODShape2')

        # Node 1
        node = nodes[1]
        self.assertEquals(node.attrib['id'], '_lodGroup1_pCube1_LOD1')
        self.assertEqual(node[0].text, "1 0 0 -0.7439139 0 1 0 1.945068 0 0 1 3.083594 0 0 0 1")
        instance_geometry = self.get_element_by_tag(node, 'collada:instance_geometry')
        self.assertEqual(instance_geometry.attrib['url'], '#pCube1_LODShape1')

        # Node 2
        node = nodes[2]
        self.assertEquals(node.attrib['id'], '_lodGroup1_pSphere1_LOD0')
        self.assertEqual(node[0].text, "1 0 0 -12.10772 0 1 0 0 0 0 1 0.8363657 0 0 0 1")
        instance_geometry = self.get_element_by_tag(node, 'collada:instance_geometry')
        self.assertEqual(instance_geometry.attrib['url'], '#pSphere1_LODShape0')

        # LOD node 0
        node = nodes[3]
        self.assertEquals(node.attrib['id'], 'LOD___lodGroup1_pCube1_LOD1')
        instance_node = node[0]
        self.assertEqual(instance_node.attrib['url'], '#_lodGroup1_pCube1_LOD1')
        proxy = self.get_element_by_tag(instance_node, 'collada:proxy')
        self.assertEqual(proxy.attrib['url'], '#_lodGroup1_pSphere1_LOD0')
        threshold = proxy[0].text
        self.assertEqual(threshold, "52.52614")

        # LOD node 1
        node = self.get_elements_by_tag(self.doc.getroot(), 'collada:library_visual_scenes/'
                                                            'collada:visual_scene/'
                                                            'collada:node/'
                                                            'collada:instance_node')
        instance_node = node[0]
        self.assertEqual(instance_node.attrib['url'], '#_lodGroup1_pCylinder1_LOD2')
        proxy = self.get_element_by_tag(instance_node, 'collada:proxy')
        self.assertEqual(proxy.attrib['url'], '#LOD___lodGroup1_pCube1_LOD1')
        threshold = proxy[0].text
        self.assertEqual(threshold, "13.13153")
