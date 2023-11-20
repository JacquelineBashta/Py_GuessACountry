from turtle import Screen
import turtle
import pandas as pd

all_countries = []


def get_mouse_click_coor(x, y):

    global all_countries

    country = screen.textinput(title="input", prompt="which country?")
    if country == "OFF":
        print(all_countries)
        df = pd.DataFrame(all_countries, columns=['item', "x", "y"])
        df.to_csv("Asia.csv")
    else:
        t.goto(x, y)
        t.write(country)
        all_countries.append([country, x, y])


screen = Screen()
screen.bgpic("blank_Asia.png")
screen.title("Asia Game")
screen.setup(width=700, height=500)
t = turtle.Turtle()
t.penup()
t.hideturtle()

df = pd.read_csv("asia_countries.csv")


screen.listen()
screen.onscreenclick(get_mouse_click_coor)
