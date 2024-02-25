from turtle import Turtle


class Chicken(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.reset_position()
        self.setheading(90)

    def move(self):
        self.forward(30)

    def reset_position(self):
        self.goto(40, -275)
