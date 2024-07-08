import time

class Persona:
    def __init__(self, nombre, cuando_llego):
        self.nombre = nombre
        self.cuando_llego = cuando_llego
        self.amigo_adelante = None
        self.amigo_atras = None

class FilaDeAmigos:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def poner_al_final(self, nombre, cuando_llego):
        nuevo_amigo = Persona(nombre, cuando_llego)
        if not self.ultimo:
            self.primero = self.ultimo = nuevo_amigo
        else:
            self.ultimo.amigo_adelante = nuevo_amigo
            nuevo_amigo.amigo_atras = self.ultimo
            self.ultimo = nuevo_amigo

    def sacar_del_principio(self):
        if not self.primero:
            return None
        amigo = self.primero
        self.primero = amigo.amigo_adelante
        if self.primero:
            self.primero.amigo_atras = None
        else:
            self.ultimo = None
        return amigo

    def esta_vacia(self):
        return self.primero is None

    def mostrar_amigos(self):
        amigo = self.primero
        print("Amigos en la fila:")
        print("Nombre\t\tCuándo llegó")
        print("-" * 30)
        while amigo:
            print(f"{amigo.nombre}\t\t{amigo.cuando_llego:.2f}")
            amigo = amigo.amigo_adelante

def jugar_a_la_fila():
    fila = FilaDeAmigos()
    while True:
        print("\n¿Qué quieres hacer?")
        print("1. Agregar un amigo a la fila")
        print("2. Sacar un amigo de la fila")
        print("3. Ver quiénes están en la fila")
        print("4. Dejar de jugar")
        
        que_hacer = input("Escribe el número de lo que quieres hacer: ")
        
        if que_hacer == "1":
            nombre = input("¿Cómo se llama tu amigo? ")
            fila.poner_al_final(nombre, time.time())
            print(f"¡{nombre} se unió a la fila!")
        elif que_hacer == "2":
            amigo = fila.sacar_del_principio()
            if amigo:
                print(f"¡{amigo.nombre} salió de la fila!")
            else:
                print("¡Oh no! No hay nadie en la fila.")
        elif que_hacer == "3":
            fila.mostrar_amigos()
        elif que_hacer == "4":
            print("¡Gracias por jugar!")
            break
        else:
            print("Ups, no entendí eso. Intenta de nuevo.")

def contar_rapido():
    fila = FilaDeAmigos()
    
    print("Vamos a ver qué tan rápido puedo contar...")
    
    empieza = time.time()
    for i in range(1000):
        fila.poner_al_final(f"Amigo{i}", time.time())
    termina = time.time()
    print(f"¡Puse 1000 amigos en la fila en {termina - empieza:.6f} segundos!")

    empieza = time.time()
    while not fila.esta_vacia():
        fila.sacar_del_principio()
    termina = time.time()
    print(f"¡Saqué a 1000 amigos de la fila en {termina - empieza:.6f} segundos!")

if __name__ == "__main__":
    while True:
        print("\n¿A qué quieres jugar?")
        print("1. Jugar a la fila de amigos")
        print("2. Ver qué tan rápido puedo contar")
        print("3. Ya no quiero jugar")
        
        juego = input("Escribe el número del juego que quieres: ")
        
        if juego == "1":
            jugar_a_la_fila()
        elif juego == "2":
            contar_rapido()
        elif juego == "3":
            print("¡Adiós! Gracias por jugar conmigo.")
            break
        else:
            print("Ups, no entendí eso. Intenta de nuevo.")