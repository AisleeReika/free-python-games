"""Ant, simple animation demo.

Exercises

1. Wrap ant around screen boundaries.
2. Make the ant leave a trail.
3. Change the ant color based on position.
   Hint: colormode(255); color(0, 100, 200)

"""

from random import *
from turtle import *
from freegames import vector
a = 0
ant = vector(0, 0)
aim = vector(2, 0)

def wrap(value):
    "Wrap value around -200 and 200."
    return value  # TODO

def draw():
    global a
    "Move ant and draw screen."
    pencolor("red")
    ant.move(aim)
    ant.x = wrap(ant.x)
    ant.y = wrap(ant.y)

    aim.move(random() - 0.5)
    aim.rotate(random() * 10 - 5)

    pencolor("green")
    clear()

    goto(ant.x, ant.y)
    dot(4)
    a = a + 1
    print("step:" + str(a))
    if running:
        ontimer(draw, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
up()
running = True
draw()
done()
