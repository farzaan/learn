import turtle

def makeasquare():
	window = turtle.Screen()
	window.bgcolor("red")
	brad = turtle.Turtle()
	brad.color("pink")
	brad.shape("turtle")
	i = 4
	while (i > 0):
		brad.forward(100)
		brad.right(90)
		i -= 1
	
	
	window.exitonclick()
makeasquare() 