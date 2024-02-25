from turtle import Turtle
ALIGNMENT = "center"
STYLE = ("Arial", 30, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        # self.color("white")
        self.penup()
        self.goto(-220, 250)
        self.hideturtle()
        self.write(f"Level {self.level} ", align=ALIGNMENT, font=STYLE)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align=ALIGNMENT, font=STYLE)

    def update_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level {self.level} ", align=ALIGNMENT, font=STYLE)