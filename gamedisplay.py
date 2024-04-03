from turtle import Turtle

class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.pensize(15)
        self.penup()
        self.hideturtle()

    def draw_bridge(self):
        self.setheading(90)
        self.goto(-20,-250)
        for _ in range(17):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(10)

        self.goto(20,-250)
        for _ in range(17):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(10)

    def draw_safeline(self):
        self.pensize(2)
        self.goto(20, -250)
        self.setheading(180)
        self.pendown()
        self.forward(40)
        self.penup()


        self.goto(20, 250)
        self.pendown()
        self.forward(40)
        self.penup()
    def draw_safezone(self):
        # safezone on the south
        self.goto(-40,-280)
        self.pendown()
        self.setheading(90)
        self.forward(30)
        self.setheading(0)
        self.forward(20)
        self.penup()
        self.forward(40)
        self.pendown()
        self.forward(20)
        self.setheading(270)
        self.forward(30)
        self.penup()
        # safezone on the north
        self.goto(-40, 280)
        self.pendown()
        self.setheading(270)
        self.forward(30)
        self.setheading(0)
        self.forward(20)
        self.penup()
        self.forward(40)
        self.pendown()
        self.forward(20)
        self.setheading(90)
        self.forward(30)
        self.penup()