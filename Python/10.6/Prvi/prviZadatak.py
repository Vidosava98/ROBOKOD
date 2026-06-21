
import turtle as t

t.pencolor("blue")

for i in range(4):
    print(i)
    t.forward(100)
    t.left(90)

t.penup()
t.goto(25, 25)
t.pendown()

t.pencolor("red")

for i in range(3):
    t.forward(50)
    t.left(120)

