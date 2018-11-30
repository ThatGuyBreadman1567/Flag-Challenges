import turtle

x = 1
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
s = t.speed

c('red')
b()
f(120)
l(90)
f(60)
l(90)
f(120)
l(90)
f(60)
e()
l(90)
f(30)
c('black')
b()
f(90)
l(90)
f(20)
l(90)
f(90)
l(90)
f(20)
e()
l(180)
f(20)
r(90)
p('white')
c('white')
b()
f(90)
l(90)
f(20)
l(90)
f(90)
l(90)
f(20)
e()
l(180)
f(20)
r(90)
p('green')
c('green')
b()
f(90)
l(90)
f(20)
l(90)
f(90)
l(90)
f(20)
e()
l(180)
f(20)
p('black')
r(90)
f(90)
r(90)
f(60)
r(90)
f(120)
r(90)
f(60)
r(90)
f(30)

turtle.done()