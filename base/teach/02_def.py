# def get_sum(num1, num2):
# 	result = num1 + num2
# 	return result

# def get_sum(num1, num2):
# 	return num1 + num2

# def get_sum_dif(num1, num2):
# 	s = num1 + num2
# 	d = num1 - num2
# 	return s, d

# func_name()
# 1
# def cube(num):
# 	result = num ** 3
# 	return result

# x = float(input("Num: "))
#  # the 1st
# cb = cube(x)
# y = cb + 1 / x
# print(y)
# # the 2nd
# y = cube(x) + 1 / x
# print(y)
# # the 3rd
# print(cube(x) + 1 / x)

# 2-1
# def get_msg():
# 	msg = "How do you do?"
# 	return msg

# print("Nice to meet you!")
# a = get_msg()
# print(a)

# 2-2
# def display(color):
# 	msg = "There is " + color + " in the rainbow"
# 	return msg
# print(display("red"))
# print(display("yellow"))
# print(display("blue"))

# 2-3
# def display(color, exists):
# 	neg = ""
# 	if exists == False:
# 		neg = "n't any"
# 	return "There is" + neg + " " + color + " in the rainbow"

# print(display("red", True))
# print(display("yellow", True))
# print(display("black", False))

# 2-4
# def get_fullname():
# 	first_name = input("Enter first name: ")
# 	last_name = input("Enter last name: ")
# 	return first_name, last_name

# fname, lname = get_fullname()
# print("First name:", fname)
# print("Last name:", lname)

# ########## no return #############

# def display_sum(num1, num2):
# 	result = num1 + num2
# 	print(result)

# use the no return
# 1
# def display_line():
# 	print("----------------------------")
# print("Hello Python!")
# display_line()
# print("Nice to study you!")
# display_line()
# print("Would you like Coffow?")
# display_line()

# 2
# def display_line(length):
# 	for i in range(length):
# 		print("-", end = "")
# 	print()

# print("Hello Python!")
# display_line(15)
# print("Nice to study you!")
# display_line(18)
# print("Would you like Coffow?")
# display_line(22)

# 形参和实参
# def divide(n1, n2):
# 	result = n1 / n2
# 	return result

# x = float(input("Enter a number 1: "))
# y = float(input("Enter a number 2: "))

# w = divide(x, y)

# print(w)

# how func work?------------
# def maximum(n1, n2):
# 	m = n1
# 	if n2 > m:
# 		m = n2
# 	return m
# a = float(input("Enter number1: "))
# b = float(input("Enter number2: "))

# c = maximum(a, b)
# print(c)

# sameVarName--------------
# def f1():
# 	sameVarName = 1
# 	print(sameVarName)
# def f2(sameVarName):
# 	print(sameVarName)
# sameVarName = 3
# print(sameVarName)
# f1()
# f2(2)
# print(sameVarName)

# def f1(test):
# 	test += 1
# 	print(test)

# test = 5
# f1(test)
# print(test)

# func use func--------------
# def add(n1, n2):
# 	result = n1 + n2
# 	return result

# def display_sum(n1, n2):
# 	print(add(n1, n2))

# a = int(input("Enter number1: "))
# b = int(input("Enter number2: "))

# display_sum(a, b)

# default argument----------
# def prepend_title(name, title = "Mr"):
# 	return title + " " + name
# print(prepend_title("zhangsan"))
# print(prepend_title("liping", "Ms"))

# def prepend_title(first_name, last_name, title = "Mr", reverse = False):
# 	if reverse == False:
# 		return title + " " + first_name + " " + last_name
# 	else:
# 		return title + " " + last_name + " " + first_name
# print(prepend_title("John", "King"))
# print(prepend_title("Maria", "Myles", "Ms"))
# print(prepend_title("Maria", "Myles", "Ms", True))
# print(prepend_title("John", "King", reverse = True))

# (no) global -----------------
# def display_val():
# 	test = 9
# 	print(test)

# test = 8
# display_val()
# print(test)

# def display_val():
# 	print(test)
# 	#UnboundLocalError: local variable 'test' referenced before assignment
# 	test = 9
# 	print(test)

# test = 8
# display_val()
# print(test)

# def display_val():
# 	global test
# 	print(test)
# 	test = 9
# 	print(test)

# test = 8
# display_val()
# print(test)

# def display_val():
# 	a = 8
# 	b = 3
# 	print(a, b)

# def display_other_val():
# 	b = 2
# 	print(a, b)

# a = 15
# print(a)
# display_val()
# display_other_val()
# print(a)

# exercise
# 1.
# def total(a, b):
# 	s = a + b
# 	return s
# n1 = float(input("Enter number1: "))
# n2 = float(input("Enter number2: "))

# result = total(n1, n2)
# print("The sum of", n1, "+", n2, "is", result)

# 2.convert one to one
# def display_menu():
# 	print("1. Convert USD to EUR")
# 	print("2. Convert EUR to USD")
# 	print("3. Exit")
# 	print("-----------------------")
# 	print("Enter a choice: ", end = "")

# while True:
# 	display_menu()
# 	choice = int(input())

# 	if choice == 3:
# 		print("Bye!")
# 		break
# 	else:
# 		amount = float(input("Enter an amount: "))
# 		if choice == 1:
# 			print(amount, "USD = ", amount * 0.94, "EUR")
# 		else:
# 			print(amount, "EUR = ", amount / 0.94, "USD")

# 3.
# def display_menu():
# 	print("1. Convert USD to EUR")
# 	print("2. Convert USD to GBP")
# 	print("3. Convert USD to JPY")
# 	print("4. Convert USD to CAD")
# 	print("5. Exit")
# 	print("-----------------------")
# 	print("Enter a choice: ", end = "")

# def USD_to_EUR(value):
# 	return value * 0.94
# def USD_to_GBP(value):
# 	return value * 0.79
# def USD_to_JPY(value):
# 	return value * 113
# def USD_to_CAD(value):
# 	return value * 1.33

# while True:
# 	display_menu()
# 	choice = int(input())

# 	if choice == 5:
# 		print("Bye!")
# 		break
# 	else:
# 		amount = float(input("Enter an amount in US dollars: "))
# 		if choice == 1:
# 			print(amount, "USD = ", USD_to_EUR(amount), "EUR")
# 		elif choice == 2:
# 			print(amount, "USD = ", USD_to_GBP(amount), "GBP")
# 		elif choice == 3:
# 			print(amount, "USD = ", USD_to_JPY(amount), "JPY")
# 		elif choice == 4:
# 			print(amount, "USD = ", USD_to_CAD(amount), "CAD")

# 4.average
# def tst_int(n):
# 	if n == int(n):
# 		return True
# 	else:
# 		return False

# total = 0
# count = 0
# a = float(input("Enter a number: "))
# while tst_int(a) == True:
# 	if a > 0:
# 		total += a
# 		count += 1
# 	a = float(input("Enter a number: "))
# if count > 0:
# 	print(total / count)

# 5.zhisaizi
import random
ELEMENTS = 100
def dice():
	return random.randrange(1, 7)

def search_and_count(x, a):
	count = 0
	for i in range(ELEMENTS):
		if a[i] == x:
			count += 1
	return count

a = [None] * ELEMENTS

for i in range(ELEMENTS):
	a[i] = dice()

x = int(input("Enter a number 1-6: "))
print("Given value exists in the list")
print(search_and_count(x, a), "times")





		
		


















