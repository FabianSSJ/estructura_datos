import turtle
import random

def draw_triangle(points, color, my_turtle):
    my_turtle.fillcolor(color)
    my_turtle.up()
    my_turtle.goto(points[0])
    my_turtle.down()
    my_turtle.begin_fill()
    for point in points[1:] + [points[0]]:
        my_turtle.goto(point)
    my_turtle.end_fill()

def get_midpoint(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points, degree, my_turtle):
    color_map = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    draw_triangle(points, random.choice(color_map), my_turtle)
    
    if degree > 0:
        sierpinski([points[0], 
                    get_midpoint(points[0], points[1]),
                    get_midpoint(points[0], points[2])],
                   degree - 1, my_turtle)
        sierpinski([points[1], 
                    get_midpoint(points[0], points[1]),
                    get_midpoint(points[1], points[2])],
                   degree - 1, my_turtle)
        sierpinski([points[2], 
                    get_midpoint(points[2], points[1]),
                    get_midpoint(points[0], points[2])],
                   degree - 1, my_turtle)

def main():
    screen = turtle.Screen()
    screen.setup(800, 600)
    screen.title("Triángulo de Sierpinski")
    screen.bgcolor("black")

    my_turtle = turtle.Turtle()
    my_turtle.speed(0)  # Máxima velocidad
    my_turtle.hideturtle()

    points = [(-200, -100), (0, 200), (200, -100)]
    
    sierpinski(points, 5, my_turtle)
    
    screen.exitonclick()
    

if __name__ == "__main__":
    main()