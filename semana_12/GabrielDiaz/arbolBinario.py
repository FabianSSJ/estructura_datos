# Implementación de un árbol binario para resolver un problema específico

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None
    
    def agregar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._agregar(valor, self.raiz)
    
    def _agregar(self, valor, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self._agregar(valor, nodo_actual.izquierda)
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self._agregar(valor, nodo_actual.derecha)
    
    def recorrido_inorden(self, nodo, resultado):
        if nodo:
            self.recorrido_inorden(nodo.izquierda, resultado)
            resultado.append(nodo.valor)
            self.recorrido_inorden(nodo.derecha, resultado)
        return resultado
    
    def recorrido_preorden(self, nodo, resultado):
        if nodo:
            resultado.append(nodo.valor)
            self.recorrido_preorden(nodo.izquierda, resultado)
            self.recorrido_preorden(nodo.derecha, resultado)
        return resultado
    
    def recorrido_postorden(self, nodo, resultado):
        if nodo:
            self.recorrido_postorden(nodo.izquierda, resultado)
            self.recorrido_postorden(nodo.derecha, resultado)
            resultado.append(nodo.valor)
        return resultado

class ArbolExpresion(ArbolBinario):
    def infija_a_postfija(self, expresion):
        precedencia = {'+': 1, '-': 1, '*': 2, '/': 2}
        salida = []
        pila = []
        
        tokens = expresion.split()
        for token in tokens:
            if token.isdigit():
                salida.append(token)
            elif token == '(':
                pila.append(token)
            elif token == ')':
                while pila and pila[-1] != '(':
                    salida.append(pila.pop())
                pila.pop()
            else:  # es un operador
                while pila and pila[-1] != '(' and precedencia[token] <= precedencia[pila[-1]]:
                    salida.append(pila.pop())
                pila.append(token)
        
        while pila:
            salida.append(pila.pop())
        
        return ' '.join(salida)
    
    def construir_arbol(self, expresion):
        postfija = self.infija_a_postfija(expresion)
        tokens = postfija.split()
        pila = []
        
        for token in tokens:
            if token.isdigit():
                nodo = Nodo(token)
                pila.append(nodo)
            else:
                nodo = Nodo(token)
                nodo.derecha = pila.pop()
                nodo.izquierda = pila.pop()
                pila.append(nodo)
        
        self.raiz = pila.pop()
    
    def evaluar_arbol(self, nodo):
        if nodo.valor.isdigit():
            return int(nodo.valor)
        
        izquierda = self.evaluar_arbol(nodo.izquierda)
        derecha = self.evaluar_arbol(nodo.derecha)
        
        if nodo.valor == '+':
            return izquierda + derecha
        elif nodo.valor == '-':
            return izquierda - derecha
        elif nodo.valor == '*':
            return izquierda * derecha
        elif nodo.valor == '/':
            return izquierda / derecha

if __name__ == "__main__":
    print("-----------------------------------")
    print("           Árbol Binario           ")
    print("-----------------------------------")
    print("")
    valores = input("Ingrese los valores numéricos para el árbol binario, separados por espacios: ").split()
    valores = [int(valor) for valor in valores]

    arbol = ArbolBinario()
    for valor in valores:
        arbol.agregar(valor)
    
    print("")
    print(" - Recorrido Inorden:", arbol.recorrido_inorden(arbol.raiz, []))
    print(" - Recorrido Preorden:", arbol.recorrido_preorden(arbol.raiz, []))
    print(" - Recorrido Postorden:", arbol.recorrido_postorden(arbol.raiz, []))
    
    # Solicitar la expresión aritmética
    print("")
    expresion = input("Ingrese la expresión aritmética en notación infija (con espacios entre los tokens. Ejm: 2 + 1 o otra forma ( 3 + 5 ) * ( 2 - 1 )): ")

    arbol_exp = ArbolExpresion()
    arbol_exp.construir_arbol(expresion)
    resultado = arbol_exp.evaluar_arbol(arbol_exp.raiz)
    print("")
    print(f" - El resultado de la expresión {expresion} es {resultado}")
    print("")
