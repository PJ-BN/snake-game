from turtle import Turtle, Screen

screen = Screen()

Position = [(0, 0), (20, 0), (40, 0)]
MOMENT = 17
UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180


class Snake:

    def __init__(self):

        self.tur = []
        self.create()
        self.head = self.tur[0]

    def create(self):
        for i in Position:
            self.add(i)

    def add(self, i):
        new_tur = Turtle("square")
        new_tur.penup()
        new_tur.color("white")
        new_tur.goto(i)

        self.tur.append(new_tur)

    def extend(self):
        self.add(self.tur[-1].position())

    def move(self):
        for t in range(len(self.tur) - 1, 0, -1):
            x_new = self.tur[t - 1].xcor()
            y_new = self.tur[t - 1].ycor()
            self.tur[t].goto(x_new, y_new)
        self.head.forward(MOMENT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

