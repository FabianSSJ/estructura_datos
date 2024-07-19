import matplotlib.pyplot as plt
import numpy as np

def dibujar_arbol_recursivo(ax, nivel, x, y, longitud, angulo, angulo_bifurcacion):
    """
    Función recursiva para dibujar un árbol fractal.

    Parámetros:
    ax (matplotlib.axes.Axes): El eje en el que se dibujará el árbol.
    nivel (int): El nivel actual de recursión.
    x (float): Coordenada x del punto inicial de la rama.
    y (float): Coordenada y del punto inicial de la rama.
    longitud (float): Longitud de la rama actual.
    angulo (float): Ángulo de la rama actual en grados.
    angulo_bifurcacion (float): Ángulo de bifurcación entre ramas en grados.
    """
    if nivel == 0:
        return
    
    # Calcular el punto final de la rama
    x2 = x + longitud * np.cos(np.radians(angulo))
    y2 = y + longitud * np.sin(np.radians(angulo))
    
    # Dibujar la rama
    ax.plot([x, x2], [y, y2], 'b-')
    
    # Recursión para las ramas izquierda y derecha
    nuevo_longitud = longitud * 0.7  # Reducir la longitud para las subramas
    dibujar_arbol_recursivo(ax, nivel-1, x2, y2, nuevo_longitud, angulo - angulo_bifurcacion, angulo_bifurcacion)
    dibujar_arbol_recursivo(ax, nivel-1, x2, y2, nuevo_longitud, angulo + angulo_bifurcacion, angulo_bifurcacion)

def crear_arbol_recursivo(nivel, angulo_bifurcacion):
    """
    Crea y muestra un árbol recursivo.

    Parámetros:
    nivel (int): Número de niveles de recursión para el árbol.
    angulo_bifurcacion (float): Ángulo de bifurcación entre ramas en grados.
    """
    # Crear una nueva figura y eje
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Iniciar el árbol desde el centro inferior
    dibujar_arbol_recursivo(ax, nivel, 0, -1, 0.5, 90, angulo_bifurcacion)
    
    # Añadir título al gráfico
    plt.title(f'Árbol Recursivo (Nivel: {nivel}, Ángulo: {angulo_bifurcacion}°)')
    
    # Mostrar el gráfico
    plt.show()

# Ejemplo de uso
if __name__ == "__main__":
    crear_arbol_recursivo(nivel=8, angulo_bifurcacion=30)