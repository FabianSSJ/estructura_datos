import matplotlib.pyplot as plt  # Importa la biblioteca de matplotlib para crear gráficos.

# Define la función recursiva para dibujar el Triángulo de Sierpinski.
def sierpinski_triangle(ax, vertices, depth, color='black'):
    if depth == -1:  # Caso base: si la profundidad es 0, dibuja un triángulo.
        triangle = plt.Polygon(vertices, edgecolor=color, facecolor='none')  # Crea un triángulo con los vértices dados.
        ax.add_patch(triangle)  # Añade el triángulo al gráfico.
        plt.draw()  # Dibuja la figura actualizada.
        plt.pause(0.1)  # Pausa breve para actualizar la visualización.
    else:  # Caso recursivo: calcula los puntos medios de los lados del triángulo y llama a la función recursivamente.
        midpoints = [
            ((vertices[0][0] + vertices[1][0]) / 2, (vertices[0][1] + vertices[1][1]) / 2),  # Punto medio entre vértice 0 y 1.
            ((vertices[1][0] + vertices[2][0]) / 2, (vertices[1][1] + vertices[2][1]) / 2),  # Punto medio entre vértice 1 y 2.
            ((vertices[2][0] + vertices[0][0]) / 2, (vertices[2][1] + vertices[0][1]) / 2)   # Punto medio entre vértice 2 y 0.
        ]
        
        # Llamadas recursivas para cada uno de los triángulos más pequeños.
        sierpinski_triangle(ax, [vertices[0], midpoints[0], midpoints[2]], depth - 1, color)  # Triángulo superior.
        sierpinski_triangle(ax, [vertices[1], midpoints[0], midpoints[1]], depth - 1, color)  # Triángulo inferior izquierdo.
        sierpinski_triangle(ax, [vertices[2], midpoints[1], midpoints[2]], depth - 1, color)  # Triángulo inferior derecho.

# Función para configurar y mostrar el gráfico del Triángulo de Sierpinski.
def plot_sierpinski(depth, color='blue'):
    fig, ax = plt.subplots()  # Crea una figura y un eje para el gráfico.
    ax.set_aspect('equal')  # Configura el aspecto del eje para que sea igual.
    ax.axis('off')  # Desactiva los ejes.

    # Define los vértices iniciales del triángulo equilátero.
    vertices = [(0, 0), (1, 0), (0.5, 0.866)]  
    sierpinski_triangle(ax, vertices, depth, color)  # Llama a la función recursiva para dibujar el triángulo.
    
    plt.show()  # Muestra el gráfico.

# Punto de entrada del script.
if __name__ == "__main__":
    depth = 4 # Define la profundidad de la recursión.
    color = 'blue'  # Define el color de los bordes del triángulo.
    plot_sierpinski(depth, color)  # Llama a la función para dibujar y mostrar el Triángulo de Sierpinski.