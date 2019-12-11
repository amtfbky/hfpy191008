# -*- coding:utf-8 -*-

# for looper in range(5):
# 	print looper, 'x 8 = ', looper * 8

# for l in "you":
# 	print l

# 定时器
# import time
# for i in range(10, 0, -1):
# 	print i
# 	time.sleep(1)
# print "BLAST OFF!"

# 谁最酷
# for cool_guy in ["zhangsan", "lisi", "wangwu", "me"]:
# 	print cool_guy, "is the coolest guy ever!"

# while
# print "Type 3 to continue, anything else to quit."
# someInput = raw_input()
# while someInput == '3':
# 	print "Thank you for the 3. Very kind of you."
# 	print "Type 3 to continue, anything else to quit."
# 	someInput = raw_input()
# print "That's not 3, so I'm quitting now."

# continue/break，很少用到
# for i in range(1, 6):
# 	print
# 	print 'i =', i,
# 	print 'Hello, how',
# 	if i == 3:
# 		# continue
# 		break
# 	print 'are you today?'

# excise
# for i in range(1, 6, 2):
# 	print i, "--Hello"

# 哪个关键字停止循环的当前迭代，提前跑到下一次迭代？？？

# n如果没有变成整数，就是一个字符串，n*9=nnnnnnnnn
n = int(raw_input("Which multiplication table would you like?\n"))
h = int(raw_input("How high do you want to go?\n"))
print "Here's your table:"
for i in range(1, h+1):
	print n, 'x', i, '=', i * n

# n = int(raw_input("Which multiplication table would you like?\n"))
# h = int(raw_input("How high do you want to go?\n"))
# print "Here's your table:"
# i = 1
# while i < (h+1):
# 	print n, 'x', i, '=', i * n
# 	i += 1