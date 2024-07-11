import matplotlib.pyplot as plt

def sierpinski_triangle(ax, vertices, depth, color='black'):
    if depth == 0:
        triangle = plt.Polygon(vertices, edgecolor=color, facecolor='none')
        ax.add_patch(triangle)
    else:
        midpoints = [
            ((vertices[0][0] + vertices[1][0]) / 2, (vertices[0][1] + vertices[1][1]) / 2),
            ((vertices[1][0] + vertices[2][0]) / 2, (vertices[1][1] + vertices[2][1]) / 2),
            ((vertices[2][0] + vertices[0][0]) / 2, (vertices[2][1] + vertices[0][1]) / 2)
        ]
        
        sierpinski_triangle(ax, [vertices[0], midpoints[0], midpoints[2]], depth - 1, color)
        sierpinski_triangle(ax, [vertices[1], midpoints[0], midpoints[1]], depth - 1, color)
        sierpinski_triangle(ax, [vertices[2], midpoints[1], midpoints[2]], depth - 1, color)

def plot_sierpinski(depth, color='blue'):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')
    
    vertices = [(0, 0), (1, 0), (0.5, 0.866)]
    sierpinski_triangle(ax, vertices, depth, color)
    
    plt.show()

if __name__ == "__main__":
    depth = 3  
    color = 'blue'  
    plot_sierpinski(depth, color)