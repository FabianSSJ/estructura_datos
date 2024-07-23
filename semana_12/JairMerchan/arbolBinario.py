class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self, raiz=None):
        self.raiz = raiz

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(valor, self.raiz)

    def _insertar_recursivo(self, valor, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.izquierdo)
        else:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.derecho)

    def recorrido_inorden(self, nodo):
        if nodo is not None:
            self.recorrido_inorden(nodo.izquierdo)
            print(nodo.valor, end=' ')
            self.recorrido_inorden(nodo.derecho)

    def recorrido_preorden(self, nodo):
        if nodo is not None:
            print(nodo.valor, end=' ')
            self.recorrido_preorden(nodo.izquierdo)
            self.recorrido_preorden(nodo.derecho)

    def recorrido_postorden(self, nodo):
        if nodo is not None:
            self.recorrido_postorden(nodo.izquierdo)
            self.recorrido_postorden(nodo.derecho)
            print(nodo.valor, end=' ')

    def evaluar_arbol(self, nodo):
        if nodo is None:
            return 0
        if nodo.izquierdo is None and nodo.derecho is None:
            return int(nodo.valor)
        izquierdo_valor = self.evaluar_arbol(nodo.izquierdo)
        derecho_valor = self.evaluar_arbol(nodo.derecho)
        if nodo.valor == '+':
            return izquierdo_valor + derecho_valor
        if nodo.valor == '-':
            return izquierdo_valor - derecho_valor
        if nodo.valor == '*':
            return izquierdo_valor * derecho_valor
        if nodo.valor == '/':
            return izquierdo_valor / derecho_valor
            
# Construcción del árbol para la expresión (3 + 5) * 2
raiz = Nodo('*')
raiz.izquierdo = Nodo('+')
raiz.izquierdo.izquierdo = Nodo('7')
raiz.izquierdo.derecho = Nodo('9')
raiz.derecho = Nodo('4')

# Creación del árbol binario
arbol = ArbolBinario(raiz)

# Realización de los recorridos
print("Recorrido Inorden:")
arbol.recorrido_inorden(arbol.raiz)
print("\nRecorrido Preorden:")
arbol.recorrido_preorden(arbol.raiz)
print("\nRecorrido Postorden:")
arbol.recorrido_postorden(arbol.raiz)

# Evaluación del árbol
resultado = arbol.evaluar_arbol(arbol.raiz)
print(f"\nEl resultado de la expresión es: {resultado}")
