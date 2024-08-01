class GrafoMatrizAdyacencia:
    def __init__(self, n):
        self.n = n
        self.matriz = [[0] * n for _ in range(n)]

    def agregar_arista(self, nodo1, nodo2):
        self.matriz[nodo1][nodo2] = 1
        self.matriz[nodo2][nodo1] = 1

    def es_adyacente(self, nodo1, nodo2):
        return self.matriz[nodo1][nodo2] == 1

# Ejemplo de uso
grafo = GrafoMatrizAdyacencia(3)
grafo.agregar_arista(0, 1)
print(grafo.matriz)
