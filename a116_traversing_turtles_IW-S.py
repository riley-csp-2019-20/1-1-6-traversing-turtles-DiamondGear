#   a116_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []



# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  my_turtles.append(t)

# set the starting point of the turtle 
startx = 0
starty = 0

# 
for t in my_turtles:
	t.penup()
	t.goto(startx, starty)
	t.pendown()
	t.left(45)
	t.forward(30)
	
	

	
#	
	startx = t.xcor()
	starty = t.ycor()
wn = trtl.Screen()
wn.mainloop()
