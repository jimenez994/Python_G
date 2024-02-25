from turtle import Screen
from chicken import Chicken
from car import Car
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Crossing Turtle")
screen.tracer(0)
screen.listen()
screen.colormode(255)

scoreboard = Scoreboard()
chicken = Chicken()
car_list = []

for _ in range(0, 10):
    car_list.append(Car())

screen.onkey(chicken.move, 'space')

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    for car in car_list:
        distance = car.distance(chicken)
        # Collition
        if distance < car.shapesize()[0]*19 + chicken.shapesize()[0]:
            scoreboard.game_over()
            game_is_on = False
        car.move()
        if car.xcor() < -300:
            car.reset_position()

    if chicken.ycor() > 280:
        chicken.reset_position()
        scoreboard.update_level()
        for _ in range(0, 2):
            car_list.append(Car())

screen.exitonclick()
