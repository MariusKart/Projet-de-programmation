# This will work if ran from the root folder.
import sys 
sys.path.append("delivery_network")

from graph import Graph, graph_from_file
from time import perf_counter

import unittest   # The test framework

"""class Test_GraphCC(unittest.TestCase):
    def test_network0(self):
        g = graph_from_file("input/network.00.in")
        cc = g.connected_components_set()
        self.assertEqual(cc, {frozenset({1, 2, 3, 4, 5, 6, 7, 8, 9, 10})})

    def test_network1(self):
        g = graph_from_file("input/network.01.in")
        cc = g.connected_components_set()
        self.assertEqual(cc, {frozenset({1, 2, 3}), frozenset({4, 5, 6, 7})})

if __name__ == '__main__':
    unittest.main()"""


trajets=[[6,11],[16,13],[10,3],[2,17],[14,1],[20,15],[10,1],[15,5],[4,15]]
t=[]
g = graph_from_file("input/network.01.in")
for trajet in trajets:
    t_start=perf_counter()
    g.min_power(trajet[0],trajet[1])
    t_stop=perf_counter()
    t.append(t_stop-t_start)
mean_time=sum(t)/len(trajets)
total_time=140*len(trajets)
print(total_time)