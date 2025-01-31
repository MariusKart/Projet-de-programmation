# Question 10
from graph import Graph, graph_from_file
from time import perf_counter
data_path = "/home/onyxia/work/Projet-de-programmation-RAVELOMANANA-MORO/input/network.2.in"
g = graph_from_file(data_path)#we create a graph from the data
time = 0 #we set a time counter
with open ("/home/onyxia/work/Projet-de-programmation-RAVELOMANANA-MORO/input/routes.1.in","r") as in_routes_file:
    nb_routes = int(float((in_routes_file.readline())))
    for _ in range(1,11):
        t_start = perf_counter()
        src, dest, _ = list(map(int, in_routes_file.readline().split()))
        g.min_power(src, dest)
        t_stop = perf_counter()
        time += (t_stop-t_start)
print("total time=", time*nb_routes/10) #some of the files have 100,000 routes
# total time= 0.09092981717549264
