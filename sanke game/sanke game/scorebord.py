from turtle import Turtle

noo = 0


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 260)
        self.penup()
        self.color("white")
        self.num = noo
        self.update()

    def update(self):
        self.write(f"score : {self.num}", align="center", font=("Arial", 20, "normal"))

    def increase(self):
        self.num += 1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 28, "normal"))



