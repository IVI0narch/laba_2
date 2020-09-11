import turtle

turtle.shape('turtle')
angle = 0
for i in range(1080):
    turtle.speed(1000)
    turtle.forward(1/360*angle)
    angle += 1
    turtle.left(1)