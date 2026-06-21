import turtle

boje = ["red", "green", "blue"]

t = turtle.Turtle()

rad = [100, 80, 50]

for i in range(3):
    t.penup()
    t.goto(0, -rad[i])
    t.pendown()
    t.fillcolor(boje[i])
    t.begin_fill()
    t.circle(rad[i])
    t.end_fill()

turtle.done()
