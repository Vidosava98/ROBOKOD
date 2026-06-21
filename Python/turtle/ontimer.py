import turtle
import random

# Screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(600,600)
screen.title("Teleport Target")

# Player
player = turtle.Turtle()
player.shape("square")
player.color("cyan")
player.penup()
player.speed(0)

# Target
target = turtle.Turtle()
target.shape("circle")
target.color("yellow")
target.penup()
target.speed(0)

target.goto(random.randint(-250,250), random.randint(-250,250))

# Score
score = 0
score_pen = turtle.Turtle()
score_pen.hideturtle()
score_pen.color("white")
score_pen.penup()
score_pen.goto(-280,260)
score_pen.write("Score: 0", font=("Arial",16,"normal"))

# Movement
def left():
    player.setx(player.xcor() - 20)

def right():
    player.setx(player.xcor() + 20)

def up():
    player.sety(player.ycor() + 20)

def down():
    player.sety(player.ycor() - 20)

# Controls
screen.listen()
screen.onkey(left,"Left")
screen.onkey(right,"Right")
screen.onkey(up,"Up")
screen.onkey(down,"Down")

# Collision
def is_collision(t1,t2):
    return t1.distance(t2) < 20

# Teleport target
def teleport():
    target.goto(random.randint(-250,250), random.randint(-250,250))
    screen.ontimer(teleport,2000)

teleport()

# Game loop
def game_loop():
    global score

    if is_collision(player,target):

        score += 1
        score_pen.clear()
        score_pen.write(f"Score: {score}",font=("Arial",16,"normal"))

        target.goto(random.randint(-250,250), random.randint(-250,250))

    screen.ontimer(game_loop,20)

game_loop()

turtle.done()
