import random
from turtle import Turtle, Screen
from random import randint

my_pet = Turtle()
my_pet.shape("turtle")
my_pet.color("red", "blue")

my_screen = Screen()
my_screen.colormode(255)

my_pet.speed("fastest")
def random_color():
    color = randint(0, 255), randint(0, 255), randint(0, 255)
    return color


def make_shape(sides, color):
    my_pet.pencolor(color)
    right = 360 / sides
    for _ in range(sides):
        my_pet.forward(100)
        my_pet.right(right)


def make_shapes():
    for sides in range(10):
        make_shape(3 + sides, random_color())


# make_shapes()


def random_moves(steps):
    turns = ["left", "right", "back"]
    my_pet.pensize(15)
    my_pet.forward(40)
    while steps > 0:
        my_pet.pencolor(random_color())
        random_turn = random.choice(turns)
        if random_turn == "left":
            my_pet.left(90)
        elif random_turn == "back":
            my_pet.right(180)
        else:
            my_pet.right(90)
        my_pet.forward(40)
        steps -= 1


# random_moves(140)

loop = 0
while loop < 360:
    my_pet.pencolor(random_color())
    my_pet.circle(100)
    my_pet.right(5)
    loop += 5



# for _ in range(15):
#     my_pet.penup()
#     my_pet.forward(10)
#     my_pet.pendown()
#     my_pet.forward(10)


my_screen.exitonclick()
