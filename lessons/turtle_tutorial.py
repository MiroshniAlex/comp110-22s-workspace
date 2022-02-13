"""Turtle Tutorial."""

from turtle import Turtle, colormode, done

leo: Turtle = Turtle()
bob: Turtle = Turtle()

# leo.hideturtle()
# bob.hideturtle()
leo.penup()
bob.penup()
leo.goto(-200, -150)
bob.goto(-200, -150)
leo.pendown()
bob.pendown()

bob.speed(50)

colormode(255)

bob.color(32, 67, 93)
# leo.fillcolor(32,67,93)
leo.color("green", "yellow")

# leo.begin_fill()

side_length: float = 400

i: int = 0
while i < 3:
    leo.forward(side_length)
    leo.left(120)
    i += 1

# leo.end_fill()

i = 0
while i < 200:
    bob.forward(side_length)
    if i // 20 == 0:
        bob.left(120.5)
    elif i // 30 <= 1:
        bob.left(119.5)
    else: 
        bob.left(120.5)
    side_length *= .97
    i += 1

done()