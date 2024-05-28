""" import turtle
s=turtle.Turtle()
s.pensize(10)
s.circle(100)
s.seth(180)
s.circle(100)
turtle.done() """

""" import turtle
s=turtle.Turtle()
s.forward(100)
s.backward(50)
s.right(90)
s.dot()
s.forward(100)
s.home()
s.goto(100,-60)
s.shape("circle")
s.left(750)
turtle.done() """

""" import turtle
s=turtle.Turtle()
s.speed(1)
s.pensize(10)
turtle.bgcolor("violet")
for x in range(10):
    s.circle(100)
    s.right(200)
turtle.done()
 """

""" import turtle
t=turtle.Turtle()
t.penup()
t.setpos(-20,40)
t.pendown()
t.pensize(10)
t.pencolor("green")
t.forward(100)
t.backward(100)
t.right(90)
t.forward(100)
t.left(90)
t.forward(100)
t.backward(100)
t.right(90)
t.forward(100)
t.left(90)
t.forward(100)
turtle.done() """
#suba letter
import turtle
s=turtle.Turtle()
s.speed(1)
s.penup()
s.setpos(10,20)
s.pendown()
s.pensize(10)
s.color("yellow")
s.pencolor("black")
s.begin_fill()
s.circle(100)
s.end_fill()
s.penup()
s.setpos(50,150)
s.pendown()
s.color("black")
s.begin_fill()
s.circle(10)
s.end_fill()
s.penup()
s.setpos(-40,150)
s.pendown()
s.color("black")
s.begin_fill()
s.circle(10)
s.end_fill()
s.penup()
s.setpos(-35,70)
s.pendown()
s.right(45)
s.forward(1)
for x in range(90):
    s.forward(1)
    s.left(1)





#s letter
s.penup()
s.setpos(-90,-20)
s.pendown()
s.speed(0)
s.pensize(10)
turtle.bgcolor("violet")
s.pencolor("green")
for x in range(265):
    s.forward(1)
    s.left(1)
s.right(10)
s.forward(150)
for x in range(265):
    s.forward(1)
    s.right(1)
#u letter
s.penup()
s.setpos(-40,-10)
s.pendown()
s.right(130)
s.forward(70)
for x in range(170):
    s.forward(1)
    s.left(1)
s.left(10)
s.forward(90)
#b letter
s.penup()
s.setpos(100,10)
s.pendown()
s.right(90)
s.forward(1)
s.right(90)
s.forward(230)
s.backward(230)
s.left(90)
s.forward(1)
for x in range(185):
    s.forward(1)
    s.right(1)
s.left(180)
for x in range(175):
    s.forward(1)
    s.right(1)
#a letter
s.penup()
s.setpos(210,10)
s.pendown()
s.left(120)
s.forward(180)
s.backward(180)
s.right(45)
s.forward(180)
s.backward(75)
s.left(105)
s.forward(90)
turtle.done()

