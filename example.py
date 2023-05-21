import turtle
import random

# Set up screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create turtle
space_turtle = turtle.Turtle()
space_turtle.speed(0)
space_turtle.hideturtle()

# Function to draw a star
def draw_star(turtle, size):
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()

# Function to draw a circle (for our planet)
def draw_planet(turtle, size, color):
    turtle.penup()
    turtle.goto(0, -size)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()

# Function to draw a spaceship
def draw_spaceship(turtle, size):
    turtle.penup()
    turtle.goto(-size/2, -size*2)
    turtle.color("grey")
    turtle.pendown()
    turtle.begin_fill()

    for _ in range(2):
        turtle.forward(size)
        turtle.right(60)
        turtle.forward(size)
        turtle.right(120)
    turtle.right(60)
    turtle.forward(size)

    turtle.end_fill()

# Draw multiple stars
space_turtle.color("white")
for _ in range(50):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    size = random.randint(5, 20)
    space_turtle.penup()
    space_turtle.goto(x, y)
    space_turtle.pendown()
    draw_star(space_turtle, size)

# Draw a planet
draw_planet(space_turtle, 100, "blue")

# Draw a spaceship
draw_spaceship(space_turtle, 100)

# End
turtle.done()
