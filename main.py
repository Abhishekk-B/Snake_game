from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

scr = Screen()
scr.bgcolor("black")
scr.title("Snake Game")
scr.setup(width=600, height=600)
scr.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
scr.listen()
scr.onkey(snake.up, "Up")
scr.onkey(snake.down, "Down")
scr.onkey(snake.right, "Right")
scr.onkey(snake.left, "Left")

is_on = True
while is_on:
    scr.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_on = False
        scoreboard.game_over()

    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            is_on = False
            scoreboard.game_over()

scr.exitonclick()
