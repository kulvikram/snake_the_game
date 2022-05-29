from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.refresh()

    def refresh(self):
        self.color("green")
        self.speed("fastest")
        self.goto(random.randint(-340,340),random.randint(-340,340))



