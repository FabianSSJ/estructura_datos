import matplotlib.pyplot as plt

def draw_triangle(ax, vertices, color='green'):
    triangle = plt.Polygon(vertices, edgecolor=color, fill=None)
    ax.add_patch(triangle)

def sierpinski(ax, depth, vertices):
    if depth == 0:
        draw_triangle(ax, vertices)
    else:
        # en la mitad 
        mid01 = [(vertices[0][0] + vertices[1][0]) / 2, (vertices[0][1] + vertices[1][1]) / 2]
        mid12 = [(vertices[1][0] + vertices[2][0]) / 2, (vertices[1][1] + vertices[2][1]) / 2]
        mid20 = [(vertices[2][0] + vertices[0][0]) / 2, (vertices[2][1] + vertices[0][1]) / 2]
        
        #recursividad
        sierpinski(ax, depth-1, [vertices[0], mid01, mid20])
        sierpinski(ax, depth-1, [vertices[1], mid12, mid01])
        sierpinski(ax, depth-1, [vertices[2], mid20, mid12])

def main():
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')

    # triangulo inicial 
    vertices = [[0, 0], [1, 0], [0.5, 1]]
    depth = 2  #profundiad aplicada ......
    
    sierpinski(ax, depth, vertices)
    

    plt.show()

if __name__ == "__main__":
    main()
