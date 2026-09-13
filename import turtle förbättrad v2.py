import turtle
import math
import random

# --- Skärm & Turtle Setup ---
screen = turtle.Screen()
screen.setup(width=1000, height=750)
screen.colormode(255)  # Tillåter exakta RGB-färger för mjuka övergångar
BG_COLOR = (12, 18, 38)
screen.bgcolor(BG_COLOR)
screen.title("Alienfamiljen - Premium Scen med Miljö och Ljuseffekter")
screen.tracer(False)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

# --- Matematiska Ritfunktioner ---

def draw_true_ellipse(cx, cy, rx, ry, fill_color, outline_color=None, outline_width=2):
    pen.penup()
    if outline_color:
        pen.color(outline_color, fill_color)
        pen.pensize(outline_width)
    else:
        pen.color(fill_color, fill_color)
        pen.pensize(1)
        
    steps = 60
    for i in range(steps + 1):
        angle = (2 * math.pi * i) / steps
        x = cx + rx * math.cos(angle)
        y = cy + ry * math.sin(angle)
        if i == 0:
            pen.goto(x, y)
            pen.pendown()
            pen.begin_fill()
        else:
            pen.goto(x, y)
    pen.end_fill()
    pen.penup()

def draw_rotated_ellipse(cx, cy, rx, ry, angle_deg, fill_color):
    pen.penup()
    pen.color(fill_color)
    steps = 40
    angle_rad = math.radians(angle_deg)
    cos_rot = math.cos(angle_rad)
    sin_rot = math.sin(angle_rad)
    
    for i in range(steps + 1):
        t = (2 * math.pi * i) / steps
        x_base = rx * math.cos(t)
        y_base = ry * math.sin(t)
        x = cx + (x_base * cos_rot - y_base * sin_rot)
        y = cy + (x_base * sin_rot + y_base * cos_rot)
        if i == 0:
            pen.goto(x, y)
            pen.pendown()
            pen.begin_fill()
        else:
            pen.goto(x, y)
    pen.end_fill()
    pen.penup()

def draw_line(x1, y1, x2, y2, color, thickness):
    pen.penup()
    pen.goto(x1, y1)
    pen.color(color)
    pen.pensize(thickness)
    pen.pendown()
    pen.goto(x2, y2)
    pen.penup()

# --- Designade Objekt & Miljö ---

def draw_scenery():
    # Stjärnor med olika färg och storlek
    for _ in range(60):
        sx = random.randint(-500, 500)
        sy = random.randint(-100, 375)
        size = random.uniform(1, 3)
        color = random.choice([(255,255,255), (200,220,255), (255,255,200)])
        draw_true_ellipse(sx, sy, size, size, color)

    # Måne i bakgrunden
    draw_true_ellipse(-350, 200, 60, 60, (230, 230, 240))
    draw_true_ellipse(-320, 220, 15, 15, (200, 200, 210)) # Krater
    draw_true_ellipse(-370, 180, 20, 20, (200, 200, 210)) # Krater

    # Landskap / Kullar (ritas som gigantiska ellipser längst ner)
    draw_true_ellipse(-300, -450, 400, 250, (6, 9, 20)) # Vänster kulle
    draw_true_ellipse(350, -500, 500, 300, (8, 12, 25))  # Höger kulle
    draw_true_ellipse(0, -400, 600, 150, (10, 15, 30))   # Mittenkulle (marken de står på)

def draw_ufo(x, y, scale=1.0):
    s = scale
    
    # 1. Traktorstråle (Mjuk gradient i 15 lager)
    beam_color = (150, 255, 180)
    for i in range(15):
        alpha = i / 15
        # Blanda strålens färg med bakgrundens färg för fusk-transparens
        r = int(BG_COLOR[0] + (beam_color[0] - BG_COLOR[0]) * alpha)
        g = int(BG_COLOR[1] + (beam_color[1] - BG_COLOR[1]) * alpha)
        b = int(BG_COLOR[2] + (beam_color[2] - BG_COLOR[2]) * alpha)
        
        w_top = (100 - i * 5) * s
        w_bot = (160 - i * 8) * s
        
        pen.penup()
        pen.goto(x - w_top, y - 10*s)
        pen.color((r, g, b))
        pen.pendown()
        pen.begin_fill()
        pen.goto(x + w_top, y - 10*s)
        pen.goto(x + w_bot, y - 350*s)
        pen.goto(x - w_bot, y - 350*s)
        pen.end_fill()
    
    # 2. Kupolens bakgrund
    draw_true_ellipse(x, y + 25*s, 65*s, 45*s, (50, 100, 120), (30, 80, 100), 2)
    
    # 3. Liten Pilot inuti UFO:t!
    pilot_y = y + 30*s
    draw_true_ellipse(x, pilot_y, 25*s, 18*s, (129, 199, 132)) # Pilothuvud
    draw_rotated_ellipse(x - 10*s, pilot_y + 2*s, 5*s, 8*s, -30, (20, 20, 20)) # Vänster öga
    draw_rotated_ellipse(x + 10*s, pilot_y + 2*s, 5*s, 8*s, 30, (20, 20, 20))  # Höger öga
    
    # 4. Kupolens glas-reflektion (Ritas över piloten för glas-effekt)
    pen.penup()
    pen.goto(x - 40*s, y + 45*s)
    pen.color((200, 240, 255))
    pen.pensize(4)
    pen.setheading(60)
    pen.pendown()
    pen.circle(-45*s, 50) # Ritar en böjd vit linje som blänk
    
    # 5. Huvudskrov
    draw_true_ellipse(x, y, 170*s, 35*s, (200, 210, 220), (140, 150, 160), 3)
    
    # 6. Undersida
    draw_true_ellipse(x, y - 15*s, 85*s, 22*s, (126, 87, 194), (94, 53, 177), 3)
    
    # 7. Lampor (med liten glöd bakom sig)
    for dx in (-110, -55, 0, 55, 110):
        dy = y - 5*s + (1 - abs(dx)/(130*s)) * 8*s 
        draw_true_ellipse(x + dx*s, dy, 12*s, 8*s, (255, 200, 0)) # Glöd
        draw_true_ellipse(x + dx*s, dy, 7*s, 5*s, (255, 255, 200)) # Lampa


def draw_alien(x, y, scale=1.0, is_adult=True, shirt_color=(76, 175, 80)):
    s = scale if is_adult else scale * 0.7
    skin = (129, 199, 132)
    skin_dark = (76, 175, 80)
    
    # --- Mått ---
    foot_y = y - 90*s
    
    # 0. Drop-shadow på marken (Gör att de står fast på jorden)
    draw_true_ellipse(x, foot_y - 5*s, 50*s, 10*s, (5, 8, 15))

    # 1. Armar & Ben
    draw_line(x - 20*s, y - 20*s, x - 25*s, foot_y, skin, 12*s)
    draw_line(x + 20*s, y - 20*s, x + 25*s, foot_y, skin, 12*s)
    
    draw_line(x - 42*s, foot_y, x - 15*s, foot_y, (69, 90, 100), 14*s) # Sko V
    draw_line(x + 15*s, foot_y, x + 42*s, foot_y, (69, 90, 100), 14*s) # Sko H
    
    draw_line(x - 40*s, y + 20*s, x - 75*s, y - 20*s, skin, 10*s) # Arm V
    draw_line(x + 40*s, y + 20*s, x + 75*s, y - 20*s, skin, 10*s) # Arm H

    # 2. Kropp
    draw_true_ellipse(x, y, 45*s, 55*s, shirt_color, (30, 30, 30), 2)
    draw_true_ellipse(x, y, 15*s, 15*s, (255, 179, 0)) # Detalj

    # 3. Huvud
    head_y = y + 70*s
    draw_true_ellipse(x, head_y, 60*s, 45*s, skin, skin_dark, 3)

    # 4. Ögon
    draw_rotated_ellipse(x - 22*s, head_y + 5*s, 14*s, 22*s, -25, (15, 15, 15))
    draw_rotated_ellipse(x + 22*s, head_y + 5*s, 14*s, 22*s, 25, (15, 15, 15))
    draw_true_ellipse(x - 25*s, head_y + 12*s, 4*s, 5*s, (255,255,255)) # Glans V
    draw_true_ellipse(x + 19*s, head_y + 12*s, 4*s, 5*s, (255,255,255)) # Glans H

    # 5. Mun
    pen.penup()
    pen.goto(x - 10*s, head_y - 20*s)
    pen.setheading(-60)
    pen.color((46, 125, 50))
    pen.pensize(3*s)
    pen.pendown()
    pen.circle(12*s, 120)

    # 6. Antenner
    draw_line(x - 20*s, head_y + 40*s, x - 35*s, head_y + 70*s, skin, 4*s)
    draw_line(x + 20*s, head_y + 40*s, x + 35*s, head_y + 70*s, skin, 4*s)
    draw_true_ellipse(x - 35*s, head_y + 70*s, 8*s, 8*s, (255, 179, 0))
    draw_true_ellipse(x + 35*s, head_y + 70*s, 8*s, 8*s, (255, 179, 0))


# --- Rendera hela scenen ---

# 1. Rita Miljön (Stjärnor, måne, mark)
draw_scenery()

# 2. Rita UFO och traktorstråle i bakgrunden
draw_ufo(0, 230, 1.1)

# 3. Rita Familjen i förgrunden (rgb-färger för kläderna)
draw_alien(-230, -80, scale=1.0, is_adult=True, shirt_color=(229, 57, 53))   # Röd
draw_alien(230, -80, scale=1.0, is_adult=True, shirt_color=(57, 73, 171))    # Blå
draw_alien(-90, -130, scale=0.7, is_adult=False, shirt_color=(253, 216, 53)) # Gul
draw_alien(90, -130, scale=0.7, is_adult=False, shirt_color=(142, 36, 170))  # Lila

screen.update()
screen.mainloop()