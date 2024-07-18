import matplotlib.pyplot as plt
import numpy as np

def sierpinski(points, degree):
    def get_midpoint(p1, p2):
        return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

    if degree > 0:
        p1, p2, p3 = points
        
        # Calcula los puntos medios
        m1 = get_midpoint(p1, p2)
        m2 = get_midpoint(p2, p3)
        m3 = get_midpoint(p3, p1)
        
        # Llama recursivamente para cada subtriángulo
        sierpinski([p1, m1, m3], degree-1)
        sierpinski([m1, p2, m2], degree-1)
        sierpinski([m3, m2, p3], degree-1)
    else:
        # Dibuja el triángulo
        plt.fill(*zip(*points), "k")

def draw_sierpinski(degree):
    points = np.array([(0, 0), (0.5, np.sqrt(3)/2), (1, 0)])
    
    plt.figure(figsize=(8, 8))
    sierpinski(points, degree)
    plt.axis('off')
    plt.title(f"Triángulo de Sierpinski - Nivel {degree}")
    plt.tight_layout()
    plt.savefig(f'sierpinski_nivel_{degree}.png', dpi=300, bbox_inches='tight')
    plt.show()

# Dibujar para los niveles especificados
levels = [0, 1, 3, 6, 8]

for level in levels:
    draw_sierpinski(level)