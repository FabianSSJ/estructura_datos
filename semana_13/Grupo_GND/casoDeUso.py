# Una aplicación para la gestión de inventarios que utilice árboles AVL para mantener el orden de los productos.

class NodoProducto:
    def __init__(self, clave, nombre, cantidad):
        self.clave = clave
        self.nombre = nombre
        self.cantidad = cantidad
        self.izquierda = None
        self.derecha = None
        self.altura = 1

class InventarioAVL:
    def obtener_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def obtener_balance(self, nodo):
        if not nodo:
            return 0
        return self.obtener_altura(nodo.izquierda) - self.obtener_altura(nodo.derecha)

    def rotacion_izquierda(self, z):
        y = z.derecha
        T2 = y.izquierda

        y.izquierda = z
        z.derecha = T2

        z.altura = 1 + max(self.obtener_altura(z.izquierda), self.obtener_altura(z.derecha))
        y.altura = 1 + max(self.obtener_altura(y.izquierda), self.obtener_altura(y.derecha))

        return y

    def rotacion_derecha(self, y):
        x = y.izquierda
        T2 = x.derecha

        x.derecha = y
        y.izquierda = T2

        y.altura = 1 + max(self.obtener_altura(y.izquierda), self.obtener_altura(y.derecha))
        x.altura = 1 + max(self.obtener_altura(x.izquierda), self.obtener_altura(x.derecha))

        return x

    def insertar(self, raiz, clave, nombre, cantidad):
        if not raiz:
            return NodoProducto(clave, nombre, cantidad)
        elif clave < raiz.clave:
            raiz.izquierda = self.insertar(raiz.izquierda, clave, nombre, cantidad)
        else:
            raiz.derecha = self.insertar(raiz.derecha, clave, nombre, cantidad)

        raiz.altura = 1 + max(self.obtener_altura(raiz.izquierda), self.obtener_altura(raiz.derecha))

        balance = self.obtener_balance(raiz)

        if balance > 1 and clave < raiz.izquierda.clave:
            return self.rotacion_derecha(raiz)

        if balance < -1 and clave > raiz.derecha.clave:
            return self.rotacion_izquierda(raiz)

        if balance > 1 and clave > raiz.izquierda.clave:
            raiz.izquierda = self.rotacion_izquierda(raiz.izquierda)
            return self.rotacion_derecha(raiz)

        if balance < -1 and clave < raiz.derecha.clave:
            raiz.derecha = self.rotacion_derecha(raiz.derecha)
            return self.rotacion_izquierda(raiz)

        return raiz

    def preorden(self, raiz):
        if not raiz:
            return
        print("Clave: {0}, Nombre: {1}, Cantidad: {2}".format(raiz.clave, raiz.nombre, raiz.cantidad))
        self.preorden(raiz.izquierda)
        self.preorden(raiz.derecha)

if __name__ == "__main__":
    inventario = InventarioAVL()
    raiz = None

    while True:
        print("-------------------------------")
        print("    Inventario de productos    ")
        print("-------------------------------")
        print("")
        opcion = input("¿Desea ingresar un nuevo producto? (s/n): ")
        if opcion.lower() != 's':
            break

        clave = int(input("Ingrese la clave del producto: "))
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad del producto: "))
        print("")

        raiz = inventario.insertar(raiz, clave, nombre, cantidad)

    print("")
    print("Inventario en preorden:")
    inventario.preorden(raiz)
    print("")
