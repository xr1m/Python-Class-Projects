import turtle

tscreen = turtle.Screen()

tscreen.bgcolor("Aqua")

tscreen.title("Spiral Pattern")

t = turtle.Turtle()

size = int(input("Enter size"))

turn_count = 0

max_turns = int(input("Enter Maximum Turns"))

while True:

    t.forward(size)

    t.left(90)

    turn_count += 1

    size += 10

    if turn_count == max_turns:

        break

turtle.done()