"""Maze, move from one side to another.

Excercises

1. Keep score by counting taps.
2. Make the maze harder.
3. Generate the same maze twice.

"""

from turtle import *
from random import random
from freegames import line

a = 0

def draw():
    "Draw maze."
    color('black')
    width(1)

    for x in range(-200, 200, 40):
        for y in range(-200, 200, 40):
            if random() > 0.5:
                line(x, y, x + 40, y + 40)
            else:
                line(x, y + 40, x + 40, y)

    update()

def tap(x, y):
    global a
    "Draw line and dot for screen tap."
    if abs(x) > 198 or abs(y) > 198:
        a = 0
        up()
    else:
        down()

    width(2)
    color('red')
    goto(x, y)
    dot(4)

    a = a + 1
    print("move:" + str(a))

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
draw()
onscreenclick(tap)
done()
