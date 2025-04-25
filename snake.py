from turtle import Turtle, Screen
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

x = 0
y = 0
starting_positions = []
for i in range(3):
    x-=20
    starting_positions.append((x,y))

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()

    def create_snake(self):
        for position in starting_positions:
            self.add_block(position)

    def add_block(self, position):
        snake = Turtle()
        snake.penup()
        snake.shape("square")
        snake.color("white")
        snake.goto(position)
        self.snake_body.append(snake)

    def extend(self):
        for i in range(8):
            self.add_block(self.snake_body[-1].position())


    def move(self):
        for block_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[block_num - 1].xcor()
            new_y = self.snake_body[block_num - 1].ycor()
            self.snake_body[block_num].goto(new_x, new_y)
        self.snake_body[0].forward(5)

    def up(self):
        if self.snake_body[0].heading() != DOWN:
            self.snake_body[0].setheading(UP)

    def down(self):
        if self.snake_body[0].heading() != UP:
            self.snake_body[0].setheading(DOWN)

    def left(self):
        if self.snake_body[0].heading() != RIGHT:
            self.snake_body[0].setheading(LEFT)

    def right(self):
        if self.snake_body[0].heading() != LEFT:
            self.snake_body[0].setheading(RIGHT)

