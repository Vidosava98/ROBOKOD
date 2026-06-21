import turtle
import random

# Ekran
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Robot Laser Game")
screen.setup(width=600, height=600)

# Robot
robot = turtle.Turtle()
robot.shape("square")
robot.color("cyan")
robot.shapesize(2, 2)
robot.penup()
robot.goto(0, -250)

# Laser
laser = turtle.Turtle()
laser.shape("square")
laser.color("red")
laser.shapesize(0.3, 1)
laser.penup()
laser.hideturtle()
laser.speed(0)

laser_state = "ready"

# Neprijatelj
enemy = turtle.Turtle()
enemy.shape("circle")
enemy.color("green")
enemy.penup()
enemy.goto(random.randint(-280, 280), 250)

# Score
score = 0
score_pen = turtle.Turtle()
score_pen.hideturtle()
score_pen.color("white")
score_pen.penup()
score_pen.goto(-280, 260)
score_pen.write("Score: 0", font=("Arial", 16, "normal"))

# Kretanje robota
def left():
    x = robot.xcor() - 20
    if x < -280:
        x = -280
    robot.setx(x)

def right():
    x = robot.xcor() + 20
    if x > 280:
        x = 280
    robot.setx(x)

# Pucanje
def fire_laser():
    global laser_state
    if laser_state == "ready":
        laser_state = "fire"
        laser.goto(robot.xcor(), robot.ycor() + 20)
        laser.showturtle()

# Sudar
def is_collision(t1, t2):
    return t1.distance(t2) < 20

# Glavna funkcija igre
def game_loop():
    global laser_state, score

    # Pomeri laser
    if laser_state == "fire":
        y = laser.ycor()
        y += 20
        laser.sety(y)

        if y > 300:
            laser.hideturtle()
            laser_state = "ready"

    # Pomeri neprijatelja
    enemy.sety(enemy.ycor() - 2)
    if enemy.ycor() < -300:
        enemy.goto(random.randint(-280, 280), 250)

    # Provera sudara
    if is_collision(laser, enemy):
        laser.hideturtle()
        laser_state = "ready"
        enemy.goto(random.randint(-280, 280), 250)

        score += 1
        score_pen.clear()
        score_pen.write(f"Score: {score}", font=("Arial", 16, "normal"))

    # Ponovo pozovi ovu funkciju nakon 20ms
    screen.ontimer(game_loop, 20)

# Kontrole
screen.listen()
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(fire_laser, "space")

# Pokreni igru
game_loop()
turtle.done()
