COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
import random
from turtle import Turtle


class CarManager():
    def __init__(self):
       self.all_cars = []

    def generate_cars(self, nth_time):
        random_chance = random.randint(1,nth_time)
        if random_chance == 1:
            new_car = Turtle(shape="circle")

            new_car.shapesize(stretch_wid=1,stretch_len=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randrange(-240,240,5)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)



    def move_car(self):
        for car in self.all_cars:
            car.forward(-10)

    def reset_speed(self):
        self.car_speed = 0.1




