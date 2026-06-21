import turtle
import random

# Ekran
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=400, height=400)
screen.title("Jumping Square")

# Kvadrat
square = turtle.Turtle()
square.shape("square")
square.color("cyan")
square.shapesize(2, 2)
square.penup()
square.goto(0, 0)
square.speed(0)

# Score
score = 0
score_pen = turtle.Turtle()
score_pen.hideturtle()
score_pen.color("white")
score_pen.penup()
score_pen.goto(-180, 160)
score_pen.write(f"Score: {score}", font=("Arial", 14, "normal"))

# Kretanje levo/desno
def move_left():
    x = square.xcor() - 20
    if x < -180:
        x = -180
    square.setx(x)

def move_right():
    x = square.xcor() + 20
    if x > 180:
        x = 180
    square.setx(x)

# Kontrole
screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# Skakanje kvadrata
direction = 1  # 1 = gore, -1 = dole

def game_loop():
    global direction, score
    y = square.ycor() + 5 * direction
    if y > 150:
        direction = -1
        score += 1
        score_pen.clear()
        score_pen.write(f"Score: {score}", font=("Arial", 14, "normal"))
    elif y < -150:
        direction = 1
    square.sety(y)
    screen.ontimer(game_loop, 50)

# Pokreni igru
game_loop()
turtle.done()
