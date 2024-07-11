import random
import time

class Nodo:
    def __init__(self, cliente):
        self.cliente = cliente
        self.siguiente = None
        self.anterior = None

class Cola:
    def __init__(self):
        self.frente = None
        self.final = None

    def esta_vacia(self):
        return self.frente is None

    def encolar(self, cliente):
        nuevo_nodo = Nodo(cliente)
        if self.esta_vacia():
            self.frente = self.final = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.final
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo

    def desencolar(self):
        if self.esta_vacia():
            return None
        cliente = self.frente.cliente
        self.frente = self.frente.siguiente
        if self.frente:
            self.frente.anterior = None
        else:
            self.final = None
        return cliente

class Cliente:
    def __init__(self, nombre, tiempo_llegada):
        self.nombre = nombre
        self.tiempo_llegada = tiempo_llegada

    def __str__(self):
        return f"Cliente: {self.nombre}, Tiempo de llegada: {self.tiempo_llegada}"

def simular_cola_espera():
    cola = Cola()
    tiempo_actual = 0
    
    print("Simulación de cola de espera iniciada")
    
    for i in range(10):  # Simulamos 10 clientes
        tiempo_actual += random.randint(1, 5)  # Tiempo aleatorio entre llegadas
        nombre_cliente = f"Cliente_{i+1}"
        nuevo_cliente = Cliente(nombre_cliente, tiempo_actual)
        cola.encolar(nuevo_cliente)
        print(f"Tiempo {tiempo_actual}: {nuevo_cliente} ha llegado y se ha unido a la cola.")
        
        # Simulamos atención al cliente cada 3 llegadas
        if (i + 1) % 3 == 0:
            time.sleep(1)  # Pausa para mejor visualización
            cliente_atendido = cola.desencolar()
            if cliente_atendido:
                print(f"Tiempo {tiempo_actual}: {cliente_atendido} ha sido atendido.")
    
    print("\nAtendiendo a los clientes restantes:")
    while not cola.esta_vacia():
        time.sleep(1)  # Pausa para mejor visualización
        cliente_atendido = cola.desencolar()
        tiempo_actual += random.randint(1, 3)  # Tiempo aleatorio de atención
        print(f"Tiempo {tiempo_actual}: {cliente_atendido} ha sido atendido.")
    
    print("Simulación finalizada")

if __name__ == "__main__":
    simular_cola_espera()
