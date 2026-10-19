import math
from turtle import *

# Function to calculate the x-coordinate of a point on the heart curve
def heart_x(k):
    return 15 * math.sin(k)**3

# Function to calculate the y-coordinate of a point on the heart curve
def heart_y(k):
    return 12 * math.cos(k) - 5 * math.cos(2*k) - 2 * math.cos(3*k) - math.cos(4*k)

# Set up turtle graphics
speed(0)        # fastest drawing
bgcolor("black")
color("#D00D0D")
pensize(2)
hideturtle()

tracer(5, 0)

# Draw the heart shape using radial strokes
for i in range(610):
    k = i / 100  # smooth parametric increment
    x = heart_x(k) * 20
    y = heart_y(k) * 20

    penup()
    goto(0, 0)   # start at center
    pendown()
    goto(x, y)   # draw stroke outward
    goto(0, 0)   # return to center

done()