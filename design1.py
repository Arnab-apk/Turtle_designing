import turtle
import colorsys

# Set up screen
screen = turtle.Screen()
screen.bgcolor("black")

# Turtle setup
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)
turtle.colormode(255)

# Color settings
h = 0

# Draw Mandala Pattern
for i in range(36):
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()

    # Color cycle using HSV
    h += 0.025
    r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(h, 1, 1)]
    pen.pencolor(r, g, b)

    for j in range(6):
        pen.forward(100)
        pen.right(60)
    pen.right(10)  # rotate each iteration

# Hide turtle and end
pen.hideturtle()
turtle.done()
