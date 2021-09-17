
# Script Name: first_attempt.py
# Author: Ben Murphy

from turtle import *
from random import randint


turt = Turtle()

def colour_pentagon_spiral():
    turt.hideturtle()
    turt.speed(0)
    x = 0
    bgcolor("black")
    while x < 200:
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        colormode(255)

        turt.pencolor(r, g, b)
        turt.fd(x)
        turt.lt(80)
        turt.fd(30)
        turt.rt(10)
        x += 1
    turt.getscreen().exitonclick()

def triangle():
    turt.hideturtle()
    for i in range(0, 3):
        turt.fd(60)
        turt.lt(120)
    turt.getscreen().exitonclick()


def square():
    turt.hideturtle()
    for i in range(0, 4):
        turt.fd(50)
        turt.rt(90)
    turt.getscreen().exitonclick()


def lotus_attempt():
    x = 60
    bgcolor("black")
    turt.speed(0)
    turt.hideturtle()
    turt.pencolor("white")
    while x < 180:
        turt.fd(x)
        turt.lt(90)
        turt.fd(x)
        turt.lt(90)
        turt.fd(x)
        turt.lt(95)
        turt.fd(x)

        x += 1
    turt.getscreen().exitonclick()




def circle():
    turt.hideturtle()
    turt.speed(0)
    x = 0
    while x < 20:
        turt.fd(30)
        turt.lt(20)
        turt.rt(40)

        x += 1
    turt.getscreen().exitonclick()

def dodechahedron():
    turt.hideturtle()
    turt.speed(0)
    x = 0
    while x < 20:
        turt.fd(30)
        turt.lt(10)
        turt.rt(40)

        x += 1
    turt.getscreen().exitonclick()


def spiral():
    bgcolor("black")
    turt.hideturtle()
    turt.speed(0)
    turt.pencolor("white")
    x = 0
    y = 0
    while x < 150:
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        colormode(255)
        turt.pencolor(r, g, b)
        turt.fd(x)
        turt.lt(y)
        turt.rt(40)

        x += 1
        if y < 20:
            y += 1
        else:
            y -= 3
    turt.getscreen().exitonclick()



def triangle_attrempt():
    turt.hideturtle()
    turt.speed(0)
    x = 0
    while x < 40:
        for i in range(0, 3):
            turt.fd(60)
            turt.lt(120)
        x += 1
        turt.lt(170)

    turt.getscreen().exitonclick()

def pentagon_spiral():
    turt.hideturtle()
    turt.speed(0)
    x = 0
    bgcolor("black")
    turt.pencolor("white")
    while x < 200:
        turt.fd(x)
        turt.lt(80)
        turt.fd(30)
        turt.rt(10)
        x += 1
    turt.getscreen().exitonclick()


def background():
    turt.speed(0)
    p = 80
    for x in range(300):
        p += 30
        turt.fd(p)
        turt.rt(360*2 / 4 + 1)
    turt.getscreen().exitonclick()

def star():
    turt.hideturtle()
    turt.speed(0)
    for x in range(5):
        turt.fd(100)
        turt.rt(144)
    turt.getscreen().exitonclick()



#background()