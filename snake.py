from turtle import Turtle, Screen
import time

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
        self.segments[0].shape("turtle")

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


    def add_segment(self, position):
        turtle = Turtle(shape="circle")
        turtle.turtlesize(1)
        turtle.speed(2)
        turtle.penup()
        turtle.color("white")
        turtle.goto(position)
        self.segments.append(turtle)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(15)
        time.sleep(.1)

    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)
