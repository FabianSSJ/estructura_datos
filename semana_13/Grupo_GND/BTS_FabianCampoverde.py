import time
import random

# Implementación de un Árbol Binario de Búsqueda (BST)
class Nodo:
    def _init_(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class BST:
    def _init_(self):
        self.raiz = None
    
    def insertar(self, clave, valor):
        if self.raiz is None:
            self.raiz = Nodo(clave, valor)
        else:
            self._insertar_recursivo(self.raiz, clave, valor)
    
    def _insertar_recursivo(self, nodo, clave, valor):
        if clave < nodo.clave:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(clave, valor)
            else:
                self._insertar_recursivo(nodo.izquierda, clave, valor)
        elif clave > nodo.clave:
            if nodo.derecha is None:
                nodo.derecha = Nodo(clave, valor)
            else:
                self._insertar_recursivo(nodo.derecha, clave, valor)

    def buscar(self, clave):
        return self._buscar_recursivo(self.raiz, clave)
    
    def _buscar_recursivo(self, nodo, clave):
        if nodo is None:
            return None
        if clave == nodo.clave:
            return nodo
        elif clave < nodo.clave:
            return self._buscar_recursivo(nodo.izquierda, clave)
        else:
            return self._buscar_recursivo(nodo.derecha, clave)

# Implementación de una Tabla Hash con manejo de colisiones por encadenamiento
class TablaHash:
    def _init_(self, tamaño):
        self.tamaño = tamaño
        self.tabla = [[] for _ in range(tamaño)]
    
    def _hash(self, clave):
        return hash(clave) % self.tamaño
    
    def insertar(self, clave, valor):
        indice = self._hash(clave)
        self.tabla[indice].append((clave, valor))

    def buscar(self, clave):
        indice = self._hash(clave)
        for k, v in self.tabla[indice]:
            if k == clave:
                return v
        return None

# Función para medir el tiempo de ejecución
def medir_tiempo(func, *args):
    inicio = time.time()
    resultado = func(*args)
    fin = time.time()
    return fin - inicio, resultado

# Función para probar ambos métodos
def prueba_eficiencia():
    # Generación de datos aleatorios
    datos = [random.randint(1, 1000000) for _ in range(10000)]

    # Prueba con BST
    bst = BST()
    for clave in datos:
        bst.insertar(clave, str(clave))

    # Medir tiempo de búsqueda en BST
    tiempo_bst_busqueda, _ = medir_tiempo(bst.buscar, datos[0])

    # Prueba con Tabla Hash
    tabla_hash = TablaHash(10000)
    for clave in datos:
        tabla_hash.insertar(clave, str(clave))

    # Medir tiempo de búsqueda en Tabla Hash
    tiempo_hash_busqueda, _ = medir_tiempo(tabla_hash.buscar, datos[0])

    print(f"Tiempo de búsqueda en BST: {tiempo_bst_busqueda:.6f} segundos")
    print(f"Tiempo de búsqueda en Tabla Hash: {tiempo_hash_busqueda:.6f} segundos")

# Ejecutar prueba de eficiencia
prueba_eficiencia()