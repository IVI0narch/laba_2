import turtle


def circle():
    turtle.speed(10000)
    for i in range(60):
        turtle.forward(7)
        turtle.left(6)

for i in range(8):
    circle()
    turtle.left(360 / 8)
