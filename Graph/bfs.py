from audioop import reverse

from graph import Graph
class BreathFirstSearch:
    def __init__(self,graph:Graph,source:int):
        self.marked = [False for i in range(graph.get_number_of_vertices())]
        self.edgeTo = [None for i in range(graph.get_number_of_vertices())]


        self.source=source
        self.bfs(graph,source)

    def bfs(self, graph:Graph, source:int):
        queue=list()
        self.marked[source]=True
        queue.append(source)
        while len(queue) != 0:
            v1=queue.pop(0)
            for v2 in reversed(graph.get_adj_list(v1)):
                if not self.marked[v2]:
                    self.marked[v2]=True
                    self.edgeTo[v2]=v1
                    queue.append(v2)

    def has_path_to(self,vertex:int)->bool:
        return self.marked[vertex]

    def path_to(self,vertex:int):
        if not self.has_path_to(vertex):
            return None
        else:
            path=list()
            temp=vertex
            while  temp != self.source:
                path.append(temp)
                temp=self.edgeTo[temp]
            else:
                path.append(self.source)
                return path[::-1]






