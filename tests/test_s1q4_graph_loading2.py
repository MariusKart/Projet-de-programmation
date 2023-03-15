# À compléter
import sys 
sys.path.append("delivery_network")

from graph import Graph, graph_from_file

import unittest   # The test framework

class Test_distance(unittest.TestCase):
    def test_network4(self):
        g1 = graph_from_file("input/network.04.in")
        edges=[(2 ,3, 4, 3),(3, 4, 4, 2),(1, 4, 11, 6),(2, 1, 4, 89)]
        g2= Graph(range(1, 11))
        for edge in edges:
            g2.add_edge(edge[0], edge[1], edge[2], edge[3])
if __name__ == '__main__':
    unittest.main()
