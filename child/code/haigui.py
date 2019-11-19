import turtle
# import random
# a = int(input("Enter the length of the base: "))
# b = int(input("Enter the length of the height: "))

# wn = turtle.Screen()
# george = turtle.Turtle()
# george.shape("turtle")
# turtle.delay(50)

# rect-----------
# george.forward(a)
# george.left(90)
# george.forward(b)
# george.left(90)
# george.forward(a)
# george.left(90)
# george.forward(b)

# zhijiao sanjiaoxing-----
# george.forward(100)
# george.setheading(270)
# george.forward(100)
# george.setheading(135)
# george.forward(141)

# Draw a triangle---------
# george.forward(100)
# george.left(120)
# george.forward(100)
# george.left(120)
# george.forward(100)
# george.left(120)

# Draw a house-----------
# Change pen's color to blue
# george.color("blue")
# george.forward(200)
# george.left(90)
# george.forward(100)
# george.left(90)
# george.forward(200)
# george.left(90)
# george.forward(100)

# # Move George to the top left corner of the tectangle
# george.penup() # Pull pen up
# george.backward(100)
# george.pendown() # Pull pen down

# # Draw the red roof
# george.setheading(45)
# # george.left(135)
# george.color("red")
# george.forward(141)
# george.right(90)
# george.forward(141) # 141?

# goto-------------
# george.goto(-200, 100)

# Draw a x------------
# george.goto(-100, 200)
# george.goto(0, 0)
# george.goto(-100, -200)
# george.goto(0, 0)
# george.goto(100, -200)
# george.goto(0, 0)
# george.goto(100, 200)
# george.goto(0, 0)

# Change pen's size to 5 pixels
# george.pensize(5)

############### for ###################
wn = turtle.Screen()
george = turtle.Turtle()
george.shape("turtle")
turtle.delay(50)

# rect slowly-----------------
# for i in range(4):
# 	george.forward(50)
# 	george.left(90)

# Move the turtle to pole position
# george.penup()
# george.backward(200)
# george.pendown()

# # First square
# for i in range(4):
# 	george.forward(50)
# 	george.left(90)

# # Move the turtle to pole position
# # where next square will be drawn
# george.penup()
# george.forward(100)
# george.pendown()

# # second square
# for i in range(4):
# 	george.forward(50)
# 	george.left(90)

# george.penup()
# george.forward(100)
# george.pendown()

# rect quick-------------------
# george.penup()
# george.backward(200)
# george.pendown()

# for square in range(2):
# 	# Draw a square
# 	for i in range(4):
# 		george.forward(50)
# 		george.left(90)

# 	george.penup()
# 	george.forward(100)
# 	george.pendown()

# no same square-----------------
# george.penup()
# george.backward(330)
# george.pendown()

# for multiplier in range(1, 4):
# 	# Draw a square
# 	for i in range(4):
# 		george.forward(50 * multiplier)
# 		george.left(90)

# 	george.penup()
# 	george.forward(50 * multiplier)
# 	george.forward(30)
# 	george.pendown()

# no same house-------------------
# george.penup()
# george.backward(330)
# george.pendown()

# for multiplier in range(1, 4):
# 	# Draw a rectangle
# 	george.forward(100 * multiplier)
# 	george.left(90)
# 	george.forward(50 * multiplier)
# 	george.left(90)
# 	george.forward(100 * multiplier)
# 	george.left(90)
# 	george.forward(50 * multiplier)

# 	# Move George to the top left corner of the rectangle
# 	george.penup()
# 	george.backward(50 * multiplier)
# 	george.pendown()

# 	# Draw the roof
# 	george.setheading(45)
# 	george.forward(70.5 * multiplier)
# 	george.right(90)
# 	george.forward(70.5 * multiplier)

# 	# Move next
# 	george.penup()
# 	george.setheading(270) # 360-90=downward
# 	george.forward(50 * multiplier)
# 	george.setheading(0) # 0=forward
# 	george.forward(30)
# 	george.pendown()

# wubianxing-----------------------
# george.pensize(2)
# sides = 5
# for i in range(sides):
# 	george.forward(100)
# 	george.right(360 / sides)


# wujiaoxing-----------------------
# george.pensize(3)
# for i in range(5):
# 	george.forward(150)
# 	george.right(180 / 5 * 4)

# qijiaoxing----------------------
# george.pensize(3)
# points = 7
# for i in range(points):
# 	george.forward(150)
# 	george.right(180 / points * (points -1))

# random star----------------------
# Don't forget import random
# turtle.delay(0)
# for star in range(10):
# 	a = random.randrange(-200, 200)
# 	b = random.randrange(-200, 200)
# 	george.penup()
# 	george.goto(a, b)
# 	george.pendown()

# 	points = random.randrange(5, 23, 2)

# 	length = random.randrange(10, 100)
# 	for i in range(points):
# 		george.forward(length)
# 		george.right(180 / points * (points - 1))

# 
george.pensize(3)
flag = False
for x in range(18):
	george.forward(100)

	if flag == False:
		george.right(110)
	else:
		george.left(150)

	flag = not flag

wn.exitonclick()
