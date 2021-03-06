import turtle


def circle(step):
    turtle.speed(10000)
    for i in range(60):
        turtle.forward(step)
        turtle.left(6)
def half_circle():
    turtle.speed(10000)
    for i in range(60):
        turtle.forward(2)
        turtle.left(3)

turtle.begin_fill()
circle(8)
turtle.color('yellow')
turtle.end_fill()
turtle.color('black')
turtle.penup()
turtle.goto(-25, 85)
turtle.pendown()
turtle.begin_fill()
circle(1)
turtle.color('blue')
turtle.end_fill()
turtle.penup()
turtle.goto(25, 85)
turtle.pendown()
turtle.begin_fill()
circle(1)
turtle.color('blue')
turtle.end_fill()
turtle.penup()
turtle.goto(0, 60)
turtle.pendown()
turtle.color('black')
turtle.width(3)
turtle.right(90)
turtle.forward(20)
turtle.penup()
turtle.goto(-40, 50)
turtle.pendown()
turtle.color('red')
half_circle()