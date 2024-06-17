import turtle


window = turtle.Screen()
window.bgcolor('white')

# This code makes a new Turtle. Pick a new name for the turtle
animal = turtle.Turtle()

# Make your turtle's shape 'turtle', .shape('turtle')
animal.shape('turtle')
# Set your turtle's speed using .speed(2)
animal.speed(2)
# Set your turtle's color using .color('green') and .pencolor('blue')
animal.color('purple')
animal.pencolor('blue')
# Move your turtle forward using .forward(100)
# TEST    Did your turtle move forward?
animal.forward(100)
# Move your turtle left or right using .left(90) or .right(90)
animal.left(90)
# Now put the forward and left/right code into a for loop to repeat 4 times.
# TEST    Did your turtle draw a square?
for i in range (4):
    animal.forward(100)
    animal.left(90)
# Move your turtle to a new place on the screen using .goto(x, y)
# x=0 and y=0 is the center of the screen
animal.goto(8,8)
# Have your turtle draw a circle using .circle(radius, steps=30)
# TEST    Did your turtle draw a circle?
animal.begin_fill()
animal.circle(20, steps=30)
# Add color to your shape by adding .begin_fill() before drawing the circle
# and .end_fill() below
animal.end_fill()
# Draw 3 more shapes with different fill colors!
animal.begin_fill()
for i in range (3):
    animal.forward(60)
    animal.left(40)
animal.goto(7,7)
animal.end_fill()

animal.begin_fill()
for i in range(3):
    animal.forward (80)
    animal.right(60)
animal.goto(10,10)
animal.end_fill()

animal.begin_fill()
for i in range(10):
    animal.forward (100)
    animal.left(100)
animal.goto(12,12)
animal.end_fill()

# ===================== DO NOT EDIT THE CODE BELOW ============================
turtle.done()
