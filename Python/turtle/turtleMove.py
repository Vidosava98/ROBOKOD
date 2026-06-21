import turtle
import random

screen = turtle.Screen()
screen.setup(600, 600)

player = turtle.Turtle()
player.shape("classic") #["arrow", "turtle", "circle", "square", "triangle", "classic"]
player.penup()
player.goto(-250, -250)

end = turtle.Turtle()
end.penup()
end.color("green")
end.goto(250, 250)
end.dot(20)

drawer = turtle.Turtle()
drawer.hideturtle()
drawer.speed(0)

levelNeprijatelja = input("Unesi level neprijatelja, unosom light, medium i strong kljucnih reci")
brojMina = 0

if levelNeprijatelja == "light":
    brojMina = 20
    poluprecnikMina = 10
elif levelNeprijatelja == "medium":
    brojMina = 30
    poluprecnikMina = 15
elif levelNeprijatelja == "strong":
    brojMina = 60
    poluprecnikMina = 20
else:
    brojMina = 15
    poluprecnikMina = 15

enemies = []

    
for i in range(brojMina):
    drawer.penup()
    drawer.fillcolor("red")
    x = random.randint(-250,250)
    y = random.randint(-250, 250)
    dimenzije = [x, y, poluprecnikMina, poluprecnikMina]
    enemies.append(dimenzije)
    drawer.goto(x,y)
    drawer.pendown()
    drawer.begin_fill()
    for _ in range(4):  # Crta kvadrat
        drawer.forward(poluprecnikMina)
        drawer.left(90)
    drawer.end_fill()

def collide(x, y):
    for wx, wy, w, h in enemies:
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
        print("Dodirnuo si krug! Pokušaj ponovo.")

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
