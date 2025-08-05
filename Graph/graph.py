class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.edge=0
        self.adj_list=[list() for i in range(self.vertices) ]


    def get_number_of_vertices(self):
        return self.vertices

    def get_adj_list(self, vertex):
        return self.adj_list[vertex]

    def get_number_of_edges(self):
        return self.edge


    def add_edge(self,vertex1,vertex2):
        self.adj_list[vertex1].append(vertex2)
        self.adj_list[vertex2].append(vertex1)
