# Implementación del Árbol de Recursión
import turtle

def dibujar_rama(tortuga, longitud, profundidad, angulo):
    if profundidad > 0:
        # Dibujar la rama
        tortuga.forward(longitud)
        # Guardar la posición y el ángulo actuales
        posicion = tortuga.position()
        angulo_actual = tortuga.heading()
        
        # aqui dibujamos la rama izquierda
        tortuga.left(angulo)
        dibujar_rama(tortuga, longitud * 0.7, profundidad - 1, angulo)
        
        # Volvemos a la posición y ángulo originales
        tortuga.penup()
        tortuga.goto(posicion)
        tortuga.setheading(angulo_actual)
        tortuga.pendown()
        
        # Dibujamos la rama derecha
        tortuga.right(angulo)
        dibujar_rama(tortuga, longitud * 0.7, profundidad - 1, angulo)
        
        # Volver a la posición y ángulo originales
        tortuga.penup()
        tortuga.goto(posicion)
        tortuga.setheading(angulo_actual)
        tortuga.pendown()

# Configuración de la ventana de Turtle
ventana = turtle.Screen()
ventana.setup(width=800, height=600)
ventana.bgcolor("white")

# Crear un objeto Turtle
tortuga = turtle.Turtle()
tortuga.speed(0)  # Velocidad máxima de dibujo
tortuga.left(90)  # Apuntar hacia arriba

# en esta seccion podemos definir parámetros iniciales

longitud_inicial = 200  # la longitud de la rama inicial
nivel_profundidad = 8   # el nivel de profundidad de la recursión
angulo_bifurcacion = 50 # el angulo de bifurcación en grados

# Colocamos la tortuga en la base del árbol
tortuga.penup()
tortuga.goto(0, -250)
tortuga.pendown()

# Aqui llamamos a la función recursiva para dibujar el árbol
dibujar_rama(tortuga, longitud_inicial, nivel_profundidad, angulo_bifurcacion)

# Ocultamos el cursor de Turtle y mostrar el resultado
tortuga.hideturtle()
ventana.mainloop()
