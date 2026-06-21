import turtle

t = turtle.Turtle()
t.color("yellow")

# prvi krug
t.penup()
#t.goto(-120, 0)
t.pendown()
t.circle(100)

# drugi krug (ne dodiruje prvi)
t.penup()
t.goto(150, 50)
t.pendown()
t.circle(50)

turtle.done()
