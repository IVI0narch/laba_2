import turtle


def circle(step):
    turtle.speed(10000)
    for i in range(60):
        turtle.forward(step)
        turtle.left(6)

n = 10
for i in range(n):
    circle(7 + 2 * i)
    turtle.left(180)