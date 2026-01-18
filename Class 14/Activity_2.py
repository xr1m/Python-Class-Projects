# Star (Turtle):

import turtle

turtle.Screen().bgcolor("Blue")

t = turtle.Turtle()

t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.penup()
t.right(150)
t.forward(50)

# Second triangle which overlaps the first triangle:

t.pendown()
t.right(90)
t.forward(100)
t.right(120)
t.forward(100)
t.right(120)
t.forward(100)

turtle.done()