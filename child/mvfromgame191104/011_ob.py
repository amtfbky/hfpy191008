# -*- coding:UTF-8 -*-

# def oh(wu, er, yi):
# 	# sum_total = (wu * 5) + (er * 2) + yi
# 	print(wu)
# 	print(er)
# 	print(yi)
	
# 	return "total is ${0}".format(wu*5+er*2+yi)
# 	# print "total is $",
# 	# return sum_total

# n = oh(3, 4, 5) # 返回值必须赋值给一个变量，再打印
# print(n) # 这个问题让我鼓揪了好一阵

# 真实世界的真实对象（物体）包括2个方面：
#	可以对它们做什么（动作），在Python中称为方法method
#	如何描述（属性或特性），在Python中称为属性attribute
# 对象=属性+方法=>class类：对象的描述或蓝图+instance实例：用类建立的一个真正的对象
# class Ball:
# 	def __init__(self, size, color, direction):
# 	# 初始化对象
# 		self.size = size
# 		self.color = color
# 		self.direction = direction
	
# 	def __str__(self):
# 	# __str__内置方法，这里改变了内容
# 		msg = "Hi, I'm a " + self.size + " " + self.color + " ball!"
# 		return msg
	
# 	def bounce(self):
# 	# 弹跳方法
# 		if self.direction == "down":
# 			self.direction = "up"

# myBall = Ball("small", "gray", "down")
# # myBall.direction = "down"
# # myBall.color = "green"
# # myBall.size = "small"

# print "I just created a ball."
# print "My ball is", myBall.size
# print "My ball is", myBall.color
# print "My ball's direction is", myBall.direction
# print "Now I'm going to bounce the ball"
# print
# myBall.bounce()
# print "Now the ball's direction is", myBall.direction
# print myBall

# 示例类：烤热狗
# 属性
# cooked_level:烤的时间0-3生；3-5半生不熟；5-8烤好；8以上就成木炭了
# cooked_string:字符串，描述生熟程度
# condiments:配料列表，如番茄酱、芥末酱等

# 方法
# cook():烤
# add_condiment():加配料
# __init__():默认属性
# __str__():让print出来好看一些

class HotDog:
	# 未生火，热狗是生的，未加配料
	def __init__(self):
		self.cooked_level = 0
		self.cooked_string = "Raw"
		self.condiments = []

	def __str__(self):
		msg = "hot dog"
		# 加配料了
		if len(self.condiments) > 0:
			msg = msg + " with"		# hot dog with
		for i in self.condiments:
			msg = msg + i + ", "	# hot dog with xxx, xxx
		msg = msg.strip(", ")
		msg = self.cooked_string + " " + msg + "."
		return msg

	# 烤热狗
	def cook(self, time):
		# 按时间增加烤制级别
		self.cooked_level = self.cooked_level + time
		if self.cooked_level > 8:
			self.cooked_string = "Charcoal"
		elif self.cooked_level > 5:
			self.cooked_string = "Well-done"
		elif self.cooked_level > 3:
			self.cooked_string = "Medium"
		else:
			self.cooked_string = "Raw"

	# 加配料
	def addCondiment(self, condiments):
		self.condiments.append(condiments)

# 用类实例一个对象
myDog = HotDog()
# 烤前
# print myDog.cooked_level
# print myDog.cooked_string
# print myDog.condiments

# 开火4分钟，检验能否开火
# print "Now I'm going to cook the hot dog"
# myDog.cook(4)
# print myDog.cooked_level
# print myDog.cooked_string
# print myDog.condiments

# 开火，加配料，显示生熟程度
print myDog
print "Cooking hot dog for 4 minutes..."
myDog.cook(4)
print myDog
print "Cooking hot dog for 3 more minutes..."
myDog.cook(3)
print myDog
print "What happens if I cook it for 10 more minutes?"
myDog.cook(10)
print myDog
print "Now, I'm going to add some stuff on my hot dog"
myDog.addCondiment("ketchup")
myDog.addCondiment("mustard")
print myDog



		



