class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, v):
        if v not in self.adj_list:
            self.adj_list[v] = []

    def add_edge(self, v1, v2):
        if v1 not in self.adj_list:
            self.add_vertex(v1)
        if v2 not in self.adj_list:
            self.add_vertex(v2)
        self.adj_list[v1].append(v2)

    def print_graph(self):
        for vertex in self.adj_list:
            print(f"{vertex}:{self.adj_list[vertex]}")

# Crear un grafo
g = Graph()

# Añadir vértices
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")

# Añadir aristas
g.add_edge("A", "B")
g.add_edge("B", "C")
g.add_edge("C", "A")

# Imprimir el grafo
g.print_graph()