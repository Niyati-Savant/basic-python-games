import turtle as t
import random

timmy = t.Turtle()
timmy.shape("arrow")
timmy.speed('fastest')


"""To draw a square"""
# for a in range(4):
#     timmy.forward(100)
#     timmy.left(90)

"""To draw a dashed lines"""
# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()
"""To draw all shapes in diff colors"""

"""To to set RGB colors"""
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    selected_color = (r,g,b)
    return selected_color


# colors = ["red", "royal blue", "green", "firebrick", "green yellow", "gold", "salmon", "dark magenta", "cyan",
#           "medium slate blue", "orange", "slate gray", "blue violet",]
# for shape in range(3, 9):
#     angle = 360 / shape
#     timmy.color(random.choice(colors))
#     for side in range(shape):
#         timmy.forward(100)
#         timmy.right(angle)

"""TO set random path"""
# directions = [0, 90, 180, 270]
#
# timmy.pensize(10)
# timmy.speed('fastest')
# for _ in range(200):
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))

"""Spirograph"""

def draw_spirograph(gap_size):
    for _ in range(int(360/gap_size)):
        timmy.circle(100)
        timmy.color(random_color())
        timmy.setheading(timmy.heading() + gap_size)

draw_spirograph(5)

my_screen = t.Screen()
my_screen.exitonclick()
