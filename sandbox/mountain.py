"""Copying Andrew's Mountain Rng."""

from turtle import Turtle, done, colormode, tracer, update, TurtleScreen, Screen
from random import randint, random
import numpy as np


def main():
    boris: Turtle = Turtle()
    tracer(0, 0)
    colormode(255)
    screen_color(boris)
    screen: TurtleScreen = Screen()
    star(boris, 500)
    mountain(boris, -200, -150, 15)
    mountain(boris, 0, -150, 15)
    mountain(boris, -300, -150, 15)
    mountain(boris, -360, -150, 15)
    mountain(boris, 100, -150, 15)
    mountain(boris, -650, -150, 15)
    grass(boris, -150)
    update()
    done()


def move(turtle, x, y):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.setheading(0)


def screen_color(turtle):
    move(turtle, -400, -400)
    turtle.color(0, 0, 40)
    turtle.begin_fill()
    for i in range(0, 4):
        turtle.fd(800)
        turtle.left(90)
    turtle.end_fill()


def grass(turtle, y):
    move(turtle, -400, y)
    turtle.color("green")
    turtle.begin_fill()
    for i in range(0, 4):
        turtle.fd(800)
        turtle.right(90)
    turtle.end_fill()


def mountain(turtle, x, y, num_ridges):
    move(turtle, x, y)
    colors: list[tuple] = [(130, 110, 75), (100, 90, 75), (65, 60, 55), (90, 90, 80)]
    turtle.color((0, 0, 0), (colors[randint(0, len(colors) - 1)]))
    min_length = 10
    max_length = 40
    turtle.begin_fill()
    up_slope(turtle, min_length, max_length, num_ridges)
    down_slope(turtle, min_length, max_length, y)
    turtle.goto(x, y)
    turtle.end_fill()


def up_slope(turtle, min_length, max_length, num_ridges):
    for i in range(0, num_ridges):
        # multiplier: float = 1 / randint(1, 10)
        current_length: int = randint(min_length, max_length)
        turtle.setheading(randint(-10, 80)) # 30 + i * 5))
        turtle.fd(current_length)
        # turtle.setheading(randint(-70, -30))
        # turtle.fd(current_length * multiplier)


def down_slope(turtle, min_length, max_length, y):
    while turtle.ycor() > y:
        # multiplier: float = 1 / randint(2, 10)
        current_length: int = randint(min_length, max_length)
        turtle.setheading(randint(-80, 10))
        turtle.fd(current_length)
        # turtle.setheading(randint(30, 70))
        # turtle.fd(current_length * multiplier)


def star(turtle, amount):
    turtle.color("white")
    for i in range(0, amount):
        turtle.color(randint(200, 255), randint(200, 255), randint(160, 255))
        x = randint(-360, 360)
        y = (((2 * random()) ** 2) * randint(-75, 50)) + 150
        move(turtle, x, y)
        turtle.dot(randint(1, 4))


def tree(turtle, x, y):
    move(turtle, x, y)

    # Draws trunk

    turtle.begin_fill()
    for i in range(0, 2):
        turtle.fd(8)
        turtle.left(90)
        turtle.fd(50)
        turtle.left(90)
    turtle.end_fill()

    # Draws leaves
    


if __name__ == "__main__":
    main()