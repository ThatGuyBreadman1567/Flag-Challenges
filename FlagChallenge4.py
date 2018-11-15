# 90 * 120 
# 50 * 50
import turtle
x=0
turtle.speed(8)
turtle.fillcolor('blue')
turtle.begin_fill()
turtle.goto(120,0)
turtle.goto(120,90)
turtle.goto(0,90)
turtle.goto(0,0)
turtle.end_fill()
turtle.penup()
turtle.goto(0,10)
turtle.pendown()
turtle.fillcolor('white')
while x != 4:
    turtle.begin_fill()
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(10)
    turtle.end_fill()
    turtle.left(180)
    turtle.forward(20)
    turtle.right(90)
    x += 1
turtle.fillcolor('blue')
turtle.begin_fill()
while x != 8:
    turtle.forward(50)
    turtle.right(90)
    x += 1
turtle.end_fill()
turtle.right(90)
turtle.forward(30)
turtle.left(90)
turtle.fillcolor('white')
turtle.begin_fill()
while x != 12:
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    x += 1
turtle.end_fill()
turtle.done()