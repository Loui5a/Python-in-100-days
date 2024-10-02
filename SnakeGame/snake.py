from turtle import Turtle
START_COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    #creates the snake with 3 segments:
    def create_snake(self):
        for coordinates in START_COORDINATES:
            self.add_segment(coordinates)

    def add_segment(self, coordinates):
        square = Turtle()
        square.shape("square")
        square.color("white")
        square.penup()
        square.goto(coordinates)
        self.segments.append(square)

    # extend the snake with one segment:
    def extend(self):
        self.add_segment(self.segments[-1].position())


    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
    # moves each segment forward:
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # up, down, left and right changes the position of the head.
    # the snake can only change direction 90 degrees at the time.
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)




