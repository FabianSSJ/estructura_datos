import matplotlib.pyplot as plt
import numpy as np

def render_tree(start_x, start_y, branch_angle, max_depth, branch_length, canvas):
    if max_depth == 0:
        return
    
    end_x = start_x + branch_length * np.cos(branch_angle)
    end_y = start_y + branch_length * np.sin(branch_angle)
    
    canvas.plot([start_x, end_x], [start_y, end_y], color='green')
    
    # Recursively render the left and right branches
    render_tree(end_x, end_y, branch_angle - np.pi / 6, max_depth - 1, branch_length * 0.7, canvas)
    render_tree(end_x, end_y, branch_angle + np.pi / 6, max_depth - 1, branch_length * 0.7, canvas)

figure, canvas = plt.subplots()
canvas.set_aspect('equal')
canvas.axis('off')

# Start rendering the tree from the base point (0, 0)
render_tree(0, 0, np.pi / 2, 10, 100, canvas)  # Esta línea establece la profundidad inicial del árbol

plt.show()