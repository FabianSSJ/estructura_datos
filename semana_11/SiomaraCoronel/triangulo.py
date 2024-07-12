# Importamos la biblioteca matplotlib para crear gráficos.
import matplotlib.pyplot as plt

def draw_triangle(vertices):
    # Crea un objeto de tipo Polígono utilizando los vértices proporcionados.
    # El triángulo tendrá bordes de color púrpura y no estará relleno.
    triangle = plt.Polygon(vertices, edgecolor='purple', fill=None)
    # Añade el triángulo a la gráfica actual.
    plt.gca().add_patch(triangle)

def sierpinski(vertices, depth):
    # Dibuja el Triángulo de Sierpinski con la profundidad dada.
    if depth == 0:
        # Si la profundidad es 0, dibuja el triángulo actual.
        draw_triangle(vertices)
    else:
        # Calcula los puntos medios de cada lado del triángulo.
        # Punto medio entre el primer y segundo vértice.
        mid1 = [(vertices[0][0] + vertices[1][0]) / 2, (vertices[0][1] + vertices[1][1]) / 2]
        # Punto medio entre el segundo y tercer vértice.
        mid2 = [(vertices[1][0] + vertices[2][0]) / 2, (vertices[1][1] + vertices[2][1]) / 2]
        # Punto medio entre el tercer y primer vértice.
        mid3 = [(vertices[2][0] + vertices[0][0]) / 2, (vertices[2][1] + vertices[0][1]) / 2]
        

        # Llama recursivamente para cada triángulo más pequeño
        sierpinski([vertices[0], mid1, mid3], depth - 1)
        sierpinski([vertices[1], mid1, mid2], depth - 1)
        sierpinski([vertices[2], mid2, mid3], depth - 1)

def main():
    # Crea una nueva figura para la gráfica.
    plt.figure()
    # Ajusta la relación de aspecto para que los ejes X e Y tengan la misma escala.
    plt.gca().set_aspect('equal')
    # Oculta los ejes de la gráfica.
    plt.axis('off')

    # Define los vértices iniciales del triángulo
    vertices = [[0, 0], [1, 0], [0.5, 0.866]]
    
    # Profundidad de la recursión
    depth = 4  # Cambia este valor para probar diferentes niveles de profundidad
    
    # Llama a la función para dibujar el Triángulo de Sierpinski con los vértices y la profundidad especificados.
    sierpinski(vertices, depth)
    
    # Establece los límites del eje X.
    plt.xlim(-0.1, 1.1)
    # Establece los límites del eje Y.
    plt.ylim(-0.1, 1.1)
    
    # Muestra la gráfica
    plt.show()

if __name__ == "__main__":
    main()
