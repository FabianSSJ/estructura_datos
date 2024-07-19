# Ejercicio del TRIANGULO DE SIERPINSKI

import turtle

def dibujar_triangulo(tortuga, vertices):
    # Dibujamos un triángulo dado sus vértices
    tortuga.penup()
    tortuga.goto(vertices[0])
    tortuga.pendown()
    tortuga.goto(vertices[1])
    tortuga.goto(vertices[2])
    tortuga.goto(vertices[0])

def sierpinski(tortuga, profundidad, vertices):
    if profundidad == 0:
        dibujar_triangulo(tortuga, vertices)
    else:
        # Calculamos los puntos medios de los lados del triángulo
        medio01 = ((vertices[0][0] + vertices[1][0]) / 2, (vertices[0][1] + vertices[1][1]) / 2)
        medio12 = ((vertices[1][0] + vertices[2][0]) / 2, (vertices[1][1] + vertices[2][1]) / 2)
        medio20 = ((vertices[2][0] + vertices[0][0]) / 2, (vertices[2][1] + vertices[0][1]) / 2)
        # Llamada recursiva para los tres triángulos más pequeños
        sierpinski(tortuga, profundidad-1, [vertices[0], medio01, medio20])
        sierpinski(tortuga, profundidad-1, [medio01, vertices[1], medio12])
        sierpinski(tortuga, profundidad-1, [medio20, medio12, vertices[2]])

# Aqui es para configurar la ventana de Turtle
ventana = turtle.Screen()
ventana.setup(width=600, height=600)
ventana.bgcolor("white")

# Creamos un objeto Turtle
tortuga = turtle.Turtle()
tortuga.speed(-1)  # Velocidad máxima de dibujo

# Definimos los vértices del triángulo inicial
vertices_iniciales = [(-200, -150), (0, 200), (200, -150)]

# Aqui dibujamos el Triángulo de Sierpinski de acuerdo al nivel de profundidad
# Entre mayor porfundidad, mas triangulos, y viceversa
nivel_profundidad = 2 # Aqui podemos variar la profundidad
sierpinski(tortuga, nivel_profundidad, vertices_iniciales)

# Ocultar el cursor de Turtle y mostrar el resultado
tortuga.hideturtle()
ventana.mainloop()
