import matplotlib.pyplot as plt
import math

# Función recursiva para dibujar el árbol
def draw_tree(x, y, length, angle, depth, max_depth, length_factor, branch_angle):
    if depth == max_depth:
        plt.plot([x, x + length * math.cos(angle)], [y, y + length * math.sin(angle)], color='green', linewidth=2)
        return

    x_new = x + length * math.cos(angle)
    y_new = y + length * math.sin(angle)

    plt.plot([x, x_new], [y, y_new], color='brown', linewidth=2 - depth * 0.1)

    draw_tree(x_new, y_new, length * length_factor, angle + branch_angle, depth + 1, max_depth, length_factor, branch_angle)
    draw_tree(x_new, y_new, length * length_factor, angle - branch_angle, depth + 1, max_depth, length_factor, branch_angle)

# Función para inicializar y mostrar el dibujo
def draw_recursive_tree(max_depth):
    initial_length = 1
    initial_angle = math.pi / 2
    length_factor = 0.7
    branch_angle = math.radians(30)

    plt.figure(figsize=(10, 10))
    plt.axis('off')
    plt.title(f"Árbol Recursivo - Profundidad {max_depth}")

    draw_tree(0, -1, initial_length, initial_angle, 0, max_depth, length_factor, branch_angle)

    plt.show()

if __name__ == '__main__':
    # Probar con diferentes niveles de profundidad
    for depth in range(3, 11):
        draw_recursive_tree(depth)
