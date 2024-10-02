from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
y_coordinates = [-100, -60, -20, 20, 60, 100]
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
chads = []
for i in range(6):
    new_chad = Turtle(shape="turtle")
    new_chad.penup()
    new_chad.color(colors[i])
    new_chad.goto(-230,y_coordinates[i])
    chads.append(new_chad)


if user_bet:
    is_race_on = True


while is_race_on:

    for chad in chads:
        if chad.xcor() > 230:
            is_race_on = False
            winning_color = chad.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0,10)
        chad.forward(rand_distance)

screen.exitonclick()