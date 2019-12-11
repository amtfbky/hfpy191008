# name1 = "张三"
# name2 = "李四"
# print(name1, "是个坏小子，", name2, "也是个坏种")

# print("求和2+3=：", 2 + 3)

# print("3rd", "July", "2019")
# print("3rd", "July", "2019", sep = "/")

# name = "Mary"
# print("hello", name, end = ";")
# print("hi", name, end = ";")
# print("how do you do?", name, end = ".")

# print("how do you do?\nI'm fine.\nAnd you?")

# print("1\tone\n2\ttwo")

# name = input("What's your name? ")
# print("Hello,", name)

# name = input("name: ")
# age = int(input("age: "))
# defen = float(input("defen: "))
# print(type(defen))
# print(name, "age: ", age, "defen: ", defen)

# a = "Hello, "
# b = "nice to meet you!"
# c = a + b
# print(c)

# a = "Hello, "
# a += "nice to meet you!"
# print(a)

# # Data input - Prompt the user to enter values for base and height
# base = float(input("Enter the length of Base: "))
# height = float(input("Enter the length of Height: "))

# # Data processing - Calculate the area of the rectangle
# area = base * height

# # Results output - Display the result on user's screen
# print("The area of the rectangle is", area)

# # Data input - Prompt the user to enter a value for radius
# radius = float(input("Enter the length of Radius: "))

# # Data processing - Calculate the area of the circle
# area = 3.14159 * radius ** 2

# # Results output - Display the result on user's screen
# print("The area of the circle is", area)

# # Data input - Prompt the user to enter a temperature value
# # in degrees Fahrenheit
# fahrenheit = float(input("Enter a temperature in Fahrenheit: "))

# # Data processing - Calculate the degrees Celsius equivalent
# celsius = 5 / 9 * (fahrenheit -32)

# # Results output - Display the result on user's screen
# print("The temperature in Celsius is", celsius)

# a = 8.9
# b = int(a)
# print(b)

# print(int(89))
# print(int(8.9))
# print(int(-8.9))

# c = "8"
# d = "9"
# print(c + d)
# print(int(c) + int(d))

# a = 1
# b = 2
# c = 3
# d = 4
# e = max(a, b, c, d)
# print(e)

# print(max(1, 2, 3, 4))

# seq = [1, 2, 3, 4]
# print(max(seq))

# a = "2.2"
# b = "3.3"
# print(a + b)
# print(float(a) + float(b))

# # Assign sequence [1, 2, 3, 4, 5] to variable a
# a = range(1, 6)

# # Assign sequence [0, 1, 2, 3, 4, 5] to variable b
# b = range(6)

# # Assign sequence [0, 10, 20, 30, 40] to variable c
# c = range(0, 50, 10)

# # Assign sequence [100, 95, 90, 85] to variable d
# d = range(100, 80, -5)

# import random # import random module

# # Display a random integer between 10 and 100
# print(random.randrange(10, 101))

# # Assign a random integer between 0 and 10 to variable x
# x = random.randrange(11)
# # and display it
# print(x)

# # Display a random integer between -20 and 20
# print(random.randrange(-20, 21))

# # Display a random odd integer between 1 and 97
# print(random.randrange(1, 99, 2))

# # Display a random even integer between 0 and 98
# print(random.randrange(0, 100, 2))

# import math

# seq = [2.2, 3, 4]
# print(math.fsum(seq))

# import math

# print(math.sqrt(9))
# print(math.sqrt(81))

# s = "abcdefghijklmnopqrstuvwxyz"
# print(s[0])
# print(s[9])
# print(s[25])
# print(s[-1])
# print(s[-26])

# name = "Mary"
# letter1, letter2, letter3, letter4 = name
# print(letter1)
# print(letter2)
# print(letter3)
# print(letter4)

# n = "123456789"
# print(n[3:6]) # 456
# print(n[:6]) # 123456
# print(n[6:]) # 789
# print(n[2:8:2]) # 357
# print(n[6:-2]) # 7
# print(n[-6:-3]) # 456
# print(n[-6:]) # 456789
# print(n[:-3]) # 123456

# ex:reversed
# s = "abcd"
# s_reversed = s[3] + s[2] + s[1] + s[0]
# print(s_reversed)

# s = "abcd"
# a, b, c, d = s
# s_reversed = d + c + b + a
# print(s_reversed)

# s = "abcd"
# s_reversed = s[::-1]
# print(s_reversed)

# replace
# a = "I am newbie in Go. Python rocks!"
# b = a.replace("Go", "C++")
# print(b)
# print(a)

# len
# a = "abcd efg hik, lmn32"
# print(len(a))

# b = "opq rst uv, wxyz543"
# c = len(b)
# print(c)

# find
# a = "I am newbie in Python rocks!"
# i = a.find("newbie")
# print(i)
# print(a.find("Python"))
# print(a.find("rocks"))

# a = "What's Your Name?"
# b = a.lower()
# print(b)
# print(a)

# c = a.upper()
# print(c)
# print(a)

# d = a.replace("Your", "his").upper()
# print(d)
# print(a)

# str(number)
# age = int(input("Enter your age: "))
# new_age = age + 5
# msg = "You'll be " + str(new_age) + " years old in 5 years from now."
# print(msg)

# ex:login_id
# import random
# last_name = input("Enter your name: ")

# # Get a random integer between 100 and 999
# random_int = random.randrange(100, 1000)

# # Create login ID
# login_id = last_name[:3].upper() + str(random_int)
# print(login_id)

# find+切换名字顺序
# full_name = input("Enter your full name: ")

# # Find the position of space character. This is also the number
# # of characters first name contains
# space_pos = full_name.find(" ")

# # Get space_pos number of characters starting from position 0
# name1 = full_name[:space_pos]

# # Get the rest of the characters starting from position space_pos + 1
# name2 = full_name[space_pos + 1:]

# full_name = name2 + " " + name1
# print(full_name)

# import random
# a = "abcdefghijklmnopqrstuvwxyz"
# random_letter1 = a[random.randrange(26)]
# random_letter2 = a[random.randrange(26)]
# random_letter3 = a[random.randrange(26)]
# random_letter4 = a[random.randrange(26)]
# random_word = random_letter1 + random_letter2 + \
# 				random_letter3 + random_letter4
# print(random_word)


# import random
# a = "abcdefghijklmnopqrstuvwxyz"
# random_letter1 = a[random.randrange(len(a))]
# random_letter2 = a[random.randrange(len(a))]
# random_letter3 = a[random.randrange(len(a))]
# random_letter4 = a[random.randrange(len(a))]
# random_word = random_letter1 + random_letter2 + \
# 				random_letter3 + random_letter4
# print(random_word)


# if
# age = int(input("Enter your age: "))

# if age < 18:
# 	print("You are underage!")
# 	print('You have to wait foe a few more years.')

# name = input("Enter your name of an olympian: ")

# if name == "Zeus":
# 	print("You are the king of the Gods!")

# print("You live on Mount olympian.")

# a = int(input())

# b = 3
# if a * 2 > 6:
# 	b = a * 3
# 	a = a * 2

# print(b, a)

# # 找出体重最轻的人，不使用min()
# w1 = int(input("Enter the weight of the 1st person: "))
# w2 = int(input("Enter the weight of the 2nd person: "))
# w3 = int(input("Enter the weight of the 3rd person: "))
# w4 = int(input("Enter the weight of the 4th person: "))
# # memorize the weight of the first person
# minimum = w1

# # If second one is lighter, forget everything and memorize this weight
# if w2 < minimum:
# 	minimum = w2
# # If third one is lighter, forget everything and memorize this weight
# if w3 < minimum:
# 	minimum = w3
# # If fourth one is lighter, forget everything and memorize this weight
# if w4 < minimum:
# 	minimum = w4

# print(minimum)

# # min()
# print(min(w1, w2, w3, w4))

# 找出体重最重的人的名字
# w1 = int(input("Enter the weight of the 1st person: "))
# n1 = input("Enter the name of the person: ")
# w2 = int(input("Enter the weight of the 2nd person: "))
# n2 = input("Enter the name of the 2nd person: ")
# w3 = int(input("Enter the weight of the 3rd person: "))
# n3 = input("Enter the name of the 3rd person: ")

# maximum = w1
# m_name = n1 # this variable holds the name of the heaviest person

# if w2 > maximum:
# 	maximum = w2
# 	m_name = n2 # Someone else is heavier, Keep his or her name.

# if w3 > maximum:
# 	maximum = w3
# 	m_name = n3 # Someone else is heavier, Keep his or her name.

# print("The heaviest person is", m_name)
# print("His or her weight is", maximum)

# if-else
# age = int(input("Enter your age: "))
# if age >= 18:
# 	print("You are an adult!")
# else:
# 	print("You are underage!")

# excise
# a = int(input()) # 3 -3 0
# if a > 0:
# 	print("Positive")
# else:
# 	print("Negative")


# maximum
# a = float(input("Enter number A: "))
# b = float(input("Enter number B: "))

# fangfa1
# if b > a:
# 	maximum = b
# else:
# 	maximum = a

# print("Greatest value:", maximum)

# fangfa2
# maximum = a
# if b > a:
# 	maximum = b

# print("Greatest value:", maximum)

# fangfa3
# maximum = max(a, b)
# print("Greatest value:", maximum)


# Gallons and liters
# COEFFICIENT = 3.785

# print("1: Gallons to liters")
# print("2: Liters to gallons")
# choice = int(input("Enter choice: "))

# quantity = float(input("Enter quantity: "))

# if choice == 1:
# 	result = quantity * COEFFICIENT
# 	print(quantity, "gallons =", result, "liters")
# else:
# 	result = quantity / COEFFICIENT
# 	print(quantity, "liters =", result, "gallons")

# if-elif
# a = int(input())
# b = int(input())

# if a > 3:
# 	print("Message #1")
# elif a > 1 and b <= 10:
# 	print("Message #2")
# 	print("Message #3")
# elif b == 0:
# 	print("Message #4")
# else:
# 	print("Message #5")

# print("The end!")

# 0~999
# a = int(input("Enter an integer (0 - 999): "))

# # if a <= 9:
# # 	count = 1
# # elif a <= 99:
# # 	count = 2
# # else:
# # 	count = 3

# # print("You entered a ", count, "-digit number", sep = "")


# if a < 0 or a > 999:
# 	print("Wrong number!")
# elif a <= 9:
# 	print("You entered a 1-digit number")
# elif a <= 99:
# 	print("You entered a 2-digit number")
# else:
# 	print("You entered a 3-digit number")

# 1~7,Sunday,Monday,...
# day = int(input("Enter a number between 1 and 7: "))

# if day == 1:
# 	print("Sunday")
# elif day == 2:
# 	print("Monday")
# elif day == 3:
# 	print("Tuesday")
# elif day == 4:
# 	print("Wednesday")
# elif day == 5:
# 	print("Thursday")
# elif day == 6:
# 	print("Friday")
# elif day == 7:
# 	print("Saturday")
# else:
# 	print("Invalid Number")

# M C T
# v = input("Enter the type of vehicle (M, C, T): ")

# if v == "M":
# 	print("You need to pay $1")
# elif v == "C":
# 	print("You need to pay $2")
# elif v == "T":
# 	print("You need to pay $3")
# else:
# 	print("Invalid vehicle")

# －－－－－－nested if-elif structure－－－－－－－－－－
# a = int(input("Enter a number: "))
# if a < 1 or a > 3:
# 	print("Invalid Number")
# else:
# 	print("Valid Number")

# 	if a == 1: # this is the nested if-elif structure
# 		print("1st choice selected")
# 	elif a == 2:
# 		print("2nd choice selected")
# 	else:
# 		print("3rd choice selected")

# a = int(input())
# b = 10
# if a < 30:
# 	if a < 15:
# 		b = b + 2
# 	else:
# 		b -= 1
# else:
# 	b += 1

# print(b)

# a = float(input("Enter a number: "))

# if a > 0:
# 	print("Positive")
# else:
# 	if a < 0:
# 		print("Negative")
# 	else:
# 		print("Zero")

# if a > 0:
# 	print("Positive")
# elif a < 0:
# 	print("Negative")
# else:
# 	print("Zero")

# a = float(input("Enter 1st number: "))
# op = input("Enter type of operation: ") # Variable op is of type string
# b = float(input("Enter 2nd number: "))

# if op == "+":
# 	print(a + b)
# elif op == "-":
# 	print(a - b)
# elif op == "*":
# 	print(a * b)
# elif op == "/":
# 	if b == 0:
# 		print("Error: Division by zero")
# 	else:
# 		print(a / b)