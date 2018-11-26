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

s(10)

l(180)
u()
f(200)
l(180)
d()
r(90)
f(100)
l(90)
c('blue')
b()
while x != 4:
    f(400)
    l(90)
    f(40)
    l(90)
    f(400)
    l(90)
    f(40)
    l(180)
    f(80)
    r(90)
    x += 1
e()
p('white')
r(90)
f(40)
p('black')
f(200)
l(90)
l(30)
c('red')
b()
f(200)
l(120)
f(200)
e()
l(120)
f(100)
l(90)
u()
f(60)
l(90)
f(30)
d()
c('white')
b()
l(198)
while x != 6:
    f(22.36)
    l(72)
    f(22.36)
    r(144)
    f(22.36)
    l(72)
    f(22.36)
    l(180)
    l(36)
    x += 1
f(22.36)
l(72)
f(22.36)
e()
r(162)
u()
f(30)
r(90)
f(60)
r(270)
d()
f(100)
l(90)
f(400)
l(90)
f(200)

turtle.done()
