import turtle

t = turtle.Turtle()
t.speed(5)

# Crtanje jajeta
def draw_egg():
    t.penup()
    t.goto(0, -60)
    t.setheading(0)
    t.pendown()
    
    t.begin_fill()
    t.fillcolor("lavender")
    t.color("black")
    
    t.circle(100, 180)
    t.circle(200, 180)
    
    t.end_fill()

# Funkcija za crtanje krugova (simetrično)
def symmetric_dots():
    t.color("red")
    
    positions = [(30, 40), (30, 0), (30, -40)]
    
    for x, y in positions:
        # desna strana
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.dot(15)
        
        # leva strana (ogledalo)
        t.penup()
        t.goto(-x, y)
        t.pendown()
        t.dot(15)

# Funkcija za V šare (simetrično)
def symmetric_v_pattern():
    t.color("blue")
    
    for y in [30, 0, -30]:
        t.penup()
        t.goto(0, y)
        t.setheading(0)
        t.pendown()
        
        for i in range(6):
            t.forward(10)
            if i % 2 == 0:
                t.left(60)
            else:
                t.right(60)

# Funkcija za linije (simetrično)
def symmetric_lines():
    t.color("green")
    
    for y in [50, -50]:
        t.penup()
        t.goto(-60, y)
        t.pendown()
        t.forward(120)

# Crtanje
draw_egg()
symmetric_lines()
symmetric_v_pattern()
symmetric_dots()

t.hideturtle()
turtle.done()
