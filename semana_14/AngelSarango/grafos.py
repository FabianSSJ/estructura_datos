class Grafo:
    def __init__(self):
        self.adyacencia = {}

    def agregar_vertice(self, vertice):
        self.adyacencia[vertice] = []

    def agregar_arista(self, v1, v2):
        self.adyacencia[v1].append(v2)
        self.adyacencia[v2].append(v1)

    def buscar_adyacencia(self, v1, v2):
        return v2 in self.adyacencia[v1]
    
class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.matriz = [[0 for x in range(vertices)] for y in range(vertices)]

    def agregar_arista(self, v1, v2):
        self.matriz[v1][v2] = 1
        self.matriz[v2][v1] = 1

    def buscar_adyacencia(self, v1, v2):
        return self.matriz[v1][v2] == 1