import turtle
t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor('whitesmoke')
t.hideturtle()
t.goto(0,-10)

t.pensize(3)
t.color('red')
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90,200)
t.setheading(60)
t.circle(-90,200)
t.forward(178)
t.end_fill()

t.penup()
t.goto(-65,130)
t.pendown()
t.color('White')
t.write("I Love Programming (BB)", 
font=("verdana",10,"bold"))

turtle.done()



# t.penup()
# t.goto(-220, -180)
# t.pendown()
# t.color('blue')
# t.write("BibekBB",font=("Verdana", 35,"blod"))

# turtle.done()
