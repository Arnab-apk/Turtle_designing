import turtle
import colorsys

# Set up screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create turtle
t = turtle.Turtle()
t.speed(0)
turtle.colormode(255)
t.pensize(2)

# Color settings
hue = 0
n = 36  # number of petals
radius = 120

# Draw pattern
for i in range(360):
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    rgb = tuple(int(c * 255) for c in color)
    t.pencolor(rgb)
    t.forward(i * 0.5)
    t.left(59)
    t.circle(radius, 60)
    hue += 0.005

# Hide turtle and exit on click
t.hideturtle()
turtle.done()
