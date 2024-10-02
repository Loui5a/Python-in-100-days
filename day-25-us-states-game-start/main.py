import turtle
import pandas

# create the screen with the image of America:
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(width=725, height=491)
turtle.shape(image)

# read and process data using pandas:
data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
# create an empty list to save the guessed states
guessed_states = []
# have the process looped until all states are guessed or the user types "exit"
while len(guessed_states) < 50:
    # add a pop-up text box with the number of correctly guessed states as title.
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state.lower() == "exit":
        missing_states = [state for state in states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in states:
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
        correct_state = data[data["state"] == answer_state]
        # create a turtle to move to the right coordinates and write the name of the state.
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(correct_state["x"].item(), correct_state["y"].item())
        t.write(answer_state)

