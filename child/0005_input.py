# -*- coding:utf-8 -*-
# import urllib  # 关于互联网的类

# print "Enter your name: ",  # 逗号用来把多个print语句合并到同一行上，且增加一个空格
# someone = raw_input()

# raw_input的简便方法
# someone = raw_input("Enter your name: ")
# print "Hi, " + someone + ", nice to meet you!"

# temp_string = raw_input()
# fahrenheit = float(temp_string)
# 以上两句可简写
# print "This program converts Fahrenheit to Celsius"
# print "Type in a temperature in Fahrenheit: "
# fahrenheit = float(raw_input())
# celsius = (fahrenheit - 32) * 5.0 / 9
# print "That is ", celsius, "degrees Celsius"

# int(xxx)把小数转换成整数
# response = raw_input("How many students are in your class: ")
# numberOfStudents = int(response)

# 从互联网上的一个文件得到输入
# file = urllib.urlopen('https://github.com/amtfbky/amtfbky.github.io/blob/master/test.txt')
# message = file.read()
# print message

# excise
# answer = raw_input()
# print type(answer)  # <type 'str'>

# 让raw_input()打印一个提示消息？？？
# print raw_input("This is a tips: ")

# 使用raw_input()得到一个整数
# print raw_input(int())  # 写反了???
# print int(raw_input())  # 3.8这样也不行

# a = raw_input()
# print int(a)  # 3.8这样还不行


# 使用raw_input()得到一个浮点数
# print raw_input(float())  # 写反了
# print float(raw_input())

# 姓名
# xing = "chen"
# ming = "zhen"
# print xing, ming

# 先问你的姓，再问你的名，然后打印出来
# xing = raw_input("What's your first name: ")
# ming = raw_input("what's your last name: ")
# print xing, ming

# 长方形房间，长多少？宽多少？再算面积
# chang = raw_input("How many the chang: ")
# kuang = raw_input("How many the kuang: ")
# print int(chang) * int(kuang)

# 接着上一题，几平方米的地毯？几平方尺？询问价格/平方尺？总价？
# mi = int(chang) * int(kuang)
# print mi, "平方米"
# chi = mi * 9
# print chi, "平方尺"
# rice = raw_input("元/平方尺：")
# allRice = int(rice) * chi
# print allRice, "元"

# 统计零钱，几个五分币？二分币？一分币？总？
wu = raw_input()
er = raw_input()
yi = raw_input()
print int(wu) * 5 + int(er) * 2 + int(yi) * 1

