import tkinter as tk
from tkinter import ttk
import random

class Nodo:
    def __init__(self, nombre, clave):
        self.nombre = nombre
        self.clave = clave
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, nombre, clave):
        if not self.raiz:
            self.raiz = Nodo(nombre, clave)
        else:
            self._insertar_recursivo(self.raiz, nombre, clave)

    def _insertar_recursivo(self, nodo, nombre, clave):
        if nombre < nodo.nombre:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(nombre, clave)
            else:
                self._insertar_recursivo(nodo.izquierda, nombre, clave)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(nombre, clave)
            else:
                self._insertar_recursivo(nodo.derecha, nombre, clave)

    def buscar(self, nombre):
        return self._buscar_recursivo(self.raiz, nombre)

    def _buscar_recursivo(self, nodo, nombre):
        if nodo is None or nodo.nombre == nombre:
            return nodo
        if nombre < nodo.nombre:
            return self._buscar_recursivo(nodo.izquierda, nombre)
        return self._buscar_recursivo(nodo.derecha, nombre)

    def inorden(self):
        resultado = []
        self._inorden_recursivo(self.raiz, resultado)
        return resultado

    def _inorden_recursivo(self, nodo, resultado):
        if nodo:
            self._inorden_recursivo(nodo.izquierda, resultado)
            resultado.append((nodo.nombre, nodo.clave))
            self._inorden_recursivo(nodo.derecha, resultado)

class Alumno:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("CRUD de Alumnos con Árbol Binario")
        self.arbol = ArbolBinario()
        
        self.configurar_interfaz()
        self.cargar_datos_predeterminados()

    def configurar_interfaz(self):
        # Nombre
        tk.Label(self.ventana, text="Nombre:").grid(row=0, column=0)
        self.nombre_entry = tk.Entry(self.ventana)
        self.nombre_entry.grid(row=0, column=1)

        # Clave
        tk.Label(self.ventana, text="Clave:").grid(row=1, column=0)
        self.clave_entry = tk.Entry(self.ventana)
        self.clave_entry.grid(row=1, column=1)

        # Botones
        tk.Button(self.ventana, text="Agregar", command=self.agregar_alumno).grid(row=2, column=0)
        tk.Button(self.ventana, text="Buscar", command=self.buscar_alumno).grid(row=2, column=1)

        # Tabla
        self.tabla = ttk.Treeview(self.ventana, columns=('nombre', 'clave'), show='headings')
        self.tabla.heading('nombre', text='Nombre')
        self.tabla.heading('clave', text='Clave')
        self.tabla.grid(row=3, column=0, columnspan=2)

        # Mensaje
        self.mensaje = tk.Label(self.ventana, text="", fg="green")
        self.mensaje.grid(row=4, column=0, columnspan=2)

    def cargar_datos_predeterminados(self):
        nombres = ["Juan", "María", "Carlos", "Ana", "Pedro", "Laura", "Diego", "Sofía", "Miguel", "Isabel"]
        for nombre in nombres:
            clave = ''.join(random.choices('0123456789', k=6))
            self.arbol.insertar(nombre, clave)
        self.actualizar_tabla()

    def actualizar_tabla(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        for nombre, clave in self.arbol.inorden():
            self.tabla.insert('', 'end', values=(nombre, clave))

    def agregar_alumno(self):
        nombre = self.nombre_entry.get()
        clave = self.clave_entry.get()
        if nombre and clave:
            self.arbol.insertar(nombre, clave)
            self.actualizar_tabla()
            self.mensaje.config(text="Alumno agregado con éxito")
        else:
            self.mensaje.config(text="Por favor, ingrese nombre y clave")

    def buscar_alumno(self):
        nombre = self.nombre_entry.get()
        if nombre:
            resultado = self.arbol.buscar(nombre)
            if resultado:
                self.mensaje.config(text=f"Encontrado: {resultado.nombre}, Clave: {resultado.clave}")
            else:
                self.mensaje.config(text="Alumno no encontrado")
        else:
            self.mensaje.config(text="Por favor, ingrese un nombre para buscar")

if __name__ == "__main__":
    ventana = tk.Tk()
    aplicacion = Alumno(ventana)
    ventana.mainloop()