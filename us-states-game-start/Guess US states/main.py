import turtle
import pandas

data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()
answered_states = []
missing_state = []
data_dict = data.to_dict()

print(state_list)
total_states = 50
guessed_ones = 0
screen = turtle.Screen()
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

screen.title("Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
while guessed_ones != 50:
    answer = screen.textinput(title=f"{guessed_ones}/{total_states} Correct Guess", prompt="Guess a state")
    answer = answer.title()
    if answer == "Exit":
        for state in state_list:
            if state not in answered_states:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")

        break
    for key in range(0, 50):
        if answer == data_dict['state'][key] and answer not in answered_states:
            answered_states.append(answer)
            guessed_ones += 1
            x_cor = data_dict['x'][key]
            y_cor = data_dict['y'][key]
            writer.goto(x_cor,y_cor)
            writer.write(f"{answer}")
            break


