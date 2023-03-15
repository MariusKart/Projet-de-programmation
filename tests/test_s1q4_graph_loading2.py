# À compléter
import sys 
sys.path.append("delivery_network")

from graph import Graph, graph_from_file, add_edge

import unittest   # The test framework

class Test_distance(unittest.TestCase):
    def test_network4(self):
        g1 = graph_from_file("input/network.04.in")
        g2=Graph()
        edges=[(2 ,3, 4, 3),(3, 4, 4, 2),(1, 4, 11, 6),(2, 1, 4, 89)]
        for edge in edge:
            g2.addedge(edge[0], edge[1], edge[2], edge[3])
        self.assertEqual(g1, g2)
if __name__ == '__main__':
    unittest.main()
