import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



def populate_names():
    print("Populating names")
is_correct = True
while is_correct:
    answer_state = screen.textinput(title="Guess the state", prompt="What's another state name?")
    print(answer_state)



turtle.mainloop()
