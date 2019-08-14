import turtle
import random

turtle.Screen().setup(width=640, height=640)
turtle.bgcolor('orange')



GRID_SIZE = 80
GRID_SPAN = 3
GRID_MAX  = GRID_SIZE * GRID_SPAN
MOVE_PROBABILITY = .1

def line(x1, y1, x2, y2):
    turtle.up()
    turtle.goto(x1,y1)
    turtle.down()
    turtle.goto(x2,y2)

turtle.speed(0)
turtle.hideturtle()
turtle.color('dark orange')
turtle.width(15)

for i in range(-GRID_SPAN,GRID_SPAN+1):
    scaled_i = i * GRID_SIZE
    line(-GRID_MAX,scaled_i,GRID_MAX,scaled_i)
    line(scaled_i,-GRID_MAX,scaled_i,GRID_MAX)


def actors(file):
    actor = turtle.Turtle()
    #change shape
    if file.endswith( '.gif'):
        turtle.register_shape(file)
        actor.shape(file)
    else:
        actor.shape(file)
    actor.up()
    return actor


achilles = actors('./data/Walk.gif')
tortoise = actors('turtle')
qi = actors('circle')
qi.goto(0,GRID_MAX+42)

def catchup():
    if achilles.position() == tortoise.position():
        update_qi(100)
        tortoise.circle(50, steps=20)
        move_tortoise()
    else:
        update_qi(-20)
        if random.random() < MOVE_PROBABILITY:
            move_tortoise()

def update_qi(d_qi):
    qi.forward(d_qi)
    qi_x, _ = qi.position()
    if qi_x >= GRID_MAX:
        end_game('Victory')
    if qi_x <= -GRID_MAX:
        end_game('Defeat')

def end_game(message):
    achilles.write(message, align='center', font=('Helvetia', 64, 'bold'))
    for key in ('Up', 'Down', 'Left', 'Right'):
        turtle.onkey(None,key)


def move_achilles_up():
    x, y = achilles.position()
    if y < GRID_MAX:
        achilles.goto(x + 0 * GRID_SIZE , y + 1 * GRID_SIZE)
    catchup()

def move_achilles_down():
    x, y = achilles.position()
    achilles.goto(x + 0 * GRID_SIZE , y + -1 * GRID_SIZE)
    catchup()

def move_achilles_left():
    x, y = achilles.position()
    achilles.goto(x + -1 * GRID_SIZE , y + 0 * GRID_SIZE)
    catchup()

def move_achilles_right():
    x, y = achilles.position()
    achilles.goto(x + 1 * GRID_SIZE , y + 0 * GRID_SIZE)
    catchup()

def move_tortoise():
    x = random.randint(-GRID_SPAN, GRID_SPAN)
    y = random.randint(-GRID_SPAN, GRID_SPAN)
    tortoise.goto(x * GRID_SIZE, y * GRID_SIZE)


move_tortoise()

turtle.listen()

turtle.onkey(move_achilles_up, 'Up')
turtle.onkey(move_achilles_down, 'Down')
turtle.onkey(move_achilles_left, 'Left')
turtle.onkey(move_achilles_right, 'Right')

turtle.mainloop()

