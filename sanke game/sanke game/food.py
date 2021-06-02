from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.7, 0.7)
        self.color("green")
        self.refresh()

    def refresh(self):
        x_cordinte = random.randint(-280, 280)
        y_cordinte = random.randint(-280, 280)
        self.goto(x_cordinte, y_cordinte)
