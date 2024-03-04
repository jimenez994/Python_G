import turtle
import pandas
from state import State
from turtle import Turtle, Screen

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.tracer(0)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data['state']
x_cors = data['x']
y_cors = data['y']


def populate_names():
    for i in range(len(data['state'])):
        State(states[i], x_cors[i], y_cors[i])
        # print(f"State: {state}, Coordinates: ({x}, {y})")


# populate_names()
screen.update()
guessed_states = []
missing_states = []

is_correct = True
while is_correct:
    input_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                   prompt="What's another state name?").strip().capitalize()
    # exit amd save missed states
    if input_state == "Exit":
        for state in states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        is_correct = False

    if input_state in data['state'].values:
        if input_state in guessed_states:
            print("state already guessed")
        else:
            guessed_states.append(input_state)
            # If the state exists, get its coordinates
            state_row = data[data['state'] == input_state]
            state_x = state_row['x'].iloc[0]
            state_y = state_row['y'].iloc[0]
            State(input_state, state_x, state_y)
    else:
        print("State not found.")


