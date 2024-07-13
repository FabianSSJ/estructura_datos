import matplotlib.pyplot as plt
import numpy as np

def draw_triangle(ax, p1, p2, p3, depth):
    if depth == 0:
        triangle = plt.Polygon([p1, p2, p3], closed=True, fill=None, edgecolor='black')
        ax.add_patch(triangle)
    else:
        # Calculate midpoints
        mid1 = (p1 + p2) / 2
        mid2 = (p2 + p3) / 2
        mid3 = (p1 + p3) / 2

        # Recursive calls
        draw_triangle(ax, p1, mid1, mid3, depth - 1)
        draw_triangle(ax, mid1, p2, mid2, depth - 1)
        draw_triangle(ax, mid3, mid2, p3, depth - 1)

def sierpinski_triangle(depth):
    fig, ax = plt.subplots()
    ax.set_aspect('equal', 'box')
    p1 = np.array([0, 0])
    p2 = np.array([1, 0])
    height = np.sqrt(3) / 2
    p3 = np.array([0.5, height])

    draw_triangle(ax, p1, p2, p3, depth)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, height)
    ax.axis('off')
    plt.show()

# Example usage:
sierpinski_triangle(depth=6)

