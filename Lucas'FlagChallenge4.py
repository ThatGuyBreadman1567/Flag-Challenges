import turtle
turtle.fillcolor('blue')
turtle.penup()
turtle.pencolor('blue')
x = 0
while x != 4:
    turtle.begin_fill()
    turtle.forward(120)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(120)
    turtle.end_fill()
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    x += 1
turtle.forward(120)
turtle.left(90)
turtle.forward(90)
turtle.left(90)
turtle.penup()
turtle.fillcolor('white')
turtle.forward(70)
turtle.begin_fill()
while x != 8:
    turtle.forward(50)
    turtle.left(90)
    x += 1
turtle.end_fill()
turtle.fillcolor('blue')
while x != 10:
    turtle.forward(20)
    turtle.begin_fill()
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(10)
    turtle.end_fill()
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    x += 1
turtle.pendown()
turtle.left(90)
turtle.forward(50)
while x != 12:
    turtle.right(90)
    turtle.forward(120)
    turtle.right(90)
    turtle.forward(90)
    x += 1    
turtle.done()