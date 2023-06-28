from turtle import Turtle

ALIGN = 'center'
FONT = ("Arial", 15, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        with open("data.txt") as f:
            self.high_score = int(f.read())
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 250)
        self.update_board()


    def update_board(self):
        self.clear()
        self.write(f'Score: {self.score} High-Score:{self.high_score}', move=False, align=ALIGN, font=FONT)

    def inc_score(self):
        self.score += 10
        self.update_board()

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt",mode='w') as f:
                f.write(str(self.score))
        self.score = 0
        self.update_board()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f' GAME OVER', move=False, align=ALIGN, font=FONT)

