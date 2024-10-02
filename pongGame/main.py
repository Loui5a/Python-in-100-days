from turtle import Turtle, Screen
from padle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


START_COORDINATES = [(350, 0), (-350, 0)]
SCOREBOARD_POSITIONS = [(-100, 200),(100, 200)]
PLAYER_STRING = ["LEFT PLAYER", "RIGHT"]

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle(START_COORDINATES[0])
left_paddle = Paddle(START_COORDINATES[1])
ball = Ball()
scoreboard_left = Scoreboard(SCOREBOARD_POSITIONS[0])
scoreboard_right = Scoreboard(SCOREBOARD_POSITIONS[1])

screen.listen()
screen.onkey(right_paddle.paddle_up, "Up")
screen.onkey(right_paddle.paddle_down, "Down")

screen.onkey(left_paddle.paddle_up, "w")
screen.onkey(left_paddle.paddle_down, "s")

game_on = True
score_left = 0
score_right = 0

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if scoreboard_left.score > 2 or scoreboard_right.score > 2:
        game_on = False
        ball.hideturtle()
        if scoreboard_left.score > scoreboard_right.score:
            scoreboard_left.game_over(PLAYER_STRING[0])
        else:
            scoreboard_right.game_over(PLAYER_STRING[1])


    # Detect collision with top and bottom wall:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect right misses:
    if ball.xcor() > 350:
        scoreboard_left.score += 1
        scoreboard_left.update_scoreboard()
        ball.reset_position()
        ball.move()

    if ball.xcor() < -350:
        scoreboard_right.score += 1
        scoreboard_right.update_scoreboard()
        ball.reset_position()
        ball.move()

    #detect collision with paddles:
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()



screen.exitonclick()
