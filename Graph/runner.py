from graph import Graph
from bfs import BreathFirstSearch
def graph_repr(g1:Graph):
    graph_str=""
    for v in range(g1.get_number_of_vertices()):
        for w in g1.get_adj_list(v):
            graph_str =graph_str+str(v)+"-" +str(w) + "\n"
    return graph_str


g1 = Graph(13)
g1.add_edge(0,5)
g1.add_edge(4,3)
g1.add_edge(0,1)
g1.add_edge(9,12)
g1.add_edge(6,4)
g1.add_edge(5,4)
g1.add_edge(0,2)
g1.add_edge(11,12)
g1.add_edge(9,10)
g1.add_edge(0,6)
g1.add_edge(7,8)

g1.add_edge(9,11)
g1.add_edge(5,3)
# print(graph_repr(g1))
bfs1=BreathFirstSearch(g1,0)
print(bfs1.has_path_to(3))
print(bfs1.path_to(4))
