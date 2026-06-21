import turtle

t = turtle.Turtle()

t.fillcolor("red")
t.pencolor("blue")

t.begin_fill()

for i in range(3):
    t.forward(100)
    t.left(120)

t.end_fill()

turtle.done()
