from turtle import Turtle, Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.02)
    snake.move()

    if snake.snake_body[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.update_score()


    if snake.snake_body[0].xcor() > 280 or snake.snake_body[0].ycor() > 280 or snake.snake_body[0].xcor() < -280 or snake.snake_body[0].ycor() < -280:
        game_on = False
        score.game_over()

    for block in snake.snake_body[1:]:
        if snake.snake_body[0].distance(block) < 5:
            game_on = False
            score.game_over()











screen.exitonclick()