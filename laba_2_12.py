import turtle

turtle.left(90)
def half_circle(step):
    turtle.speed(10000)
    for i in range(60):
        turtle.forward(step)
        turtle.right(3)

n = 5
for i in range(n):
    if i % 2 == 0:
        half_circle(5)
    else:
        half_circle(2)