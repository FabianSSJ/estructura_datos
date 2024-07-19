import matplotlib.pyplot as plt
import math

def draw_tree(ax, x, y, length, angle, depth):
    if depth == 0:
        return

    # Calcula las coordenadas del punto final de la rama
    x_end = x + length * math.cos(angle)
    y_end = y + length * math.sin(angle)

    # Dibuja la línea
    ax.plot([x, x_end], [y, y_end], color='brown')

    # Reduce la longitud de la rama y la profundidad
    new_length = length * 0.7
    new_depth = depth - 1

    # Llama recursivamente para las dos ramas
    draw_tree(ax, x_end, y_end, new_length, angle + math.pi / 6, new_depth)
    draw_tree(ax, x_end, y_end, new_length, angle - math.pi / 6, new_depth)

def main():
    # Solicita la profundidad del usuario
    depth = int(input("Ingrese la profundidad del árbol recursivo: "))

    # Crea la figura y el eje
    fig, ax = plt.subplots()

    # Ajusta los límites del gráfico
    ax.set_xlim(-100, 100)
    ax.set_ylim(0, 150)

    # Dibuja el árbol recursivo
    draw_tree(ax, 0, 0, 50, math.pi / 2, depth)

    # Muestra el gráfico
    plt.show()

if __name__ == "__main__":
    main()

