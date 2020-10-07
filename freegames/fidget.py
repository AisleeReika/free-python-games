"""Fidget, inspired by fidget spinners.

Exercises

1. Change the spinner pattern.
2. Respond to mouse clicks.
3. Change its acceleration.
4. Make it go forwards and backwards.

"""

from turtle import *

state = {'turn': 0}

def spinner():
    "Draw fidget spinner."
    clear()
    angle = state['turn'] / 10
    right(angle)
    forward(100)
    dot(120, 'green')
    back(100)
    right(120)
    forward(100)
    dot(120, 'green')
    back(100)
    right(120)
    forward(100)
    dot(120, 'green')
    back(100)
    right(120)
    update()

def animate():
    "Animate fidget spinner."
    if state['turn'] > 0:
        state['turn'] -= 1

    spinner()
    ontimer(animate, 20)

def flick1():
    "Flick fidget spinner."
    state['turn'] += 10

def flick2():
    "Flick fidget spinner."
    state['turn'] += 20

def flick3():
    "Flick fidget spinner."
    state['turn'] += 30

def flick4():
    "Flick fidget spinner."
    state['turn'] += 40

def flick5():
    "Flick fidget spinner."
    state['turn'] += 50

def flick6():
    "Flick fidget spinner."
    state['turn'] += 60

def flick7():
    "Flick fidget spinner."
    state['turn'] += 70

def flick8():
    "Flick fidget spinner."
    state['turn'] += 80

def flick9():
    "Flick fidget spinner."
    state['turn'] += 90

def flick0():
    "Flick fidget spinner."
    state['turn'] += 100


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
width(20)
onkey(flick1, '1')
onkey(flick2, '2')
onkey(flick3, '3')
onkey(flick4, '4')
onkey(flick5, '5')
onkey(flick6, '6')
onkey(flick7, '7')
onkey(flick8, '8')
onkey(flick9, '9')
onkey(flick0, '0')
listen()
animate()
done()
