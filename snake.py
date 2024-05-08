import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# Create the screen BS
win = turtle.Screen()
win.title("Snake Game")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)

# Schlangenkopf
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# Create the food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []  # Körperteile

# score display
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Funktionen zum Bewegen der Schlange
def move():
    if head.direction == "Up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "Down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "Right":
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "Left":
        x = head.xcor()
        head.setx(x - 20)

# Funktionen zum Ändern der Richtung der Schlange
def go_up():
    if head.direction != "Down":
        head.direction = "Up"

def go_down():
    if head.direction != "Up":
        head.direction = "Down"

def go_right():
    if head.direction != "Left":
        head.direction = "Right"

def go_left():
    if head.direction != "Right":
        head.direction = "Left"

# Keyboard bindings
win.listen()
win.onkeypress(go_up, "w")
win.onkeypress(go_down, "s")
win.onkeypress(go_right, "d")
win.onkeypress(go_left, "a")

# Main game loop
while True:
    win.update()

    # Auf Kollision mit dem Futter prüfen
    if head.distance(food) < 20:
        # das Futter an eine zufällige Position
        x = random.randint(-280, 280)
        y = random.randint(-280, 240)
        food.goto(x, y)

        # neue körperteile
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Erhöhen die Punktzahl
        score += 10

        if score > high_score:
            high_score = score

        score_display.clear()
        score_display.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    # snake körper bewegen
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Bewegen  das erste Körpersegment dorthin, wo sich der Kopf befindet
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Auf Kollision mit den Rändern prüfen
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 240 or head.ycor() < -280:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"

        # Reset the score
        score = 0

        # Clear the body segments
        for segment in segments:
            segment.goto(1000, 1000)  # Move segments off-screen
        segments.clear()

        score_display.clear()
        score_display.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

win.mainloop()
##Erweiterungsmöglichkeiten  :Schwierigkeitsgrad , Grafiken, Sounds 