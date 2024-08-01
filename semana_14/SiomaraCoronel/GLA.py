# Creamos un clase de Grafo Lista Adyacencia
class GLA:
    def __init__(self):
        # Inicializa un grafo vacío usando un diccionario
        self.grafo = {}

    def agregar_nodo(self, nodo):
        # Añade un nuevo nodo al grafo si no existe ya
        if nodo not in self.grafo:
            self.grafo[nodo] = []

    def agregar_arista(self, nodo1, nodo2):
        # Añade una arista entre nodo1 y nodo2 si ambos nodos existen en el grafo
        if nodo1 in self.grafo and nodo2 in self.grafo:
            if nodo2 not in self.grafo[nodo1]:
                self.grafo[nodo1].append(nodo2)
            if nodo1 not in self.grafo[nodo2]:
                self.grafo[nodo2].append(nodo1)

    def es_adyacente(self, nodo1, nodo2):
        # Verifica si hay una arista entre nodo1 y nodo2
        return nodo2 in self.grafo[nodo1]

# Ejemplo de uso
grafo = GLA()
grafo.agregar_nodo("A")
grafo.agregar_nodo("B")
grafo.agregar_arista("A", "B")

print("Grafo:", grafo.grafo)
print("¿A es adyacente a B?", grafo.es_adyacente("A", "B"))
