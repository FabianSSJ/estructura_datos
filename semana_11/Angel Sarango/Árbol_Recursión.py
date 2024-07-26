import matplotlib.pyplot as plt
import math
def dibujar_arbol(x, y, longitud, angulo, nivel):
    if nivel == 0:
        return
    # Calcula las coordenadas finales de la rama
    x_fin = x + longitud * math.cos(math.radians(angulo))
    y_fin = y + longitud * math.sin(math.radians(angulo))
    # Dibuja la rama actual
    plt.plot([x, x_fin], [y, y_fin], color='black')
    # Llama recursivamente para las ramas a la izquierda y derecha
    dibujar_arbol(x_fin, y_fin, longitud * 0.7, angulo - 20, nivel - 1)
    dibujar_arbol(x_fin, y_fin, longitud * 0.7, angulo + 20, nivel - 1)
def main():
    # Configuración inicial del gráfico
    plt.figure(figsize=(8, 8))
    plt.title('Árbol Recursivo')
    plt.axis('equal')
    # Parámetros del árbol
    x_inicio, y_inicio = 0, 0  # Coordenadas del punto inicial
    longitud_inicial = 100     # Longitud inicial de la rama
    angulo_bifurcacion = 90    # Ángulo de bifurcación
    nivel_profundidad = 3      # Nivel de profundidad del árbol
    # Llama a la función para dibujar el árbol con los parámetros especificados
    dibujar_arbol(x_inicio, y_inicio, longitud_inicial, angulo_bifurcacion, nivel_profundidad)
    # Mostrar el gráfico
    plt.show()
if __name__ == "__main__":
    main()
