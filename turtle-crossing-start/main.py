import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move,"Up")
game_is_on = True


while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.make_cars()
    car.start_moving()

    for car_item in car.all_cars:
        if car_item.distance(player) < 20:
            game_is_on = False
            score.game_over()

        if player.ycor() > 280:
            player.goto(0, -280)
            car.inc_speed()
            score.level_up()

screen.exitonclick()