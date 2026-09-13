import turtle

screen = turtle.Screen()
screen.setup(width=1000, height=750)
screen.bgcolor("midnight blue")
screen.title("Alienfamiljen")
screen.tracer(False)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)


def move(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()


def ellipse(cx, cy, width, height, color, outline="black"):
    move(cx + width / 2, cy)
    pen.setheading(90)
    pen.color(outline, color)
    pen.begin_fill()
    for _ in range(2):
        pen.circle(width / 2, 90)
        pen.circle(height / 2, 90)
    pen.end_fill()


def rectangle(cx, cy, width, height, color, outline="black"):
    move(cx - width / 2, cy - height / 2)
    pen.setheading(0)
    pen.color(outline, color)
    pen.begin_fill()
    for length, angle in [(width, 0), (height, 90), (width, 180), (height, 270)]:
        pen.forward(length)
        pen.left(90)
    pen.end_fill()


def line(x1, y1, x2, y2, color="white", size=3):
    pen.color(color)
    pen.pensize(size)
    move(x1, y1)
    pen.goto(x2, y2)
    pen.pensize(3)


def alien(x, y, scale=1.0, adult=True, shirt="forest green"):
    head_w = 100 * scale if adult else 70 * scale
    head_h = 120 * scale if adult else 85 * scale
    body_w = 85 * scale if adult else 60 * scale
    body_h = 125 * scale if adult else 90 * scale
    leg_len = 75 * scale if adult else 50 * scale
    arm_len = 65 * scale if adult else 45 * scale
    green = "#75d66b"

    # Huvud och kropp
    ellipse(x, y + 100 * scale, head_w, head_h, green)
    rectangle(x, y - 5 * scale, body_w, body_h, shirt)

    # Ögon
    eye_w = 22 * scale if adult else 15 * scale
    eye_h = 45 * scale if adult else 30 * scale
    ellipse(x - 22 * scale, y + 105 * scale, eye_w, eye_h, "black")
    ellipse(x + 22 * scale, y + 105 * scale, eye_w, eye_h, "black")

    # Litet leende
    pen.color("black")
    pen.pensize(max(1, int(2 * scale)))
    move(x - 12 * scale, y + 75 * scale)
    pen.setheading(-60)
    pen.circle(15 * scale, 120)
    pen.pensize(3)

    # Antenner
    line(x - 28 * scale, y + 157 * scale, x - 42 * scale, y + 180 * scale, green, 3)
    line(x + 28 * scale, y + 157 * scale, x + 42 * scale, y + 180 * scale, green, 3)
    ellipse(x - 43 * scale, y + 182 * scale, 10 * scale, 10 * scale, "yellow")
    ellipse(x + 43 * scale, y + 182 * scale, 10 * scale, 10 * scale, "yellow")

    # Armar
    line(x - body_w / 2, y + 20 * scale, x - body_w / 2 - arm_len, y - 15 * scale, green, 7)
    line(x + body_w / 2, y + 20 * scale, x + body_w / 2 + arm_len, y - 15 * scale, green, 7)

    # Ben och skor
    line(x - 22 * scale, y - body_h / 2, x - 30 * scale, y - body_h / 2 - leg_len, green, 8)
    line(x + 22 * scale, y - body_h / 2, x + 30 * scale, y - body_h / 2 - leg_len, green, 8)
    line(x - 42 * scale, y - body_h / 2 - leg_len, x - 20 * scale, y - body_h / 2 - leg_len, "silver", 7)
    line(x + 20 * scale, y - body_h / 2 - leg_len, x + 42 * scale, y - body_h / 2 - leg_len, "silver", 7)

    # Knapp på tröjan
    ellipse(x, y + 15 * scale, 10 * scale, 10 * scale, "orange")


def ufo(x, y, scale=1.0):
    # Stråle
    pen.color("light green")
    pen.pensize(2)
    move(x - 115 * scale, y - 25 * scale)
    pen.goto(x + 115 * scale, y - 25 * scale)
    move(x - 75 * scale, y - 100 * scale)
    pen.goto(x + 75 * scale, y - 100 * scale)
    pen.color("yellow")
    pen.fillcolor("yellow")
    pen.begin_fill()
    move(x - 115 * scale, y - 25 * scale)
    pen.goto(x + 115 * scale, y - 25 * scale)
    pen.goto(x + 75 * scale, y - 100 * scale)
    pen.goto(x - 75 * scale, y - 100 * scale)
    pen.goto(x - 115 * scale, y - 25 * scale)
    pen.end_fill()

    # UFO-kupol
    ellipse(x, y + 25 * scale, 100 * scale, 55 * scale, "light cyan", "white")

    # UFO-kropp
    ellipse(x, y, 260 * scale, 70 * scale, "silver", "white")
    ellipse(x, y - 5 * scale, 190 * scale, 35 * scale, "purple", "white")

    # Lampor
    for dx in (-80, -40, 0, 40, 80):
        ellipse(x + dx * scale, y - 15 * scale, 14 * scale, 14 * scale, "yellow")


# Stjärnor
for sx, sy in [(-450, 300), (-330, 250), (-180, 320), (40, 300), (190, 250), (370, 320), (450, 210), (-420, 80), (410, 70)]:
    ellipse(sx, sy, 5, 5, "white")

# UFO högst upp
ufo(0, 270, 0.85)

# Alienfamiljen: två vuxna och två barn
alien(-210, -80, 1.0, True, "forest green")
alien(210, -80, 1.0, True, "dark orange")
alien(-75, -165, 0.65, False, "royal blue")
alien(75, -165, 0.65, False, "hot pink")

screen.update()
screen.mainloop()