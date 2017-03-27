import turtle

def makeashape():
	window = turtle.Screen()
	window.bgcolor("red")
	brad = turtle.Turtle()
	brad.color("pink")
	brad.shape("turtle")
	brad.speed(10)
	i = 36
	while(i > 0):
		brad.right(10)
		for w in [1,2,3,4]:
			brad.forward(100)
			brad.right(90)
		i -= 1
	biell = turtle.Turtle()
	biell.shape("arrow")
	biell.color("blue")
	biell.speed(8)
	biell.circle(200)
	
	RJ = turtle.Turtle()
	RJ.color("black")
	b = 3
	while(b > 0):
		RJ.forward(200)
		RJ.left(120)
		b -= 1
	

	window.exitonclick()
makeashape() 