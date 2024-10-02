import colorgram
from turtle import Turtle, Screen
import random
import turtle as turtle_module

Chad = Turtle()
Chad.speed("fastest")

colorgram_colors = colorgram.extract('hirstPainting.jpg',30)
colors = []
for value in colorgram_colors:
    rgb = value.rgb
    color_tuple = (rgb.r, rgb.g, rgb.b)
    colors.append(color_tuple)

print(colors)



color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]
turtle_module.colormode(255)
Chad.hideturtle()
Chad.penup()
Chad.setheading(225)
Chad.forward(300)
Chad.setheading(0)
Chad.pendown()
for _ in range(10):
    for _ in range(10):
        Chad.dot(20, random.choice(color_list))
        Chad.penup()
        Chad.forward(50)
        Chad.pendown()

    Chad.setheading(90)
    Chad.penup()
    Chad.forward(50)
    Chad.setheading(180)
    Chad.forward(500)
    Chad.setheading(0)




screen = Screen()
screen.exitonclick()