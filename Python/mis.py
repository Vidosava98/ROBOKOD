import turtle
import random

# Ekran
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=400, height=400)
screen.title("Chase the Circle")

# Kvadrat (igrač)
player = turtle.Turtle()
player.shape("square")
player.color("cyan")
player.shapesize(2, 2)
player.penup()
player.speed(0)

# Krug (cilj)
target = turtle.Turtle()
target.shape("circle")
target.color("red")
target.penup()
target.speed(0)
target.goto(random.randint(-180, 180), random.randint(-180, 180))

# Score
score = 0
score_pen = turtle.Turtle()
score_pen.hideturtle()
score_pen.color("white")
score_pen.penup()
score_pen.goto(-180, 160)
score_pen.write(f"Score: {score}", font=("Arial", 14, "normal"))

# Kretanje igrača za mišom
def follow_mouse(x, y):
    player.goto(x, y)

# Sudar
def is_collision(t1, t2):
    return t1.distance(t2) < 20

# Glavna petlja
def game_loop():
    global score
    if is_collision(player, target):
        score += 1
        score_pen.clear()
        score_pen.write(f"Score: {score}", font=("Arial", 14, "normal"))
        target.goto(random.randint(-180, 180), random.randint(-180, 180))
    screen.ontimer(game_loop, 20)

# Kontrola miša
screen.listen()
screen.onscreenclick(follow_mouse)

# Pokreni igru
game_loop()
turtle.done()
