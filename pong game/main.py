from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

r_pos = (350, 0)
l_pos = (-350, 0)

my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(width=800, height=600)
my_screen.title("PONG")
my_screen.tracer(0)


pad_r = Paddle(r_pos)
pad_l = Paddle(l_pos)
pong_ball = Ball()
score = ScoreBoard()

my_screen.listen()
my_screen.onkey(pad_r.move_up, "Up")
my_screen.onkey(pad_r.move_down, "Down")

my_screen.onkey(pad_l.move_up, "w")
my_screen.onkey(pad_l.move_down, "s")

game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(pong_ball.move_speed)
    pong_ball.move()

    # top & bottom wall collision
    if pong_ball.ycor() > 280 or pong_ball.ycor() < -280:
        pong_ball.bounce_y()

    if pong_ball.distance(pad_r) < 50 and pong_ball.xcor() > 320 or \
            pong_ball.distance(pad_l) < 50 and pong_ball.xcor() < -320:
        pong_ball.bounce_x()

    # ball miss by paddle right or left
    if pong_ball.xcor() > 380:
        pong_ball.resetpos()
        score.l_point()


    if pong_ball.xcor() < -380:
        pong_ball.resetpos()
        score.r_point()

    if score.l_score == 5 or score.r_score == 5:
        game_is_on = False

my_screen.exitonclick()
