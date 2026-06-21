import turtle
import random


screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Veselo uskršnje jaje 🥚")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()


def draw_egg(x, y, width, height, color):
    t.penup()
    t.goto(x, y - height/2)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.setheading(0)
    for i in range(2):
        t.circle(width/2, 90)
        t.circle(height/2, 90)
    t.end_fill()

def draw_fun_dots(x, y, width, height, num_dots):
    colors = ["yellow", "red", "orange", "purple", "white", "green", "pink"]
    for _ in range(num_dots):
        t.penup()
        xpos = x - width/2 + random.randint(20, width-20)
        ypos = y - height/2 + random.randint(30, height-30)
        t.goto(xpos, ypos)
        t.dot(random.randint(10, 20), random.choice(colors))


positions = [(-150,0), (0,0), (150,0)]

egg_colors = ["pink", "yellow", "lightgreen"]

for pos, color in zip(positions, egg_colors):
    draw_egg(pos[0], pos[1], 80, 120, color)
    draw_fun_dots(pos[0], pos[1], 60, 100, 6)

turtle.done()
