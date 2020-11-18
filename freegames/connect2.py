"""Connect Four

Exercises

1. Change the colors.
2. Draw squares instead of circles for open spaces.
3. Add logic to detect a full row.
4. Create a random computer player.
5. How would you detect a winner?

"""

from turtle import *
from freegames import line
a = 0
b = 0
c = 0
turns = {'red': 'yellow', 'yellow': 'red'}
state = {'player': 'yellow', 'rows': [0] * 8}

def grid():
    "Draw Connect Four grid."
    bgcolor('blue')

    for x in range(-150, 200, 50):
        line(x, -200, x, 200)

    for x in range(-175, 200, 50):
        for y in range(-175, 200, 50):
            up()
            goto(x, y)
            dot(40, 'white')

    update()

def tap(x, y):
    global a, b, c
    "Draw red or yellow circle in tapped row."
    player = state['player']
    rows = state['rows']

    c = c + 1

    row = int((x + 200) // 50)
    count = rows[row]

    x = ((x + 200) // 50) * 50 - 200 + 25
    y = count * 50 - 200 + 25

    up()
    goto(x, y)
    dot(40, player)
    update()

    if c % 2 == 0:
        a = a + 1
        print("player02 move:" + str(a))
    else:
        b = b + 1
        print("player01 move:" + str(b))



    rows[row] = count + 1
    state['player'] = turns[player]

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
onscreenclick(tap)
done()
