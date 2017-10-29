import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
maria = turtle.Turtle()
maria.color("blue")
maria.pensize(5)
maria.turtlesize(3)
maria.shape("turtle")
maria.speed(2)

for nokat in range (0,8):
	# maria.stamp()
	maria.forward(150)
	maria.left(90)

	maria.right(45)

# maria.write("Hello World")
wn.exitonclick()
