import turtle
import random

turtle.Screen().setup(width=640, height= 640)
turtle.bgcolor('orange')

coin = turtle.Turtle()
coin.shape('circle')
coin.up()

STEPS = 80

def move_coin():
    x, y = coin.position()
    dx = random.randint(-3,3)
    dy = random.randint(-3,3)
    coin.goto(x + dx * STEPS, y + dy * STEPS)

move_coin()

player1 = turtle.Turtle()

def go_down():
    x,y = player1.position()
    player1.goto(x,y-STEPS)


def go_up():
    x,y = player1.position()
    player1.goto(x,y+STEPS)


def go_left():
    x,y = player1.position()
    player1.goto(x-STEPS,y)


def go_right():
    x,y = player1.position()
    player1.goto(x+STEPS,y)


turtle.listen()

turtle.onkey(go_down,'Down')
turtle.onkey(go_up,'Up')
turtle.onkey(go_left,'Left')
turtle.onkey(go_right,'Right')


turtle.mainloop()