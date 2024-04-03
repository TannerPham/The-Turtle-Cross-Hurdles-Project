import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from gamedisplay import Border
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
screen = Screen()

screen.setup(width=600, height=600)
screen.title("Cross the bridge as fast as you can, the treasure is around the corner")
screen.tracer(0)
border = Border()
player = Player()
screen.listen()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.onkey(player.go_up, "Up")
border.draw_bridge()
border.draw_safeline()
border.draw_safezone()
game_is_on = True
speed = 0.1
nth_time = 6
while game_is_on:

    time.sleep(speed)
    screen.update()

    car_manager.generate_cars(nth_time)
    car_manager.move_car()
    # detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 15:
            game_is_on = False
            player.game_over()
            car_manager.reset_speed()
    # detect when the turtle reach the finishing line
    if player.ycor() > 250:
        player.goto(0, -280)
        nth_time -= 1
        speed *= 0.8
        scoreboard.level_display()

screen.exitonclick()