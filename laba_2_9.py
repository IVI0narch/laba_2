import turtle


def n_angle(n, step):
    turtle.left(360 / n)
    for i in range(n):
        turtle.forward(step)
        turtle.left(360 / n)
    turtle.right(360 / n)
    turtle.penup()
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.pendown()

for i in range(3, 8):
    n_angle(i, 50 + i * 60)