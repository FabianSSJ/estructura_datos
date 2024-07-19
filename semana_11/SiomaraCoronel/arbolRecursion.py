# Importar las librerías
import matplotlib.pyplot as plt
import numpy as np

# Definir una función para dibujar un árbol recursivamente
def dibujar_arbol(profundidad, x0, y0, longitud, angulo):
    # Caso base: si la profundidad es 0, terminar la función recursiva
    if profundidad == 0:
        return

    # Calcular las coordenadas del punto final de la rama utilizando trigonometría
    x1 = x0 + longitud * np.cos(np.radians(angulo))
    y1 = y0 + longitud * np.sin(np.radians(angulo))

    # Dibujar la rama entre (x0, y0) y (x1, y1) con color marrón
    plt.plot([x0, x1], [y0, y1], color='brown')

    # Llamada recursiva para dibujar las ramas hijas
    dibujar_arbol(profundidad - 1, x1, y1, longitud * 0.7, angulo + 30)
    dibujar_arbol(profundidad - 1, x1, y1, longitud * 0.7, angulo - 30)

# Crear la figura y el objeto de ejes para dibujar el árbol
fig, ax = plt.subplots(figsize=(8, 8))
# Establecer los límites del gráfico en el eje x y en el eje y
ax.set_xlim([-15, 15])
ax.set_ylim([0, 15])
# Establecer el aspecto de la figura como igual para evitar distorsiones
ax.set_aspect('equal')
# Desactivar los ejes para una presentación más limpia
ax.axis('off')
# Llamar a la función dibujar_arbol para empezar a dibujar un árbol con profundidad 12
dibujar_arbol(12, 0, 0, 5, 90)
# Mostrar el gráfico con el árbol dibujado
plt.show()

