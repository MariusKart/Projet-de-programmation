# Question 7
from graph import Graph, graph_from_file
from graphviz import Digraph
"""The png of graph should be in '/home/onyxia/work/Graph.png' if you run this code"""
def draw(graph_file):
    """ It should draw a graph 

    Parameters:
    graph_file (str): data path to any graph (networ.xx.in )
    """
    g = graph_from_file(graph_file)
    g.kruskal()
    graph = Digraph()
    for node in g.nodes:
        graph.node(str(node))
    for node in g.nodes:
        for neighbor in g.graph[node]:
            if neighbor[0] > node:  #we don't need a directed graph
                if neighbor[1] != 0 : #we don't connect the unconnected nodes
                    graph.edge(str(node), str(neighbor[0]), label=str(neighbor[1]), dir='none')
    graph.render('graph', format='png', view=True)

draw("/home/onyxia/work/Projet-de-programmation-RAVELOMANANA-MORO/input/network.01.in") 

