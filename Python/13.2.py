import turtle
import random

# Podesavanje ekrana
ekran = turtle.Screen()
ekran.bgcolor("lightblue")
ekran.title("Kretanje izmedju krugova")

# Crtanje prepreka
prepreke = []

for i in range(6):
    krug = turtle.Turtle()
    krug.penup()
    krug.shape("circle")
    krug.color("red")
    krug.goto(random.randint(-250, 250), random.randint(-200, 200))
    prepreke.append(krug)

# Kreiranje igraca
igrac = turtle.Turtle()
igrac.penup()
igrac.shape("circle")
igrac.color("green")
igrac.goto(0, 0)

# Funkcija za proveru sudara
def sudar(nova_x, nova_y):
    for prepreka in prepreke:
        if prepreka.distance(nova_x, nova_y) < 40:
            return True
    return False

# Funkcije za kretanje
def gore():
    nova_y = igrac.ycor() + 20
    if not sudar(igrac.xcor(), nova_y):
        igrac.sety(nova_y)

def dole():
    nova_y = igrac.ycor() - 20
    if not sudar(igrac.xcor(), nova_y):
        igrac.sety(nova_y)

def levo():
    nova_x = igrac.xcor() - 20
    if not sudar(nova_x, igrac.ycor()):
        igrac.setx(nova_x)

def desno():
    nova_x = igrac.xcor() + 20
    if not sudar(nova_x, igrac.ycor()):
        igrac.setx(nova_x)

# Povezivanje tastature
ekran.listen()
ekran.onkey(gore, "Up")
ekran.onkey(dole, "Down")
ekran.onkey(levo, "Left")
ekran.onkey(desno, "Right")

turtle.done()
