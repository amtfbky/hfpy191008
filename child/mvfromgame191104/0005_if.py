# -*- coding:utf-8 -*-
# age = float(raw_input("Enter your age: "))
# grade = int(raw_input("Enter your grade: "))
# color = raw_input("Enter your color: ")
# if age >= 8 and grade >= 3:
# 	if color == "red" or color == "blue" or color == "green":
# 		print "You can play this game."
# else:
# 	print "Sorry, you can't play this game."

# excise
# 1.if n<=10,n*%10; if n>=10,n*%20, 各折？最终价格？
# n = int(raw_input("Enter n: "))

# if n <= 10:
# 	print n * 0.1, n - n * 0.1
# elif n >= 10:
# 	print n * 0.2, n - n * 0.2

# 2.10~12的女孩可加入足球队，如果不是女孩就不必询问年龄。
# bie = raw_input("Enter your bie: ")

# if bie == 'f':
# 	age = int(raw_input("Enter your age: "))
# 	if 10 <= age <= 12:
# 		print "Welcome to join us."
# 	else:
# 		print "Sorry, you more than 12."
# else:
# 	print "Sorry!"

# 3.你到达一个加油站，距下一个加油站还有200Km，看是否在这个站还是下一个站加油。
# 分析：油箱容积？还有油％？多少Km/升？包含5升的缓冲区防止油表不准
# tankSize = int(raw_input("Size of tank: "))
# percentFull = int(raw_input("Percent full: "))
# kmPerLiter = int(raw_input("km per liter: "))
# another = int(tankSize * percentFull * 0.01 * kmPerLiter)
# print """Size of tank: {0},
# 	percent full: {1},
# 	km per liter: {2},
# 	You can go another {3} km,
# 	The next gas station is 200 km away.""".format(tankSize,
# 		percentFull,
# 		kmPerLiter,
# 		another)
# if another > 200:
# 	# print "You can go another {0}".format(another)
# 	print "You can wait for the next station."
# else:
# 	# another += kmPerLiter * 5
# 	# print "You can go another {0}".format(another)
# 	print "Get gas now!"

# 4.if code=="123",run a App or print "You're right!"
import secret
code = str(raw_input("Enter code: "))
if code == "123":
	secret.guessN()
else:
	print "No..."
