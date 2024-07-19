import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def draw_tree(x, y, length, angle, depth, max_depth, width):
    if depth > max_depth:
        return
    
    angle_rad = np.radians(angle)
    
    x_end = x + length * np.cos(angle_rad)
    y_end = y + length * np.sin(angle_rad)
    
    color = (0.2 + 0.8 * depth / max_depth, 0, 0.5 + 0.5 * depth / max_depth)
    plt.plot([x, x_end], [y, y_end], color=color, linewidth=width)
    
    canvas.draw()
    canvas.get_tk_widget().update()
    
    draw_tree(x_end, y_end, length * 0.7, angle + 30, depth + 1, max_depth, width * 0.7)
    draw_tree(x_end, y_end, length * 0.7, angle - 30, depth + 1, max_depth, width * 0.7)

def draw_fractal_tree():
   
    plt.clf()
    plt.title('Árbol Recursivo')
    plt.axis('off')
    
  
    x = 0.5 
    y = 0.1  
    length = 0.3 
    angle = 90  
    max_depth = 10  
    width = 8  

    
    draw_tree(x, y, length, angle, 1, max_depth, width)

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

if __name__ == '__main__':
    main()