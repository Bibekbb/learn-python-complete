import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("skyblue")  # Set the background color to light blue

# Create a turtle object for drawing
pen = turtle.Turtle()
pen.speed(3)

# Function to draw a mountain
def draw_mountain(x, y, size):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.fillcolor("gray")
    pen.begin_fill()
    for _ in range(3):
        pen.forward(size)
        pen.left(120)
    pen.end_fill()

# Function to draw a tree
def draw_tree(x, y):
    # Draw tree trunk
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.fillcolor("brown")
    pen.begin_fill()
    for _ in range(2):
        pen.forward(10)
        pen.left(90)
        pen.forward(30)
        pen.left(90)
    pen.end_fill()

    # Draw tree leaves
    pen.penup()
    pen.goto(x - 20, y + 30)
    pen.pendown()
    pen.fillcolor("green")
    pen.begin_fill()
    pen.circle(20)
    pen.end_fill()

# Function to draw the river
def draw_river():
    pen.penup()
    pen.goto(-300, -100)
    pen.pendown()
    pen.fillcolor("blue")
    pen.begin_fill()
    pen.setheading(0)
    pen.forward(600)
    pen.right(90)
    pen.forward(100)
    pen.right(90)
    pen.forward(600)
    pen.right(90)
    pen.forward(100)
    pen.end_fill()

# Draw the landscape scene
draw_mountain(-100, 100, 200)  # Draw mountain on the left
draw_mountain(50, 100, 200)  # Draw mountain on the right
draw_tree(-150, -50)  # Draw tree on the left side
draw_tree(100, -50)  # Draw tree on the right side
draw_river()  # Draw river at the bottom

# Hide the turtle and finish
pen.hideturtle()

# Keep the window open until clicked
screen.exitonclick()
