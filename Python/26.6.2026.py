import turtle
import random
import time

# ekran
prozor = turtle.Screen()
prozor.title("Moj grad nocu")
prozor.bgcolor("#001122")
prozor.setup(800,600)


crtac = turtle.Turtle()
crtac.speed(0)
crtac.hideturtle()


# crtanje pravougaonika
def pravougaonik(x,y,sirina,visina,boja):
    crtac.penup()
    crtac.goto(x,y)
    crtac.pendown()

    crtac.color(boja)
    crtac.begin_fill()

    for i in range(2):
        crtac.forward(sirina)
        crtac.left(90)
        crtac.forward(visina)
        crtac.left(90)

    crtac.end_fill()



# mesec
crtac.penup()
crtac.goto(250,180)
crtac.pendown()
crtac.color("yellow")
crtac.begin_fill()
crtac.circle(50)
crtac.end_fill()


# zvezde
crtac.color("white")

for i in range(60):
    x=random.randint(-380,380)
    y=random.randint(50,280)

    crtac.penup()
    crtac.goto(x,y)
    crtac.pendown()

    crtac.dot(3)



# zgrade

zgrade=[
    (-250,-200,100,300),
    (-100,-200,120,180),
    (70,-200,90,260),
    (220,-200,120,220)
]


for z in zgrade:
    pravougaonik(
        z[0],
        z[1],
        z[2],
        z[3],
        "gray"
    )



# prozori

for z in zgrade:

    x=z[0]
    y=z[1]
    sirina=z[2]
    visina=z[3]


    for i in range(3):

        for j in range(visina//50):

            crtac.penup()
            crtac.goto(
                x+20+i*25,
                y+30+j*40
            )

            crtac.pendown()
            crtac.color("yellow")
            crtac.begin_fill()
            crtac.square = 15
            crtac.goto(x+35+i*25,y+30+j*40)
            crtac.goto(x+35+i*25,y+45+j*40)
            crtac.goto(x+20+i*25,y+45+j*40)
            crtac.goto(x+20+i*25,y+30+j*40)
            crtac.end_fill()

