import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)  # Fastest drawing speed

# Function to draw a circle with different colors
def draw_circle(radius, color):
    t.color(color)
    t.circle(radius)

# Function to create the abstract art design
def draw_abstract_art():
    colors = ["red", "blue", "green", "yellow", "purple", "orange"]
    for i in range(36):
        draw_circle(100, colors[i % len(colors)])  # Draw circle with changing colors
        t.left(10)  # Rotate the turtle to create the pattern

# Main function to draw the abstract art
def draw_design():
    draw_abstract_art()

# Call function to draw the design
draw_design()

# Hide the turtle after drawing
t.hideturtle()

# Finish the drawing
turtle.done()
