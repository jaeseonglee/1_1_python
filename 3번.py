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

tur1.forward(100)
tur2.forward(100)
tur3.forward(100)
tur4.forward(100)

for i in range(1,41) :
    tur1.left(90)
    tur1.forward(100)
    tur2.left(90)
    tur2.forward(100)
    tur3.left(90)
    tur3.forward(100)
    tur4.left(90)
    tur4.forward(100)

    tur1.left(90)
    tur1.forward(100)
    tur2.left(90)
    tur2.forward(100)
    tur3.left(90)
    tur3.forward(100)
    tur4.left(90)
    tur4.forward(100)

    tur1.left(90)
    tur1.forward(100)
    tur2.left(90)
    tur2.forward(100)
    tur3.left(90)
    tur3.forward(100)
    tur4.left(90)
    tur4.forward(100)

    tur1.left(100)
    tur1.forward(100)
    tur2.left(100)
    tur2.forward(100)
    tur3.left(100)
    tur3.forward(100)
    tur4.left(100)
    tur4.forward(100)

    
tur1.hideturtle()
tur2.hideturtle()
tur3.hideturtle()
tur4.hideturtle()

        
