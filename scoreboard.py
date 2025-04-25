from turtle import Turtle
align = 'center'
font = ('Courier', 20, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.color('white')
        self.show_score()


    def show_score(self):
        self.write(f"Score: {self.score}", False, align = align, font = font)

    def update_score(self):
        self.score += 1
        self.clear()
        self.show_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over.", False, align = align, font = font)





