import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_single_triangle(ax, points, color='k'):
    triangle = patches.Polygon(points, closed=True, edgecolor=color, fill=False)
    ax.add_patch(triangle)

def draw_sierpinski(ax, points, level):
    if level == 0:
        draw_single_triangle(ax, points)
    else:
        mid_point = lambda p1, p2: [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]
        point1, point2, point3 = points
        mid12 = mid_point(point1, point2)
        mid23 = mid_point(point2, point3)
        mid31 = mid_point(point3, point1)
        
        draw_sierpinski(ax, [point1, mid12, mid31], level-1)
        draw_sierpinski(ax, [mid12, point2, mid23], level-1)
        draw_sierpinski(ax, [mid31, mid23, point3], level-1)

def main(level):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')
    
    initial_points = [[0, 0], [1, 0], [0.5, 0.866]]
    draw_sierpinski(ax, initial_points, level)
    
    plt.show()

if __name__ == "__main__":
    level = int(input("Enter the depth: "))
    main(level)
