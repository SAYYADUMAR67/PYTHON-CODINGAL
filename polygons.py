import turtle
turtle.Screen().bgcolor("lightblue")
turtle.Screen().title("Polygons")
turtle.Screen().screensize(800, 600)
num_sides = 6
side_length = 80
angle = 360 / num_sides
for i in range(num_sides):
    turtle.forward(side_length)
    turtle.right(angle)

turtle.done()
