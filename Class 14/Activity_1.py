# Polygon (Turtle):

import turtle

userinput = int(input("Enter your sides: "))
userlen = int(input("Enter how much length you want of the sides: "))

turtle.Screen().setup(600, 600)
turtle.Screen().bgcolor("Aqua")

polygon = turtle.Turtle()
angle = 360.0/userinput

for i in range(userinput):
    polygon.forward(userlen)
    polygon.right(angle)

turtle.color("Red")

turtle.done()