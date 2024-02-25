from turtle import Turtle, Screen
from random import randint
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: \n red, "
                                                          "orange, yellow, blue, purple")
colors = ["red", "orange", "yellow", "blue", "purple"]
y_axis = [100, 50, 0, -50, -100]
turtles = []
race_on = False

for index in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_axis[index])
    turtles.append(new_turtle)

if user_bet:
    race_on = True
while race_on:
    for turtle in turtles:
        random_step = randint(0, 10)
        turtle.forward(random_step)
        if turtle.xcor() > 230:
            race_on = False
            if user_bet == turtle.pencolor():
                print(f"Congrats you won! The {turtle.pencolor()} turtle won")
            else:
                print(f"You loss! The {turtle.pencolor()} turtle won")

screen.exitonclick()