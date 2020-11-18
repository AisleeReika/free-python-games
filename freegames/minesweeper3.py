"""Minesweeper

Exercises

1. What does the `seed(0)` function call do?
2. Change the number of bombs on the grid.
3. Change the size of the grid.

"""

from random import randrange, seed
from turtle import *
from freegames import floor, square
import sys
a = 50
seed(0)
bombs = {}
shown = {}
counts = {}


def initialize():
    global a
    "Initialize `bombs`, `counts`, and `shown` grids."
    for x in range(-250, 250, 50):
        for y in range(-250, 250, 50):
            bombs[x, y] = False
            shown[x, y] = False
            counts[x, y] = -1

    for count in range(8):
        x = randrange(-200, 200, 50)
        y = randrange(-200, 200, 50)
        bombs[x, y] = True

    for x in range(-200, 200, 50):
        for y in range(-200, 200, 50):
            total = 0
            for i in (-50, 0, 50):
                for j in (-50, 0, 50):

                    total += bombs[x + i, y + j]
            counts[x, y] = total


def stamp(x, y, text):
    "Display `text` at coordinates `x` and `y`."
    square(x, y, 50, 'white')
    color('red')
    write(text, font=('Arial', 50, 'normal'))


def draw():
    "Draw the initial board grid."
    for x in range(-200, 200, 50):
        for y in range(-200, 200, 50):
            stamp(x, y, '?')


def end():
    global a
    "Draw the bombs as X's on the grid."
    for x in range(-200, 200, 50):
        for y in range(-200, 200, 50):
            if bombs[x, y]:
                stamp(x, y, 'X')



def tap(x, y):
    global a
    "Respond to screen click at `x` and `y` coordinates."
    x = floor(x, 50)
    y = floor(y, 50)
    a = a - 1
    print("move:" + str(a))
    if a == 0:
        print("gameover")
        sys.exit()



    if bombs[x, y]:
        end()

        return
    pairs = [(x, y)]

    while pairs:
        x, y = pairs.pop()
        stamp(x, y, counts[x, y])
        shown[x, y] = True

        if counts[x, y] == 0:
            for i in (-50, 0, 50):
                for j in (-50, 0, 50):
                    pair = x + i, y + j
                    if not shown[pair]:
                        pairs.append(pair)



setup(420, 420, 370, 0)
hideturtle()
tracer(False)
initialize()
draw()
onscreenclick(tap)
done()
