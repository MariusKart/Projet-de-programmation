
#Question 14 question 15
from graph import Graph, graph_from_file
data_path = "/home/onyxia/work/Projet-de-programmation-RAVELOMANANA-MORO/input/network.1.in"
route = "/home/onyxia/work/Projet-de-programmation-RAVELOMANANA-MORO/input/routes.1.in"
g=graph_from_file(data_path)
g.kruskal() #we use kruskal's algorithm to restrain our search in a tree
#we initialize a dictionnary of parents and depths 
parents = {vertice : (vertice, 0) for vertice in g.nodes} #each element is the parent of key, power to reach that parent
depths = {vertice : 0 for vertice in g.nodes}
#we fill the dictionnaries using a dfs 
visited = []
def dfs(node, graph):
    visited.append(node)
    for neighbor in graph.graph[node]:
        if neighbor[0] not in visited:
            parents[neighbor[0]] = (node, neighbor[1])
            depth = depths[node]
            depths[neighbor[0]] = depth + 1
            dfs(neighbor[0], graph)
    return parents, depths
dfs(1, g)


def reach_depth(node1, node2):
    """If node1 and node2 don't have the same depth, from the node with largest depth, this function will iterate on the parents 
    of that node to reach the same depth as the other node
    Args:
        node1 (int): vertice in a graph
        node2 (int): vertice in a graph

    Returns:
        node (int) : node with the lowest depth between 1 and 2
        current_node (int): after the function reaches the goal depth it will return the current node
        path (list) : list of tuples, path from lowest node to goal node, first element of tuple is an (int) representing a node
        second element of tuple is an (int) representing the necessary power to get from previous node to next node
    """
    path = []
    if depths[node1] == depths[node2]: #if depths are equal, no need to iterate on the parents
        return node1, node2, path
    if depths[node1] < depths[node2]: #since depth node 2 is the lowest, we set depth of node 1 as goal and then iterate on parents of node2 to get there
        goal = depths[node1]
        current_depth = depths[node2]
        current_node = (node2, 0)
        path.append(current_node)  #we add the node each time we iterate making sure to store both path and power (parent is a tuple)
        while current_depth > goal:
            current_depth = current_depth - 1
            current_node = parents[current_node[0]]
            path.append(current_node)
        return node1, current_node[0], path #finally we return highest node, the node we reached to, the path to get there
    elif depths[node2] < depths[node1]:
        goal = depths[node2]
        current_depth = depths[node1]
        current_node = (node1, 0)
        path.append(current_node)
        while current_depth > goal:
            current_depth = current_depth - 1
            current_node = parents[current_node[0]]
            path.append(current_node)
    return node2, current_node[0], path

def optimized_min_power(graph, src, dest):
    """this function should return the minimal power, path from source node to destination node,
     the algorithm is set to be optimal in a tree

    Args:
        graph (Graph): object of Graph class (works only for trees)
        src (int): source node
        dest (int): destination node

    Returns:
        final_path(list): list of integers, path from src to dest
        power (int): minimal power required to go from src to dest
    """
    if src == dest:
        return [src], 0
    #the idea is to iterate over the parents of src and dest until we find a common parent (while storing paths and powers)
    path1 = [] #path from a node to common parent
    path2 = [] 
    #first we use reach_depth function to get to the same depth
    s1 = reach_depth(src, dest)[0]
    s2 = reach_depth(src, dest)[1]
    path = reach_depth(src, dest)[2]
    path1.append((s1, 0))
    path2.append((s2, 0))
    if s1 == s2: #if we already reached the destination, given the lowest node we may have to reverse the path
        if depths[src] < depths[dest]:
            path.reverse()
        final_path = path
    elif s1 != s2: #if we didn't reach dest node 
        s1 = (s1, 0)
        s2 = (s2, 0)
        while s1[0] != s2[0]: #we iterate of the parents of s1 and s2 while storing paths and powers until we get to a common parent
            path1.append(parents[s1[0]])
            path2.append(parents[s2[0]])
            s1 = parents[s1[0]]
            s2 = parents[s2[0]]
    #given the situation, we have to reverse some of our lists
        if depths[src] == depths[dest]:
            path2.reverse()
            path1.append(s1)
            return path1 + path2
        elif depths[src] < depths [dest]:
            path2.reverse()
            path.reverse()
            path1.append(s1)
            final_path = path1 + path2 + path
        elif depths[src] > depths [dest]:
            path1.reverse()
            path2.append(s1)
            final_path = path + path2 + path1
    powers = [power[1] for power in path] #we then get power from our list of tuples
    final_path = [paths[0] for paths in final_path]
    return  final_path, max(powers)

"""Here's a little test for our algorithm using network.1.in and routes.1.in (to try other graphs and routes, the user 
has to change data_path and route variables in the beginnig)
The algorithm below sould print a list of lists, first element is src, second is dest, next we have the path (as a list) 
and the minimal power required
"""
with open (route,"r") as in_routes_file:
    nb_routes = int(float(in_routes_file.readline()))
    path_list = []
    for i in range(nb_routes):
        src, dest, cost = list(map(int, in_routes_file.readline().split()))
        path_list.append([src, dest, optimized_min_power(g, src, dest)])
#print(path_list)

"""Here's another algorithm to store the minimal powers for routes.x.in in a file named routes.x.out"""
def min_power_file(graph_file, route_file):
    """this file should create a file where min powers are stored

    Args:
        graph_file (str)
        route_file (str)
    Returns:
        None
    """
    g = graph_from_file(graph_file) 
    with open (route_file,"r") as in_routes_file:
        nb_routes = int(float(in_routes_file.readline()))
        power_list = []
        for i in range(nb_routes):
            src, dest, cost = list(map(int, in_routes_file.readline().split()))
            power_list.append(optimized_min_power(g, src, dest)[1])
    with open('routes.x.out', 'w') as f:
        for power in power_list:
            f.write(str(power) + '\n')
    f.close()
    return None
min_power_file(data_path, route)
#the file is in /home/onyxia/work/routes.x.out



    



    


