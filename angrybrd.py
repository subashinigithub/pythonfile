import turtle
s=turtle.Turtle()
s.color("red")
s.begin_fill()
s.circle(150)
s.end_fill()
s.speed(0)

s.penup()
s.setpos(70,180)
s.pendown()
s.color("black")
s.begin_fill()
s.speed(0)
s.right(90)
s.forward(10)
for x in range(145):
    s.right(1)
    s.forward(0.25)
s.right(30)
s.forward(20)
for x in range(145):
    s.right(1)
    s.forward(0.25)
s.end_fill()

s.penup()
s.setpos(-30,180)
s.pendown()
s.color("black")
s.begin_fill()
s.right(45)
s.forward(10)
for x in range(145):
    s.right(1)
    s.forward(0.25)
s.right(30)
s.forward(20)
for x in range(145):
    s.right(1)
    s.forward(0.25)
s.end_fill()

s.penup()
s.setpos(-19,190)
s.pendown()
s.pensize(10)
s.color("black")
s.right(170)
s.forward(10)
for x in range(50):
    s.left(1)
    s.forward(1)
s.penup()
s.setpos(30,190)
s.pendown()
s.pensize(10)
s.color("black")
s.right(150)
s.forward(10)
for x in range(50):
    s.right(1)
    s.forward(1)

s.penup()
s.setpos(-30,73)
s.pendown()
s.left(45)
for x in range(70):
    s.right(1)
    s.forward(1)








turtle.done()