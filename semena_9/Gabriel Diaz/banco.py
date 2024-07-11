import time

class Node:
    def __init__(self, name):
        self.name = name
        self.next = None
        self.prev = None

class DoublyLinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, name):
        new_node = Node(name)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            new_node.prev = self.rear
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None
        name = self.front.name
        self.front = self.front.next
        if self.front is not None:
            self.front.prev = None
        else:
            self.rear = None
        return name

    def is_empty(self):
        return self.front is None

class Client:
    def __init__(self, name, arrival_time):
        self.name = name
        self.arrival_time = arrival_time

def queue_simulation():
    queue = DoublyLinkedQueue()

    while True:
        print("---")
        print("1. Encolar cliente")
        print("2. Desencolar cliente")
        print("3. Salir")
        print("---")
        choice = int(input("Ingrese su elección: "))

        if choice == 1:
            name = input("Ingrese el nombre del cliente: ")
            arrival_time = time.time()
            client = Client(name, arrival_time)
            queue.enqueue(client.name)
            print(f"Cliente {name} encolado.")
        elif choice == 2:
            dequeued_name = queue.dequeue()
            if dequeued_name:
                print(f"Cliente {dequeued_name} desencolado.")
            else:
                print("La cola está vacía.")
        elif choice == 3:
            break
        else:
            print("Elección no válida.")

def efficiency_analysis():
    queue = DoublyLinkedQueue()
    start_time, end_time = 0, 0

    # Encolado
    start_time = time.time()
    for i in range(1000):
        queue.enqueue(f"Cliente{i}")
    end_time = time.time()
    print(f"Tiempo para encolar 1000 clientes: {end_time - start_time:.6f} segundos")

    # Desencolado
    start_time = time.time()
    while not queue.is_empty():
        queue.dequeue()
    end_time = time.time()
    print(f"Tiempo para desencolar 1000 clientes: {end_time - start_time:.6f} segundos")

if __name__ == "__main__":
    while True:
        print("------------------------")
        print("     COLA DE ESPERA     ")
        print("------------------------")
        print("Seleccione modo:")
        print("1. Simulación de Cola")
        print("2. Análisis de Eficiencia")
        print("3. Salir")
        print("---")
        mode_choice = int(input("Ingrese su elección: "))

        if mode_choice == 1:
            queue_simulation()
        elif mode_choice == 2:
            efficiency_analysis()
        elif mode_choice == 3:
            break
        else:
            print("Elección no válida.")
