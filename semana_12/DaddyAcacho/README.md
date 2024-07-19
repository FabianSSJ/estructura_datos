# Árbol Recursivo con Python

Este proyecto implementa un árbol recursivo utilizando Python con las bibliotecas Matplotlib y Tkinter. El árbol se dibuja en una ventana gráfica, y la profundidad de la recursión puede ser ajustada para observar diferentes configuraciones del árbol.

## Requisitos

Asegúrate de tener instaladas las siguientes bibliotecas:

```bash
pip install matplotlib numpy
```

### Explicación de los Comandos

- `pip install matplotlib numpy`:
  - **`pip`**: Herramienta de gestión de paquetes para Python.
  - **`install`**: Comando para instalar paquetes.
  - **`matplotlib`**: Biblioteca para crear gráficos y visualizaciones.
  - **`numpy`**: Biblioteca para el manejo eficiente de arreglos y operaciones matemáticas.

## Descripción del Código

### Código Principal

El código principal configura una interfaz gráfica con Tkinter y dibuja un árbol recursivo utilizando Matplotlib. Los puntos claves son:

- **Importar Librerías**:
  ```python
  import matplotlib.pyplot as plt
  import numpy as np
  import tkinter as tk
  from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
  ```

- **Función para Dibujar el Árbol**:
  ```python
  def draw_tree(x, y, length, angle, depth, max_depth, width):
      if depth > max_depth:
          return
      # ... lógica para dibujar ramas ...
      canvas.draw()
      canvas.get_tk_widget().update()
  ```

- **Función para Iniciar el Dibujo**:
  ```python
  def draw_fractal_tree():
      plt.clf()
      plt.title('Árbol Recursivo')
      plt.axis('off')
      # Parámetros iniciales
      draw_tree(x, y, length, angle, 1, max_depth, width)
  ```

- **Configuración de la Interfaz Gráfica**:
  ```python
  def main():
      global canvas
      root = tk.Tk()
      root.title("Dibujar Árbol Recursivo")
      frame = tk.Frame(root)
      frame.pack(pady=20)
      repeat_button = tk.Button(frame, text="Repetir", command=draw_fractal_tree)
      repeat_button.pack()
      fig = plt.figure(figsize=(12, 12))
      canvas = FigureCanvasTkAgg(fig, master=root)
      canvas.get_tk_widget().pack()
      root.after(1000, draw_fractal_tree)
      root.mainloop()
  ```

## Descripción Teórica

Un árbol recursivo es una estructura que se construye a partir de una raíz y se subdivide en ramas más pequeñas a medida que se profundiza en la recursión. Cada rama principal se divide en dos subramas, y este proceso se repite hasta alcanzar una profundidad máxima. La recursividad permite que cada nivel del árbol se genere a partir de la misma lógica aplicada a un nivel más pequeño.

## Cómo Ejecutar el Código

1. **Instala las bibliotecas necesarias**:
   ```bash
   pip install matplotlib numpy
   ```

2. **Guarda el código en un archivo** llamado `tree_recursive.py`.

3. **Ejecuta el archivo con el siguiente comando**:
   ```bash
   python tree_recursive.py
   ```
## Conclusión

El árbol recursivo se implementó utilizando Python con las bibliotecas Matplotlib y Tkinter. La implementación se basó en el principio de recursividad para construir una estructura de árbol, donde cada rama se subdivide en dos ramas menores en cada nivel de profundidad.

**Proceso de Implementación:**

1. **Configuración Inicial**: Se configuró un entorno gráfico con Tkinter para mostrar el árbol y se creó un lienzo de Matplotlib incrustado en la ventana de Tkinter.

2. **Función Recursiva**: La función `draw_tree` fue diseñada para dibujar el árbol recursivamente. Cada llamada recursiva calcula la posición y el color de la rama actual, y luego llama a sí misma para dibujar las ramas secundarias.

3. **Actualización de la Vista**: Después de cada actualización de las ramas, el lienzo de Matplotlib se actualiza para reflejar los cambios en la interfaz gráfica.

4. **Interfaz Gráfica**: Se añadió un botón para permitir la regeneración del árbol en la ventana gráfica, facilitando la visualización de árboles con diferentes configuraciones.

El resultado es un árbol recursivo visualmente atractivo que ilustra cómo los conceptos de recursividad y programación gráfica pueden combinarse para crear representaciones complejas y detalladas de estructuras naturales.

