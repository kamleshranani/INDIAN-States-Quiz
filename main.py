import turtle
import pandas

FONT = ("Calibiri", 8, 'normal')
TOTAL_STATES = 29

screen = turtle.Screen()
screen.title("INDIAN States Game")
screen.setup(height=700, width=600)

image = "INDIAmap.gif"
screen.addshape(image)
turtle.shape(image)

guessed_state = []
missed_state = []

data = pandas.read_csv("states_data.csv")

while len(guessed_state) < 30:
    state = screen.textinput(title=f"{len(guessed_state)}/{TOTAL_STATES} Correct",
                             prompt="What's another state's name?").title()
    print(state)
    all_states = data["state"].to_list()
    print(state in all_states)

    if state == 'Exit':
        missed_state = [states for states in all_states if states not in guessed_state]
        # for states in all_states:
        #     if states not in guessed_state:
        #         missed_state.append(states)
        missed_state_data = pandas.DataFrame(missed_state)
        missed_state_data.to_csv("states_you_missed.csv")
        break

    if state in all_states and state not in guessed_state:
        guessed_state.append(state)
        state_data = data[data.state == state]
        x = int(state_data.x)
        y = int(state_data.y)
        print(x, y)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x, y)
        t.write(arg=state, align="center", font=FONT)


# # Code to Check Cordinates
# cord = []
# def printcord(x, y):
#     print(x,y)
#     cord.append((x,y))
#     print(cord)
# turtle.onscreenclick(printcord)
# turtle.mainloop()
