import matplotlib.pyplot as plt
import matplotlib.patches as patches

def sierpinski_triangle(ax, depth, vertices):
    if depth == 0:
        # Caso base: dibuja el triángulo
        triangle = patches.Polygon(vertices, edgecolor='black', fill=None)
        ax.add_patch(triangle)
    else:
        # Divide el triángulo en 4 triángulos más pequeños
        midpoints = [
            ((vertices[0][0] + vertices[1][0]) / 2, (vertices[0][1] + vertices[1][1]) / 2),
            ((vertices[1][0] + vertices[2][0]) / 2, (vertices[1][1] + vertices[2][1]) / 2),
            ((vertices[2][0] + vertices[0][0]) / 2, (vertices[2][1] + vertices[0][1]) / 2)
        ]

        # Llamadas recursivas para los 3 triángulos restantes
        sierpinski_triangle(ax, depth-1, [vertices[0], midpoints[0], midpoints[2]])
        sierpinski_triangle(ax, depth-1, [vertices[1], midpoints[0], midpoints[1]])
        sierpinski_triangle(ax, depth-1, [vertices[2], midpoints[1], midpoints[2]])

# Configuración de la gráfica
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_axis_off()

# Vértices iniciales del triángulo equilátero
initial_vertices = [(0, 0), (1, 0), (0.5, 0.866)]

# Dibuja el Triángulo de Sierpinski con profundidad 4
sierpinski_triangle(ax, 4, initial_vertices)

# Muestra la gráfica
plt.show()
