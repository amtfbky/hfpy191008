# -*- coding:UTF-8 -*-

import random
# print random.randint(0, 100)
# print random.random() # 介于0-1之间的小数
# print random.random() * 10 # 介于1-10之间的小数

# excise
"""
s = 'hEllo wOrld'
s
Out[3]: 'hEllo wOrld'
s.upper()#全部大写
Out[4]: 'HELLO WORLD'
s
Out[5]: 'hEllo wOrld'
s.lower()#全部小写
Out[6]: 'hello world'
s
Out[7]: 'hEllo wOrld'
s.capitalize()#首字母大写
Out[8]: 'Hello world'
s
Out[9]: 'hEllo wOrld'
s.title()#每个词首字母大写
Out[10]: 'Hello World'
s
Out[11]: 'hEllo wOrld'

#大变小小变大
s.swapcase()
Out[15]: 'HeLLO WoRLD'

----判断----
s.isupper()
Out[12]: False
s.islower()
Out[13]: False
s.istitle()
Out[14]: False
"""
# def upperLetter():
# 	l = raw_input("Enter your name: ")
# 	ll = l.upper()
# 	print ll
# upperLetter()

# 生成1到20之间的5个随机整数的列表，并打印出来
# # 很笨拙的办法
# def randomFive():
# 	l = []
# 	l.append(random.randint(1, 20))
# 	l.append(random.randint(1, 20))
# 	l.append(random.randint(1, 20))
# 	l.append(random.randint(1, 20))
# 	l.append(random.randint(1, 20))
# 	print l

# randomFive()

# 一句搞定
# print random.sample(range(1, 20), 5)

# 利用迭代
# l = []
# for i in range(5):
# 	l.append(random.randint(1, 20))
# print l

# 工作30秒，每3秒打印一个随机小数

# import time
# for i in range(10):
# 	time.sleep(0.1)
# 	print random.random()


