class Nodo:
    def _init_(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def _init_(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(self.raiz, valor)

    def _insertar(self, nodo_actual, valor):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = Nodo(valor)
            else:
                self._insertar(nodo_actual.izquierdo, valor)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = Nodo(valor)
            else:
                self._insertar(nodo_actual.derecho, valor)

    def inorden(self, nodo_actual):
        if nodo_actual is not None:
            self.inorden(nodo_actual.izquierdo)
            print(nodo_actual.valor, end=' ')
            self.inorden(nodo_actual.derecho)

    def preorden(self, nodo_actual):
        if nodo_actual is not None:
            print(nodo_actual.valor, end=' ')
            self.preorden(nodo_actual.izquierdo)
            self.preorden(nodo_actual.derecho)

    def postorden(self, nodo_actual):
        if nodo_actual is not None:
            self.postorden(nodo_actual.izquierdo)
            self.postorden(nodo_actual.derecho)
            print(nodo_actual.valor, end=' ')

class NodoExpresion:
    def _init_(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def construir_arbol_expresion(expresion):
    pila = []

    for char in expresion:
        if char.isdigit():
            pila.append(NodoExpresion(int(char)))
        else:
            nodo = NodoExpresion(char)
            nodo.derecho = pila.pop()
            nodo.izquierdo = pila.pop()
            pila.append(nodo)

    return pila[0]

def evaluar_arbol(nodo):
    if nodo.izquierdo is None and nodo.derecho is None:
        return nodo.valor

    izquierdo = evaluar_arbol(nodo.izquierdo)
    derecho = evaluar_arbol(nodo.derecho)

    if nodo.valor == '+':
        return izquierdo + derecho
    elif nodo.valor == '-':
        return izquierdo - derecho
    elif nodo.valor == '*':
        return izquierdo * derecho
    elif nodo.valor == '/':
        return izquierdo / derecho



class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(self.raiz, valor)

    def _insertar(self, nodo_actual, valor):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = Nodo(valor)
            else:
                self._insertar(nodo_actual.izquierdo, valor)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = Nodo(valor)
            else:
                self._insertar(nodo_actual.derecho, valor)

    def inorden(self, nodo_actual):
        if nodo_actual is not None:
            self.inorden(nodo_actual.izquierdo)
            print(nodo_actual.valor, end=' ')
            self.inorden(nodo_actual.derecho)

    def preorden(self, nodo_actual):
        if nodo_actual is not None:
            print(nodo_actual.valor, end=' ')
            self.preorden(nodo_actual.izquierdo)
            self.preorden(nodo_actual.derecho)

    def postorden(self, nodo_actual):
        if nodo_actual is not None:
            self.postorden(nodo_actual.izquierdo)
            self.postorden(nodo_actual.derecho)
            print(nodo_actual.valor, end=' ')

class NodoExpresion:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def construir_arbol_expresion(expresion):
    pila = []

    for char in expresion:
        if char.isdigit():
            pila.append(NodoExpresion(int(char)))
        else:
            nodo = NodoExpresion(char)
            nodo.derecho = pila.pop()
            nodo.izquierdo = pila.pop()
            pila.append(nodo)

    return pila[0]

def evaluar_arbol(nodo):
    if nodo.izquierdo is None and nodo.derecho is None:
        return nodo.valor

    izquierdo = evaluar_arbol(nodo.izquierdo)
    derecho = evaluar_arbol(nodo.derecho)

    if nodo.valor == '+':
        return izquierdo + derecho
    elif nodo.valor == '-':
        return izquierdo - derecho
    elif nodo.valor == '*':
        return izquierdo * derecho
    elif nodo.valor == '/':
        return izquierdo / derecho

#realizamos una operacion artmetica
expresion = "44+6*"
raiz = construir_arbol_expresion(expresion)
resultado = evaluar_arbol(raiz)
print(f"Resultado de la expresión '{expresion}' es {resultado}")

# Crear árbol binario y realizar recorridos
arbol = ArbolBinario()
for valor in [9, 2, 10, 7, 1, 5, 8]:
    arbol.insertar(valor)

print("\nRecorrido inorden:")
arbol.inorden(arbol.raiz)

print("\nRecorrido preorden:")
arbol.preorden(arbol.raiz)

print("\nRecorrido postorden:")
arbol.postorden(arbol.raiz)
expresion = "44+6*"
raiz = construir_arbol_expresion(expresion)
resultado = evaluar_arbol(raiz)
print(f"Resultado de la expresión '{expresion}' es {resultado}")

