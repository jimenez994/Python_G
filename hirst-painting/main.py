# import colorgram
from turtle import Turtle, Screen
import random
my_screen = Screen()
my_screen.colormode(255)
# colors = colorgram.extract('pic_colorful.png', 20)
# first_color = colors[0]
# rgb_colors= []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

color_list = [(153, 83, 40), (18, 27, 52), (49, 16, 32), (212, 155, 76), (65, 33, 18), (55, 93, 152), (25, 49, 37),
              (110, 166, 207), (227, 214, 101), (240, 237, 213), (170, 144, 58), (40, 45, 126), (126, 37, 23),
              (135, 64, 109), (110, 34, 75), (196, 222, 239), (80, 75, 27), (64, 110, 78), (88, 111, 195),
              (123, 184, 146)]
dash = Turtle()
dash.hideturtle()
dash.speed("fastest")
x_axis = -300
y_axis = 300

for i in range(10):
    dash.teleport(x_axis, y_axis)
    for _ in range(10):
        color = random.choice(color_list)
        dash.pendown()
        dash.dot(20, color)
        dash.penup()
        dash.forward(50)
    y_axis -= 50

my_screen.exitonclick()
