import turtle
import pandas as pd

screen = turtle.Screen()
which_conti = screen.textinput(
    prompt=" Which Continental you wana Play with?",
    title="Choose a Contenintal")

MAX_ANSWERS = 0
TUNE_X = 0

if which_conti == "America":
    screen.bgpic("blank_states.gif")
    screen.title("United States Game")
    screen.setup(width=700, height=500)
    data = pd.read_csv("50_states.csv")
    MAX_ANSWERS = data.shape[0]
    TUNE_X = -15

elif which_conti == "Asia":
    screen.bgpic("blank_Asia.png")
    screen.title("Asia Game")
    screen.setup(width=700, height=500)
    data = pd.read_csv("Asia.csv")
    MAX_ANSWERS = data.shape[0]
    TUNE_X = 0


t = turtle.Turtle()
t.penup()
t.hideturtle()

correct_answers_l = []


while len(correct_answers_l) < MAX_ANSWERS:
    usr_inp = screen.textinput(
        title=f" {len(correct_answers_l)}/{MAX_ANSWERS} Correct",
        prompt="What is another guess?")
    if usr_inp is not None:
        usr_inp = usr_inp.title()
        if usr_inp in data.item.values and \
                usr_inp.title() not in correct_answers_l:
            correct_answers_l.append(usr_inp)
            pos_x = data.query("item == @usr_inp.title() ").x + TUNE_X
            pos_y = data.query("item == @usr_inp.title()").y
            t.goto(int(pos_x), int(pos_y))
            t.write(usr_inp, align="left")
    else:
        break

if len(correct_answers_l) == MAX_ANSWERS:
    t.goto(0, 0)
    t.write("YOU Guessed it ALL!", align="center",
            font=("Courier", 35, "bold"))
else:
    missed_answers = set(data.item.to_list()) - set(correct_answers_l)
    with open(f"Missed Answers_{which_conti}.csv", mode="w") as f:
        for item in missed_answers:
            f.write(f"{item} \n")
screen.exitonclick()
