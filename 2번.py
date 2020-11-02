import turtle

tur1 = turtle.Turtle()
tur2 = turtle.Turtle()
tur3 = turtle.Turtle()
tur4 = turtle.Turtle()

tur1.speed(100)
tur2.speed(100)
tur3.speed(100)
tur4.speed(100)

tur1.shape('turtle')
tur2.shape('turtle')
tur3.shape('turtle')
tur4.shape('turtle')



tur1.shapesize(1,1,3)
tur2.shapesize(1,1,3)
tur3.shapesize(1,1,3)
tur4.shapesize(1,1,3)

tur1.color('blue')
tur4.color('red')

for i in range(1,101) :
    tur1.forward(30)
    tur1.penup()
    
    tur1.home()
    tur1.pendown()
    tur1.right(3.6*i)

for i in range(0,5):
    tur1.penup()
    tur1.setposition(0,-50+5*i)
    tur1.pendown()
    tur1.circle(50-5*i)
    
tur2.right(60)
tur3.right(120)
tur4.right(180)


for i in range(0,40) :
    tur1.penup()
    tur2.penup()
    tur3.penup()
    tur4.penup()
    
    tur1.setposition(100-4*i,100+4*i)
    tur2.setposition(100+4*i,-100+4*i)
    tur3.setposition(-100-4*i,100-4*i)
    tur4.setposition(-100+4*i,-100-4*i)
    
    tur1.pendown()
    tur2.pendown()
    tur3.pendown()
    tur4.pendown()
    
    tur1.setposition(30-0.4*i,30+0.4*i)
    tur2.setposition(30+0.4*i,-30+0.4*i)
    tur3.setposition(-30-0.4*i,30-0.4*i)
    tur4.setposition(-30+0.4*i,-30-0.4*i)

for i in range(0,40) :
    tur1.penup()
    tur2.penup()
    tur3.penup()
    tur4.penup()
    
    tur1.setposition(100+4*i,100-4*i)
    tur2.setposition(100-4*i,-100-4*i)
    tur3.setposition(-100+4*i,100+4*i)
    tur4.setposition(-100-4*i,-100+4*i)
    
    tur1.pendown()
    tur2.pendown()
    tur3.pendown()
    tur4.pendown()
    
    tur1.setposition(30+0.4*i,30-0.4*i)
    tur2.setposition(30-0.4*i,-30-0.4*i)
    tur3.setposition(-30+0.4*i,30+0.4*i)
    tur4.setposition(-30-0.4*i,-30+0.4*i)
    
tur1.hideturtle()
tur2.hideturtle()
tur3.hideturtle()
tur4.hideturtle()
