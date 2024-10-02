import turtle
from random import randrange, randint, choice
from turtle import Turtle, Screen

Chad = Turtle()
Chad.shape("turtle")
Chad.color("chartreuse4")
# draw a square:

#polygon_angles = []
#for i in range(7):
#    polygon_angles.append(360/(4+i))
#polygon_colors = ["red", "green", "blue", "yellow", "brown", "black", "gray"]
#for i in range(7):
#    Chad.color(polygon_colors[i])
#    for _ in range(4+i):
#        Chad.forward(100)
#        Chad.left(polygon_angles[i])

# make the turle walk randomly:


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color


#Chad.pensize(10)
turtle.colormode(255)
Chad.speed("fastest")
#directions = [0, 90, 180, 270]
#for i in range(100):
#    Chad.color(random_color())
#    Chad.forward(30)
#    Chad.setheading(choice(directions))

# make the turtle draw a spirograph:
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        Chad.color(random_color())
        Chad.circle(100)
        current_heading = Chad.heading()
        Chad.setheading(current_heading + 10)

draw_spirograph(5)















screen = Screen()
screen.exitonclick()