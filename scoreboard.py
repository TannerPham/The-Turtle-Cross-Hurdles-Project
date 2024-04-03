FONT = ("Courier", 20, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()
        self.goto(-230, 260)
        self.level_update()



    def level_update(self):
        self.write(arg=f"Level: {self.level}",align="center",font = FONT)


    def level_display(self):
        self.clear()
        self.level += 1
        self.level_update()