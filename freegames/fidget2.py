"""Fidget, inspired by fidget spinners.

Exercises

1. Change the spinner pattern.
2. Respond to mouse clicks.
3. Change its acceleration.
4. Make it go forwards and backwards.

"""

from turtle import *
a = 0
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
    global a
    "Flick fidget spinner."
    state['turn'] += 10
    a = a + 1
    print("turn:" + str(a))
def flick2():
    global a
    "Flick fidget spinner."
    state['turn'] += 20
    a = a + 2
    print("turn:" + str(a))

def flick3():
    global a
    "Flick fidget spinner."
    state['turn'] += 30
    a = a + 3
    print("turn:" + str(a))

def flick4():
    global a
    "Flick fidget spinner."
    state['turn'] += 40
    a = a + 4
    print("turn:" + str(a))


def flick5():
    global a
    "Flick fidget spinner."
    state['turn'] += 50
    a = a + 5
    print("turn:" + str(a))

def flick6():
    global a
    "Flick fidget spinner."
    state['turn'] += 60
    a = a + 6
    print("turn:" + str(a))

def flick7():
    global a
    "Flick fidget spinner."
    state['turn'] += 70
    a = a + 7
    print("turn:" + str(a))

def flick8():
    global a
    "Flick fidget spinner."
    state['turn'] += 80
    a = a + 8
    print("turn:" + str(a))

def flick9():
    global a
    "Flick fidget spinner."
    state['turn'] += 90
    a = a + 9
    print("turn:" + str(a))

def flick0():
    global a
    "Flick fidget spinner."
    state['turn'] += 100
    a = a + 10
    print("turn:" + str(a))


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
