# Creamos un clase de Grafo Matriz Adyacencia
class GMA:
    def __init__(self, size):
        # Inicializa una matriz de adyacencia de tamaño size x size con ceros.
        # La matriz indica la presencia (1) o ausencia (0) de aristas entre nodos.
        self.size = size
        self.matriz = [[0] * size for _ in range(size)]

    def agregar_nodo(self):
        # Añade una nueva fila y columna en la matriz de adyacencia
        self.size += 1
        for fila in self.matriz:
            fila.append(0)
        self.matriz.append([0] * self.size)

    def agregar_arista(self, nodo1, nodo2):
        # Añade una arista entre nodo1 y nodo2 si ambos nodos existen en el grafo
        if 0 <= nodo1 < self.size and 0 <= nodo2 < self.size:
            self.matriz[nodo1][nodo2] = 1
            self.matriz[nodo2][nodo1] = 1  # Para grafos no dirigidos

    def eliminar_arista(self, nodo1, nodo2):
        # Elimina la arista entre nodo1 y nodo2 poniendo las entradas correspondientes en la matriz a cero
        if 0 <= nodo1 < self.size and 0 <= nodo2 < self.size:
            self.matriz[nodo1][nodo2] = 0
            self.matriz[nodo2][nodo1] = 0  # Para grafos no dirigidos

    def es_adyacente(self, nodo1, nodo2):
        # Verifica si hay una arista entre nodo1 y nodo2
        if 0 <= nodo1 < self.size and 0 <= nodo2 < self.size:
            return self.matriz[nodo1][nodo2] == 1
        return False

    def mostrar_matriz(self):
        # Muestra la matriz de adyacencia
        for fila in self.matriz:
            print(fila)

# Ejemplo de uso
grafo = GMA(3)
grafo.agregar_arista(0, 1)
grafo.agregar_arista(0, 2)
print("Matriz de adyacencia:")
grafo.mostrar_matriz()
print("¿A es adyacente a B?", grafo.es_adyacente(0, 1))
print("¿A es adyacente a C?", grafo.es_adyacente(0, 2))
grafo.eliminar_arista(0, 1)
print("Matriz de adyacencia después de eliminar la arista entre A y B:")
grafo.mostrar_matriz()
