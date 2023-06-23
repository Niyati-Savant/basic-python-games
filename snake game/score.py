from turtle import Turtle

ALIGN = 'center'
FONT = ("Arial", 15, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 250)
        self.update_board()


    def update_board(self):
        self.write(f'Score: {self.score}', move=False, align=ALIGN, font=FONT)

    def inc_score(self):
        self.score += 10
        self.clear()
        self.update_board()

    def game_over(self):
        self.goto(0,0)
        self.write(f'GAME OVER', move=False, align=ALIGN, font=FONT)

