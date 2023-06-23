from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color('green')
        self.shapesize(0.5, 0.5)
        self.speed('fastest')
        self.reposition()

    def reposition(self):
        new_x = randint(-260,260)
        new_y = randint(-260, 260)
        self.goto(new_x,new_y)


