import turtle
import random

t = turtle.Turtle()

a = float(input("Unesi duzinu stranice: "))

x = random.randint(-200, 200)
y = random.randint(-200, 200)

t.penup()
t.goto(x, y)
t.pendown()

t.fillcolor("red")
t.pencolor("blue")

t.begin_fill()

for i in range(3):
    t.forward(a)
    t.left(120)

t.end_fill()

turtle.done()
