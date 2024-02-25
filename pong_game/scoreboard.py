from turtle import Turtle
ALIGNMENT = "center"
STYLE = ("Arial", 80, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_r = 0
        self.score_l = 0
        self.color("white")
        self.penup()
        self.goto(0, 200)
        self.hideturtle()
        self.write(f"{self.score_l} : {self.score_r}", align=ALIGNMENT, font=STYLE)

    def update_score(self, side):
        if side == "right":
            self.score_r += 1
        else:
            self.score_l += 1
        self.clear()
        self.write(f"{self.score_l} : {self.score_r}", align=ALIGNMENT, font=STYLE)



