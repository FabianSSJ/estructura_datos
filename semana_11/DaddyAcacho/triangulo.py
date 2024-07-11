import matplotlib.pyplot as plt
import numpy as np

def sierpinski_triangle(ax, vertices, depth):
    if depth == 0:
    
        triangle = plt.Polygon(vertices, edgecolor='black', fill=None)
        ax.add_patch(triangle)
    else:
       
        midpoints = [
            (vertices[0] + vertices[1]) / 2,
            (vertices[1] + vertices[2]) / 2,
            (vertices[2] + vertices[0]) / 2
        ]
        
    
        sierpinski_triangle(ax, [vertices[0], midpoints[0], midpoints[2]], depth - 1)
        sierpinski_triangle(ax, [vertices[1], midpoints[0], midpoints[1]], depth - 1)
        sierpinski_triangle(ax, [vertices[2], midpoints[1], midpoints[2]], depth - 1)

def draw_sierpinski(depth):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    plt.axis('off')

    vertices = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3) / 2]])
    
    sierpinski_triangle(ax, vertices, depth)

    plt.show()

draw_sierpinski(4)

for i in range(5):
    draw_sierpinski(i)
