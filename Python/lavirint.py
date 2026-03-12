import turtle

screen = turtle.Screen()
screen.setup(600, 600)

player = turtle.Turtle()
player.shape("turtle")
player.penup()
player.goto(-250, -250)

end = turtle.Turtle()
end.penup()
end.color("green")
end.goto(250, 250)
end.dot(20)

walls = [
    (-100, -280, 400, 20),  # donji zid
    (-200, -200, 20, 380),  # levi zid
    (180, -200, 20, 380),   # desni zid
    (-150, -200, 20, 250),
    (-150, 50, 250, 20),
    (50, 50, 20, 200),
    (-150, -50, 200, 20),
    (50, -50, 20, 150)
]

drawer = turtle.Turtle()
drawer.hideturtle()
drawer.speed(0)

for x, y, w, h in walls:
    drawer.penup()
    drawer.goto(x, y)
    drawer.pendown()
    drawer.begin_fill()
    for _ in range(2):
        drawer.forward(w)
        drawer.left(90)
        drawer.forward(h)
        drawer.left(90)
    drawer.end_fill()

def collide(x, y):
    for wx, wy, w, h in walls:
        if wx <= x <= wx + w and wy <= y <= wy + h:
            return True
    return False

def move(dx, dy):
    new_x = player.xcor() + dx
    new_y = player.ycor() + dy
    if not collide(new_x, new_y):
        player.goto(new_x, new_y)
    else:
        player.goto(-250, -250)
        print("Dodirnuo si zid! Pokušaj ponovo.")

def gore(): move(0, 20)
def dole(): move(0, -20)
def levo(): move(-20, 0)
def desno(): move(20, 0)

screen.listen()
screen.onkey(gore, "Up")
screen.onkey(dole, "Down")
screen.onkey(levo, "Left")
screen.onkey(desno, "Right")

screen.mainloop()
