from turtle import Screen
import time

from snake import Snake
from food import Food
from scorebord import Scoreboard


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)

game = True

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

while game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 17:
        food.refresh()
        score.increase()
        snake.extend()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game = False
        score.game_over()

    for seg in snake.tur:
        if seg != snake.head:
            pass

            if snake.head.distance(seg) < 10:
                game = False
                score.game_over()
            else:
                pass
        else:
            pass

        print(seg)

screen.exitonclick()
