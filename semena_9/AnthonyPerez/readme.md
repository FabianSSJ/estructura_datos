# 🎢 ¡Bienvenido a la Fila de Amigos! 🤗

## 📚 Índice
1. [Introducción](#introducción)
2. [Características](#características)
3. [Requisitos](#requisitos)
4. [Instalación](#instalación)
5. [Uso](#uso)
6. [Estructura del Código](#estructura-del-código)
7. [Contribuciones](#contribuciones)
8. [Licencia](#licencia)

## 🌟 Introducción

¡Hola, amigo programador! 👋 Te presentamos "La Fila de Amigos", un proyecto divertido y educativo que simula una cola de personas utilizando una estructura de datos de lista doblemente enlazada. Este proyecto está diseñado para enseñar conceptos de programación de una manera amigable y accesible. 🚀

## ✨ Características

- 🧑‍🤝‍🧑 Simula una fila de personas (¡o amigos!)
- ➕ Agrega nuevos amigos a la fila
- ➖ Saca amigos de la fila
- 👀 Muestra la fila actual
- ⏱️ Mide la eficiencia de las operaciones

## 💻 Requisitos

- Python 3.6 o superior 🐍
- Módulo `time` (incluido en la biblioteca estándar de Python)

## 🛠️ Instalación

1. Clona este repositorio:
   ```
   git clone https://github.com/tu-usuario/fila-de-amigos.git
   ```
2. Navega al directorio del proyecto:
   ```
   cd fila-de-amigos
   ```

## 🎮 Uso

Ejecuta el script principal:

```
python fila_de_amigos.py
```

Sigue las instrucciones en pantalla para:
1. 👥 Jugar con la fila de amigos
2. 🏃‍♂️ Ver qué tan rápido se pueden realizar las operaciones
3. 👋 Salir del programa

## 🏗️ Estructura del Código

El proyecto consta de dos clases principales:

1. `Persona`: Representa a cada amigo en la fila.
   - Atributos: `nombre`, `cuando_llego`, `amigo_adelante`, `amigo_atras`

2. `FilaDeAmigos`: Implementa la cola como una lista doblemente enlazada.
   - Métodos principales:
     - `poner_al_final()`: O(1)
     - `sacar_del_principio()`: O(1)
     - `esta_vacia()`: O(1)
     - `mostrar_amigos()`: O(n)

Funciones adicionales:
- `jugar_a_la_fila()`: Interfaz interactiva para manejar la fila.
- `contar_rapido()`: Mide el rendimiento de las operaciones.

## 🤝 Contribuciones

¡Tus ideas son bienvenidas! Si tienes sugerencias para mejorar este proyecto:

1. 🍴 Haz un fork del repositorio
2. 🔧 Crea una nueva rama (`git checkout -b mi-super-idea`)
3. 💡 Implementa tus cambios
4. 📦 Haz commit de tus cambios (`git commit -am 'Agregué una función genial'`)
5. 🚀 Sube tus cambios (`git push origin mi-super-idea`)
6. 🎉 Crea un nuevo Pull Request

