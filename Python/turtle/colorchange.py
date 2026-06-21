import turtle
import random

# Ekran
screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width=400, height=400)
screen.title("Kvadrat Igra")

# Kvadrat
square = turtle.Turtle()
square.shape("square")
square.color("cyan")
square.penup()
square.speed(0)

# Kretanje
def move_left():
    x = square.xcor() - 20
    if x < -180:
        x = -180
    square.setx(x)

def move_right():
    x = square.xcor() + 20
    if x > 170:
        x = 170
    square.setx(x)

def move_up():
    y = square.ycor() + 20
    if y > 180:
        y = 180
    square.sety(y)

def move_down():
    y = square.ycor() - 20
    if y < -170:
        y = -170
    square.sety(y)

def change_color():
    colors = ["red", "green", "blue", "yellow", "purple", "orange"]
    square.color(random.choice(colors))

# Kontrole
screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(change_color, "space")

turtle.done()
