import turtle
import random
turtle.hideturtle()
turtle.speed(0)
turtle.pensize(5)
turtle.penup()
turtle.goto(-250,0)
turtle.pendown()
for i in range(5):
    for i in range(25):
        a = "#"
        for i in range(6):
            a = a + random.choice('0123456789ABCDEF')
        turtle.color(a)
        turtle.begin_fill()
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()
    turtle.right(144)
    turtle.end_fill()
turtle.right(72)
for i in range(5):
    for i in range(15):
        a = "#"
        for i in range(6):
            a = a + random.choice('0123456789ABCDEF')
        turtle.color(a)
        turtle.begin_fill()
        turtle.forward(10.300166666666666666666666666667)
        turtle.penup()
        turtle.forward(10.300166666666666666666666666667)
        turtle.pendown()
    turtle.left(72)
turtle.left(72)
turtle.right(18)
turtle.right(90)
turtle.color("black")
turtle.circle(264)
turtle.begin_fill()
turtle.end_fill()
turtle.penup()
turtle.forward(300)
turtle.pendown()
turtle.mainloop()