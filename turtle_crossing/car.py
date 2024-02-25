from turtle import Turtle
import random

COLOR_LIST = [(153, 83, 40), (18, 27, 52), (49, 16, 32), (212, 155, 76), (65, 33, 18), (55, 93, 152), (25, 49, 37),
              (110, 166, 207), (227, 214, 101), (240, 237, 213), (170, 144, 58), (40, 45, 126), (126, 37, 23),
              (135, 64, 109), (110, 34, 75), (196, 222, 239), (80, 75, 27), (64, 110, 78), (88, 111, 195),
              (123, 184, 146)]


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("blue")
        self.setheading(180)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.random_position()
        self.random_color()


    def move(self):
        speed = random.randint(5, 10)
        self.forward(speed)

    def reset_position(self):
        new_y = random.randrange(-240, 270, 30)
        self.goto(300, new_y)
        self.random_color()

    def random_position(self):
        new_y = random.randrange(-240, 270, 30)
        new_x = random.randint(-300, 300)
        self.goto(y=new_y, x=new_x)

    def random_color(self):
        new_color = random.choice(COLOR_LIST)
        self.color(new_color)
