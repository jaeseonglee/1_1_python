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

tur1.shapesize(1,1,5)
tur2.shapesize(1,1,3)
tur3.shapesize(1,1,3)
tur4.shapesize(1,1,3)

tur1.color('skyblue')
tur2.color('skyblue')
tur3.color('skyblue')
tur4.color('skyblue')

for i in range(1,24) :
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
    
    tur1.setposition(10-0.4*i,10+0.4*i)
    tur2.setposition(10+0.4*i,-10+0.4*i)
    tur3.setposition(-10-0.4*i,10-0.4*i)
    tur4.setposition(-10+0.4*i,-10-0.4*i)

for i in range(0,23) :
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
    
    tur1.setposition(10+0.4*i,10-0.4*i)
    tur2.setposition(10-0.4*i,-10-0.4*i)
    tur3.setposition(-10+0.4*i,10+0.4*i)
    tur4.setposition(-10-0.4*i,-10+0.4*i)

tur1.penup()
tur2.penup()
tur3.penup()
tur4.penup()

tur1.home()
tur2.home()
tur3.home()
tur4.home()

tur1.pendown()
tur2.pendown()
tur3.pendown()
tur4.pendown()

tur1.color('red')

for i in range(1,31) :
    tur1.forward(50)
    tur1.penup()
    
    tur1.home()
    tur1.pendown()
    tur1.right(12*i)

for i in range(0,13):
    if (i >= 6 ) :
        tur1.color('orange')
        tur1.penup()
        tur1.setposition(0,-50+3*i)
        tur1.pendown()
        tur1.circle(50-3*i)
    else :
        tur1.color('orange')
        tur1.penup()
        tur1.setposition(0,-50+3*i)
        tur1.pendown()
        tur1.circle(50-3*i)

  
tur1.penup()
tur2.penup()
tur3.penup()
tur4.penup()

tur1.setposition(50,50)
tur2.setposition(-50,-50)
tur3.setposition(-50,50)
tur4.setposition(50,-50)

tur1.right(180)
tur3.right(90)
tur4.left(90)

tur1.pendown()
tur2.pendown()
tur3.pendown()
tur4.pendown()

tur1.color('yellow')

tur1.forward(100)
tur2.forward(100)
tur3.forward(100)
tur4.forward(100)

for i in range(1,41) :
    if (i >= 31) :
        tur1.color('purple')
        tur2.color('purple')
        tur3.color('purple')
        tur4.color('purple')

        tur1.left(85-i*0.6)
        tur2.left(85-i*0.6)
        tur3.left(85-i*0.6)
        tur4.left(85-i*0.6)

        tur1.forward(100+i)
        tur2.forward(100+i)
        tur3.forward(100+i)
        tur4.forward(100+i)
    elif (i>= 21) :
        tur1.color('blue')
        tur2.color('blue')
        tur3.color('blue')
        tur4.color('blue')
        
        tur1.left(85-i*0.6)
        tur2.left(85-i*0.6)
        tur3.left(85-i*0.6)
        tur4.left(85-i*0.6)

        tur1.forward(100+i)
        tur2.forward(100+i)
        tur3.forward(100+i)
        tur4.forward(100+i)

    elif (i>= 11) :
        tur1.color('green')
        tur2.color('green')
        tur3.color('green')
        tur4.color('green')
        
        tur1.left(85-i*0.6)
        tur2.left(85-i*0.6)
        tur3.left(85-i*0.6)
        tur4.left(85-i*0.6)

        tur1.forward(100+i)
        tur2.forward(100+i)
        tur3.forward(100+i)
        tur4.forward(100+i)    

    elif (i>= 1) :
        tur1.color('yellow')
        tur2.color('yellow')
        tur3.color('yellow')
        tur4.color('yellow')
        
        tur1.left(85-i*0.6)
        tur2.left(85-i*0.6)
        tur3.left(85-i*0.6)
        tur4.left(85-i*0.6)

        tur1.forward(100+i)
        tur2.forward(100+i)
        tur3.forward(100+i)
        tur4.forward(100+i)
    

tur1.left(90)
tur2.left(90)
tur3.left(90)
tur4.left(90)

tur1.forward(100)
tur2.forward(100)
tur3.forward(100)
tur4.forward(100)


tur1.hideturtle()
tur2.hideturtle()
tur3.hideturtle()
tur4.hideturtle()
