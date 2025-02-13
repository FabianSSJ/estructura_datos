class Nodo:
    def _init_(self, nombre, numero):
        self.nombre = nombre
        self.numero = numero
        self.izquierda = None
        self.derecha = None

class BST:
    def _init_(self):
        self.raiz = None
    
    # Método para insertar un nuevo contacto en el BST
    def insertar(self, nombre, numero):
        if self.raiz is None:
            self.raiz = Nodo(nombre, numero)
        else:
            self._insertar_recursivo(self.raiz, nombre, numero)
    
    def _insertar_recursivo(self, nodo, nombre, numero):
        if nombre < nodo.nombre:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(nombre, numero)
            else:
                self._insertar_recursivo(nodo.izquierda, nombre, numero)
        elif nombre > nodo.nombre:
            if nodo.derecha is None:
                nodo.derecha = Nodo(nombre, numero)
            else:
                self._insertar_recursivo(nodo.derecha, nombre, numero)
        else:
            print("El contacto ya existe.")

    # Método para buscar un contacto por nombre
    def buscar(self, nombre):
        return self._buscar_recursivo(self.raiz, nombre)
    
    def _buscar_recursivo(self, nodo, nombre):
        if nodo is None:
            return None
        if nombre == nodo.nombre:
            return nodo
        elif nombre < nodo.nombre:
            return self._buscar_recursivo(nodo.izquierda, nombre)
        else:
            return self._buscar_recursivo(nodo.derecha, nombre)

    # Método para eliminar un contacto
    def eliminar(self, nombre):
        self.raiz = self._eliminar_recursivo(self.raiz, nombre)
    
    def _eliminar_recursivo(self, nodo, nombre):
        if nodo is None:
            return nodo
        
        if nombre < nodo.nombre:
            nodo.izquierda = self._eliminar_recursivo(nodo.izquierda, nombre)
        elif nombre > nodo.nombre:
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, nombre)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            temp = self._minimo(nodo.derecha)
            nodo.nombre = temp.nombre
            nodo.numero = temp.numero
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, temp.nombre)
        return nodo
    
    def _minimo(self, nodo):
        current = nodo
        while current.izquierda is not None:
            current = current.izquierda
        return current

    # Método para imprimir los contactos en orden
    def imprimir(self):
        self._imprimir_recursivo(self.raiz)
    
    def _imprimir_recursivo(self, nodo):
        if nodo:
            self._imprimir_recursivo(nodo.izquierda)
            print(f"Nombre: {nodo.nombre}, Número: {nodo.numero}")
            self._imprimir_recursivo(nodo.derecha)

# Ejemplo de uso de la clase BST
if __name__ == "_main_":
    agenda = BST()
    agenda.insertar("Carlos", "123456789")
    agenda.insertar("Ana", "987654321")
    agenda.insertar("Luis", "456789123")

    print("Agenda de contactos:")
    agenda.imprimir()

    contacto = agenda.buscar("Ana")
    if contacto:
        print(f"\nContacto encontrado: Nombre: {contacto.nombre}, Número: {contacto.numero}")
    else:
        print("\nContacto no encontrado.")

    print("\nEliminando contacto de Ana...")
    agenda.eliminar("Ana")
    
    print("\nAgenda de contactos después de eliminar a Ana:")
    agenda.imprimir()