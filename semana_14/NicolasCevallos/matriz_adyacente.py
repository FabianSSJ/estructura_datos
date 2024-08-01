class Graph:
    def __init__(self, num_vertices):
        self.adj_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    def add_edge(self, v1, v2):
        self.adj_matrix[v1][v2] = 1

    def remove_edge(self, v1, v2):
        self.adj_matrix[v1][v2] = 0

    def print_graph(self):
        for row in self.adj_matrix:
            print(' '.join(map(str, row)))

# Crear un grafo con 4 vértices
g = Graph(4)

# Añadir algunas aristas
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)

print("Grafo inicial:")
g.print_graph()

# Remover una arista
g.remove_edge(1, 2)

print("\nGrafo después de remover la arista (1,2):")
g.print_graph()