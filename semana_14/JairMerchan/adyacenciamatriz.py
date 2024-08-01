class GraphAdjacencyMatrix:
    def __init__(self, size):
        # Inicializa una matriz de adyacencia de tamaño size x size con ceros.
        # La matriz indica la presencia (1) o ausencia (0) de aristas entre nodos.
        self.size = size
        self.matrix = [[0] * size for _ in range(size)]

    def add_edge(self, node1, node2):
        # Marca la presencia de una arista entre node1 y node2 en la matriz.
        # Para grafos no dirigidos, actualiza ambas entradas de la matriz.
        if 0 <= node1 < self.size and 0 <= node2 < self.size:
            self.matrix[node1][node2] = 1
            self.matrix[node2][node1] = 1  # Para grafos no dirigidos

    def remove_edge(self, node1, node2):
        # Elimina la arista entre node1 y node2 poniendo las entradas correspondientes en la matriz a cero.
        if 0 <= node1 < self.size and 0 <= node2 < self.size:
            self.matrix[node1][node2] = 0
            self.matrix[node2][node1] = 0  # Para grafos no dirigidos

    def display(self):
        # Imprime la matriz de adyacencia.
        for row in self.matrix:
            print(row)

    def is_adjacent(self, node1, node2):
        # Verifica si hay una arista entre node1 y node2 en la matriz.
        if 0 <= node1 < self.size and 0 <= node2 < self.size:
            return self.matrix[node1][node2] == 1
        return False

# Ejemplo de uso
size = 3  # Número de nodos
g = GraphAdjacencyMatrix(size)
g.add_edge(0, 1)  # Agrega una arista entre los nodos 0 y 1
g.add_edge(0, 2)  # Agrega una arista entre los nodos 0 y 2
g.display()  # Muestra la matriz de adyacencia
print("Is adjacent (0, 1):", g.is_adjacent(0, 1))  # Verifica si hay una arista entre los nodos 0 y 1
g.remove_edge(0, 1)  # Elimina la arista entre los nodos 0 y 1
g.display()  # Muestra la matriz de adyacencia actualizada
