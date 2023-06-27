from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.update_board()

    def update_board(self):
        self.clear()
        self.write(f"Level: {self.level}",move=False,align='Left',font=FONT)

    def level_up(self):
        self.level += 1
        self.update_board()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",move=False,align='Center',font=FONT)

