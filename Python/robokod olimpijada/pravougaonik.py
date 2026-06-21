import turtle

t = turtle.Turtle()

t.pencolor("red")
t.fillcolor("blue")

t.begin_fill()

for i in range(2):
    t.forward(300)
    t.left(90)
    t.forward(150)
    t.left(90)

t.end_fill()

turtle.done()
