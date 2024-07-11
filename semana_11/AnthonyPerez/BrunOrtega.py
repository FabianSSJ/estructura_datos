import matplotlib.pyplot as plt

def draw_sierpinski(x, y, size, depth):
    if depth == 0:
        # Draw a triangle
        plt.plot([x, x + size, x + size / 2, x], [y, y, y + size * 3**0.5 / 2, y], 'b-')
    else:
        # Recursively draw three smaller triangles
        draw_sierpinski(x, y, size / 2, depth - 1)
        draw_sierpinski(x + size / 2, y, size / 2, depth - 1)
        draw_sierpinski(x + size / 4, y + size * 3**0.5 / 4, size / 2, depth - 1)

# Set the size and depth of the triangle
size = 1
depth = 5

# Create a new figure
plt.figure()

# Draw the Sierpinski Triangle
draw_sierpinski(0, 0, size, depth)

# Show the plot
plt.show()