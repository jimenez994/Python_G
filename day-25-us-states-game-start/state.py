from turtle import Turtle
ALIGNMENT = "center"
STYLE = ("Arial", 10, "normal")


class State(Turtle):
    def __init__(self, state, x, y):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(x, y)
        self.hideturtle()
        self.write(f"{state}", align=ALIGNMENT, font=STYLE)

