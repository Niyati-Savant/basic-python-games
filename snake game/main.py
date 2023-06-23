from turtle import Screen
import snake
import food
import time
import score

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(0)

my_snake = snake.Snake()
food = food.Food()
score_board = score.ScoreBoard()

my_screen.listen()
my_screen.onkey(my_snake.up, "Up")
my_screen.onkey(my_snake.down, "Down")
my_screen.onkey(my_snake.left, "Left")
my_screen.onkey(my_snake.right, "Right")
game_on = True

"""snake moves such that the 3rd seg takes place of 2nd ,2nd takes place of 1st and 1st moves ahead"""
while game_on:
    my_screen.update()
    time.sleep(0.1)
    my_snake.move()

    # eating food
    if food.distance(my_snake.head) < 15:
        food.reposition()
        my_snake.extend()
        score_board.inc_score()
    # Wall collision
    if my_snake.head.xcor() > 280 or my_snake.head.xcor() < -280 or \
            my_snake.head.ycor() > 280 or my_snake.head.ycor() < -280:
        game_on = False
        score_board.game_over()

    # Tail collision
    for part in my_snake.snake_body[1::]:
        if my_snake.head.distance(part) < 10:
            game_on = False
            score_board.game_over()

my_screen.exitonclick()
