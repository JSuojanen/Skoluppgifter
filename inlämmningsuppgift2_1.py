
import turtle
import random
from turtle import *
from random import *

Screen = turtle.Screen
turtle.speed(5)
def draw_cube(x, y):
#främre fyrkant
    teleport(x, y)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    penup
#bakre fyrkant
    teleport(x+ 40, y+ 40)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)

#för att sätta ihop fyrkanterna
    setheading(0)
    teleport(x, y)
    goto(x+ 40,y + 40)

    teleport(x + 100, y + 0)
    goto(x+ 140, y + 40)

    teleport(x + 100, y + 100)
    goto(x+ 140, y + 140)

    teleport(x+ 0, y + 100)
    goto(x+ 40, y + 140)

import turtle
from random import randint
from turtle import *

turtle.speed(5)
turtle.pensize(3)
def draw_gubbe(x, y):
    penup()
    goto(x, y)
    pendown()
    setheading(0)
    turtle.circle(30)
    right(90)
    forward(55)
    setheading(225)
    forward (50)
    setheading(45)
    forward(50)
    setheading(0)
    setheading(315)
    forward(50)


    #Här bestämmer användaren hur många kuber och gubbar ska ritas

amount = int(input("Hur många kuber vill du ha? "))
for i in range(amount):
    slump_x = randint(-300, 200)
    slump_y = randint(-300, 200)
    draw_cube(slump_x, slump_y)

amount = int(input("Hur många gubbar vill du ha? "))
for i in range(amount):
    slump_x = randint(-300, 200)
    slump_y = randint(-300, 200)
    draw_gubbe(slump_x, slump_y)


done()








