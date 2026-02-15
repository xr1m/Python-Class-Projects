# Spiral pattern (Turtle) [Square inside a Square]:

import turtle

tscreen = turtle.Screen()

tscreen.bgcolor("Aqua")
tscreen.title("Spiral Pattern")

t = turtle.Turtle()

size = 0

while True:
    for i in range(4):
        t.fd(size + 1)
        t.left(90)
        size = size - 5
    size = size + 1