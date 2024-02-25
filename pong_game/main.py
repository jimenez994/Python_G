from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_l = Paddle(-350, 0)
paddle_r = Paddle(350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
# right Paddle
screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")

# left paddle
screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect right paddle miss
    if ball.xcor() > 380:
        scoreboard.update_score('right')
        ball.bounce_x()
        ball.reset_positon()

    # Detect left paddle miss
    if ball.xcor() < -380:
        scoreboard.update_score('left')
        ball.bounce_x()
        ball.reset_positon()
screen.exitonclick()
