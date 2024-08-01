class GraphAdjacencyList:
    def __init__(self):
        # Inicializa un grafo vacío usando un diccionario.
        # Las llaves son los nodos, y los valores son listas de nodos adyacentes.
        self.graph = {}

    def add_node(self, node):
        # Agrega un nodo al grafo. Si el nodo ya existe, no hace nada.
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, node1, node2):
        # Agrega una arista entre node1 y node2.
        # En grafos no dirigidos, también agrega node1 a la lista de adyacencia de node2.
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1].append(node2)
            self.graph[node2].append(node1)  # Para grafos no dirigidos

    def remove_edge(self, node1, node2):
        # Elimina la arista entre node1 y node2.
        # Actualiza las listas de adyacencia de ambos nodos.
        if node1 in self.graph and node2 in self.graph:
            if node2 in self.graph[node1]:
                self.graph[node1].remove(node2)
            if node1 in self.graph[node2]:
                self.graph[node2].remove(node1)  # Para grafos no dirigidos

    def display(self):
        # Imprime los nodos y sus listas de adyacencia.
        for node, edges in self.graph.items():
            print(f"{node}: {edges}")

    def find_adjacent(self, node):
        # Devuelve la lista de nodos adyacentes a un nodo específico.
        return self.graph.get(node, [])

# Ejemplo de uso
g = GraphAdjacencyList()
g.add_node("A")
g.add_node("B")
g.add_node("C")
g.add_edge("A", "B")
g.add_edge("A", "C")
g.display()  # Muestra el grafo con nodos y aristas
print("Adjacent to A:", g.find_adjacent("A"))  # Muestra los nodos adyacentes a "A"
g.remove_edge("A", "B")  # Elimina la arista entre "A" y "B"
g.display()  # Muestra el grafo actualizado

