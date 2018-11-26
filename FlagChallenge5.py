import turtle

t = turtle
l = t.left
r = t.right
f = t.forward
b = t.begin_fill
e = t.end_fill
c = t.fillcolor
u = t.penup
d = t.pendown
p = t.pencolor

l(180)
u()
f(20)
l(180)
d()
r(90)
f(100)
l(90)
c('blue')
b()
f(400)
l(90)
f(200)
l(90)
f(400)
l(90)
f(200)
l(90)
e()
l(30)
c('red')
b()
f(200)
l(120)
f(200)
e()

turtle.done()