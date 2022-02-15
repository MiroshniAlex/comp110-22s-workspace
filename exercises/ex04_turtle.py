"""A fine masterpeice."""

__author__ = "730477260"

from turtle import Turtle, done, colormode, Screen, TurtleScreen, tracer, update
from random import randint


def main() -> None:
    """You enter a magic store."""
    timmy: Turtle = Turtle()
    timmy.speed(0)
    # sets background color for the screen
    screen: TurtleScreen = Screen()
    screen.screensize(500, 500, "cyan")
    colormode(255)
    tracer(0, 0)
    # builds objects
    floor(timmy)
    table(timmy, -300, -250)
    table(timmy, -70, -250)
    star(timmy, -200, 100)
    bookshelf(timmy, 157, -250, 6)
    table_potions(timmy, -317, -84, 8)
    table_potions(timmy, -87, -84, 8)
    table_potions(timmy, 158, 231, 6)
    update()
    done()


def move(turtle: Turtle, x: int, y: int) -> None:
    """Moves turtle to certain location."""
    turtle.up()
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.pd()


def floor(turtle: Turtle) -> None:
    """Makes a floor."""
    i: int = 0
    move(turtle, -500, -210)
    turtle.color("lightgrey")
    turtle.begin_fill()
    while i < 2:
        turtle.fd(1000)
        turtle.rt(90)
        turtle.fd(300)
        turtle.rt(90)
        i += 1
    turtle.end_fill()


def table(turtle: Turtle, x: int, y: int) -> None:
    """Builds a table."""
    move(turtle, x, y)
    turtle.color(132, 88, 21)
    table_leg(turtle)
    move(turtle, x + 150, y)
    table_leg(turtle)
    move(turtle, x - 20, y + 100)
    table_top(turtle)


def table_top(turtle: Turtle) -> None:
    """Builds table top."""
    turtle.begin_fill()
    i: int = 0
    while i < 2:
        turtle.fd(210)
        turtle.lt(90)
        turtle.fd(15)
        turtle.lt(90)
        i += 1
    turtle.end_fill()


def table_leg(turtle: Turtle) -> None:
    """Builds a rectangle table leg."""
    i: int = 0
    turtle.begin_fill()
    while i < 2:
        turtle.fd(20)
        turtle.lt(90)
        turtle.fd(100)
        turtle.lt(90)
        i += 1
    turtle.end_fill()


def bookshelf(turtle: Turtle, x: int, y: int, stack: int) -> None:
    """Builds a bookshelf."""
    i: int = 0
    move(turtle, x, y)
    shelf(turtle, stack)
    while i < stack:
        move(turtle, x + 11, y + 11 + (70 * i))
        book_row(turtle)
        i += 1


def shelf(turtle: Turtle, stack: int) -> None:
    """Draws as many shelfs as I could want for a bookshelf."""
    n: int = 0
    i: int = 0
    w: int = 0
    turtle.color(82, 66, 11)
    # This while loop makes a darker brown rectangle for back of bookshelf.
    turtle.begin_fill()
    while n < 2:
        turtle.fd(150)
        turtle.lt(90)
        turtle.fd(70 * stack)
        turtle.lt(90)
        n += 1
    turtle.end_fill()
    # This while loop makes the individual shelfs.
    turtle.color(132, 88, 21)
    while i < stack:
        turtle.begin_fill()
        turtle.fd(150)
        turtle.lt(90)
        turtle.fd(70)
        turtle.lt(90)
        turtle.fd(10)
        turtle.lt(90)
        turtle.fd(60)
        turtle.rt(90)
        turtle.fd(130)
        turtle.rt(90)
        turtle.fd(60)
        turtle.lt(90)
        turtle.fd(10)
        turtle.lt(90)
        turtle.fd(70)
        turtle.end_fill()
        turtle.setheading(90)
        turtle.fd(70)
        turtle.setheading(0)
        i += 1
    # This while loop puts the final top on the bookshelf
    turtle.begin_fill()
    while w < 2:
        turtle.fd(150)
        turtle.lt(90)
        turtle.fd(10)
        turtle.lt(90)
        w += 1
    turtle.end_fill()


def book(turtle: Turtle) -> None:
    """Draws a signle book."""
    i: int = 0
    height: int = randint(40, 58)
    turtle.begin_fill()
    while i < 2:
        turtle.fd(10)
        turtle.lt(90)
        turtle.fd(height)
        turtle.lt(90)
        i += 1
    turtle.end_fill()
    turtle.fd(11)


def book_row(turtle: Turtle) -> None:
    """This creates a random assortment of books on a signle shelf."""
    colors: list[str] = ["blue", "red", "green", "orange", "pink", "yellow", "cyan", "lightgreen", "grey", "skyblue", "salmon", "crimson", "maroon", "black", "turquoise", "lightgrey", "gold", "silver", "magenta", "yellowgreen", "lime", "olive", "tan", "violet", "navy", "indigo", "lavender", "purple"]
    i: int = 0
    while i < 12:
        if randint(0, 1) == 1:
            turtle.color(colors[randint(0, len(colors) - 1)])
            book(turtle)
        else:
            turtle.up()
            turtle.fd(10)
            turtle.pd()
        i += 1


def star(turtle: Turtle, x: int, y: int) -> None:
    """Creates a cool star for decor."""
    i: int = 0
    move(turtle, x, y)
    turtle.color("crimson", "gold")
    turtle.begin_fill()
    turtle.fd(200)
    turtle.lt(170)
    while i < 36:
        turtle.fd(200)
        turtle.lt(170)
        i += 1
    turtle.end_fill()


def potion1(turtle: Turtle) -> None:
    """Erlenmeyer flask."""
    turtle.up()
    turtle.fd(10)
    turtle.down()
    # Starts drawing.
    turtle.begin_fill()
    turtle.fd(5)
    turtle.right(90)
    turtle.fd(25)
    turtle.left(20)
    turtle.fd(27.5)
    turtle.right(110)
    turtle.fd(25)
    turtle.right(110)
    turtle.fd(27.5)
    turtle.left(20)
    turtle.fd(25)
    turtle.rt(90)
    turtle.end_fill()
    # Ends Drawing
    turtle.up()
    turtle.fd(16)
    turtle.pd()


def potion2(turtle: Turtle) -> None:
    """Test tube."""
    turtle.up()
    turtle.fd(9)
    turtle.pd()
    # Starts drawing
    turtle.begin_fill()
    turtle.setheading(270)
    turtle.fd(47)
    turtle.circle(3, 180)
    turtle.fd(47)
    turtle.left(90)
    turtle.fd(6)
    turtle.end_fill()
    # Ends drawing
    turtle.setheading(0)
    turtle.up()
    turtle.fd(17)
    turtle.pd()


def potion3(turtle: Turtle) -> None:
    """Beaker."""
    turtle.up()
    turtle.fd(2)
    turtle.pd()
    # Begins drawing
    turtle.begin_fill()
    turtle.setheading(270)
    turtle.fd(47)
    turtle.circle(3, 90)
    turtle.fd(14)
    turtle.circle(3, 90)
    turtle.fd(47)
    turtle.left(90)
    turtle.fd(20)
    turtle.end_fill()
    # Ends drawing
    turtle.up()
    turtle.setheading(0)
    turtle.fd(24)
    turtle.pd()
    

def table_potions(turtle: Turtle, x: int, y: int, amount: int) -> None:
    """Puts random potions on a table."""
    i: int = 0
    rand: int
    move(turtle, x, y)
    colors: list[str] = ["blue", "red", "green", "orange", "lightgreen", "crimson", "turquoise", "gold", "silver", "magenta", "lime", "violet", "indigo", "lavender", "purple"]
    while i < amount:
        rand = randint(1, 6)
        turtle.color("black", colors[randint(0, len(colors) - 1)])
        if rand == 1:
            potion1(turtle)
        elif rand == 2:
            potion2(turtle)
        elif rand == 3:
            potion3(turtle)
        else:
            turtle.up()
            turtle.fd(26)
            turtle.pd()
        i += 1


if __name__ == "__main__":
    main()