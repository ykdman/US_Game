import turtle
import pandas
# Start
IMAGE = "blank_states_img.gif"
# Screen Setting
player = turtle.Turtle()
player.penup()
player.hideturtle()

screen = turtle.Screen()  # Build Screen
screen.title("US States Game")

screen.addshape(IMAGE)  # Add Tutle Screen Shape/ img FIle

turtle.penup()
turtle.shape(IMAGE)



# Read CSV Data From "50_states.csv"
data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()

guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States correct",
                                    prompt="Another state's name?").title()  # First Chr To upper

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_lean.csv")
        break

    if answer_state in all_states:
        guessed_state.append(answer_state)  # append right answer
        # turtle setting to write
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        # get coordinate of state
        state_data = data[data["state"] == answer_state]
        t.goto(int(state_data["x"]), int(state_data["y"]))
        t.write(state_data["state"].item())  # Get Only value of row


# # when game end, User couldn't Right Answer Data Stacking to CSV / 내방법
# #
# for answer in guessed_state:
#     data.drop(data.index[(data["state"] == answer)], axis=0, inplace=True)
#
# save_data = data
# save_data.to_csv("statesaa_to_learn.csv")


#  Keeping Screen Open after Code Running
turtle.exitonclick()



