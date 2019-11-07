# -*- coding:utf-8 -*-

"""
1.str(3)，把数字变成字符串
2.不能改变变量的赋值，只能把标签贴在新的变量
3.变量名大小写敏感
4.'Python'与"Python"一样
5.'3' == 3为False
6.2Teacher，这个变量名是错的
7."8"是字符串
"""
# 1.创建一个变量，并赋值，print
a = 3
print a

# 2.改变这个变量：替换新值，或旧值加量
a = 4
print a
a += 1
print a

# 3.创建一个变量，并赋给一个字符串，print
a = 'hello world!'
print a

# 4.计算一周多少分钟？用三个变量相乘
daysPerWeek = 7
hoursPerDay = 24
minutesPerHour = 60
minutes = daysPerWeek * hoursPerDay * minutesPerHour
print minutes

# 5.如果一天有26个小时，则一周有多少分钟？
daysPerWeek = 7
hoursPerDay = 26
minutesPerHour = 60
minutes = daysPerWeek * hoursPerDay * minutesPerHour
print minutes
