import time

class Nodo:
    def __init__(self, nombre, tiempo_llegada):
        self.nombre = nombre
        self.tiempo_llegada = tiempo_llegada
        self.anterior = None
        self.siguiente = None

class ColaDobleEnlazada:
    def __init__(self):
        self.frente = None
        self.finalCola = None

    def esta_vacia(self):
        return self.frente is None

    def encolar(self, nombre, tiempo_llegada):
        nuevo_nodo = Nodo(nombre, tiempo_llegada)
        if self.esta_vacia():
            self.frente = nuevo_nodo
            self.finalCola = nuevo_nodo
        else:
            self.finalCola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.finalCola
            self.finalCola = nuevo_nodo

    def desencolar(self):
        if self.esta_vacia():
            print("La cola está vacía")
            return None
        else:
            temp = self.frente
            self.frente = self.frente.siguiente
            if self.frente is not None:
                self.frente.anterior = None
            else:
                self.finalCola = None
            return temp

    def mostrar_cola(self):
        if self.esta_vacia():
            print("La cola está vacía")
        else:
            actual = self.frente
            while actual is not None:
                print(f"Nombre: {actual.nombre}, Tiempo de Llegada: {actual.tiempo_llegada}")
                actual = actual.siguiente

def main():
    cola = ColaDobleEnlazada()
    
    # Agregar clientes a la cola
    print("Encolando clientes...")
    start_enqueue = time.time()
    cola.encolar("angel", 1)
    cola.encolar("Pablo", 2)
    cola.encolar("Sarango", 3)
    end_enqueue = time.time()
    enqueue_time = end_enqueue - start_enqueue
    print(f"Tiempo de encolado: {enqueue_time:.6f} segundos")
    
    # Mostrar la cola
    print("Estado de la cola:")
    cola.mostrar_cola()
    
    # Atender a los clientes
    print("\nAtendiendo a los clientes...")
    start_dequeue = time.time()
    while not cola.esta_vacia():
        atendido = cola.desencolar()
        if atendido:
            print(f"Atendiendo a: {atendido.nombre}, Llegó a: {atendido.tiempo_llegada}")
    end_dequeue = time.time()
    dequeue_time = end_dequeue - start_dequeue
    print(f"Tiempo de desencolado: {dequeue_time:.6f} segundos")

if __name__ == "__main__":
    main()