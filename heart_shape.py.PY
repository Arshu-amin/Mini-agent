import turtle

turtle.speed(3)
turtle.bgcolor("WHITE")
turtle.color("RED", "PINK")
turtle.pensize(3)

def curve():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)
turtle.begin_fill()
turtle.left(140)
turtle.forward(113)

curve()
turtle.left(120)
curve()

turtle.forward(112)
turtle.end_fill()
