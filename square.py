import turtle
square=turtle.Screen()
square.bgcolor("light green")
pen=turtle.Turtle()

num_sides=4
side_length=100
angle=90

for i in range(num_sides):
    pen.forward(side_length)
    pen.right(angle)

turtle.done()


