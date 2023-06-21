# from turtle import Turtle, Screen
"""Testing event listener"""
import turtle
# tom = Turtle()
# my_screen = Screen()
#
#
# def move_forward():
#     tom.forward(100)
#
# def move_backward():
#     tom.backward(100)
#
# def turn_right():
#     tom.setheading(tom.heading()-10)
#
# def turn_left():
#     tom.left(10)
#
# def clear_screen():
#     tom.clear()
#     tom.penup()
#     tom.setposition(0, 0)
#     tom.pendown()
#
# my_screen.listen()
# my_screen.onkey(key="w", fun=move_forward)
# my_screen.onkey(key="b", fun=move_backward)
# my_screen.onkey(key="a", fun=turn_right)
# my_screen.onkey(key="d", fun=turn_left)
# my_screen.onkey(key="c", fun=clear_screen)
# my_screen.exitonclick()

from turtle import Turtle, Screen
import random

my_screen = Screen()
my_screen.setup(width=600, height=450)

is_game_on = False
user_bet = my_screen.textinput(title="Place a bet", prompt="Predict which one will win?")

y_coordinates = [-150, -100, -50, 0, 50, 100, 150]
colors = ['red', 'pink', 'yellow', 'orange', 'blue', 'lavender', 'green']
player_list = []

for x in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[x])
    new_turtle.penup()
    new_turtle.goto(x=-270, y=y_coordinates[x])
    player_list.append(new_turtle)

if user_bet:
    is_game_on = True

while is_game_on:
    for player in player_list:
        if player.xcor() > 280:
            is_game_on = False
            winner = player.pencolor()
            if winner == user_bet:
                print(f"Your {user_bet} turtle Won")
            else:
                print(f"Your {user_bet} turtle lost")
            print(f"Winning turtle was {winner}")
            break

        player.forward(random.randint(1, 10))


my_screen.exitonclick()
