# ------ loops --------------
# a = float(input())
# b = float(input())
# c = float(input())
# d = float(input()) # if 1000

# total = a + b + c + d
# print(total)

# total = 0
# a = float(input())
# total = total + a

# a = float(input())
# total = total + a

# a = float(input())
# total = total + a

# execute_these_statements_4_times:
# # Python no this word
# 	a = float(input())
# 	total = total + a

# print(total)

# i = 1
# while i < 4:
# 	print("hi,how do you do?")
# 	i += 1

# print("Over!")

# total = 0
# i = 1
# # while i <= total_number_of_iterations:
# while i <= 4:
# 	# here goes a statement or block of statements
# 	a = float(input("Enter a number: "))
# 	total = total + a
# 	i += 1
# print(total)

# total = 0 
# i = 1
# while i <= 20:
# 	a = float(input("Enter a number: "))
# 	if a > 0:
# 		total = total + a
# 	i += 1
# print(total)

# n = int(input("How many numbers are you going to enter? "))
# total = 0
# i = 1
# while i <= n:
# 	a = float(input("Enter a number: "))
# 	total += a
# 	i += 1
# print(total)

# total = 0
# a = float(input())
# if a != -1:
# 	total += a
# 	a = float(input())
# 	if a != -1:
# 		total += a
# 		a = float(input())
# 		if a != -1:
# 			total += a
# 			a = float(input())
# 			...
# 			...
# print(total)

# total = 0
# a = float(input())
# while a != -1:
# 	total += a
# 	a = float(input())

# print(total)

# n = 1

# a = float(input())
# n *= a

# a = float(input())
# n *= a

# a = float(input())
# n *= a

# a = float(input())
# n *= a

# a = float(input())
# n *= a

# print(n)

# n = 1
# i = 1
# while i <= 5:
# 	a = float(input())
# 	n *= a
# 	i += 1
# print(n)

# for i in [1, 2, 3, 4, 5]:
# 	print(i, end = " ")

# for letter in "Python":
# 	print(letter, end = "-")

# for i in range(0, 11, 1):
# 	print(i, end = " ")
# print()

# for i in range(0, 11):
# 	print(i, end = " ")
# print()

# for i in range(11):
# 	print(i, end = " ")
# print()

# for i in range(2, 12, 2):
# 	print(i, end = " ")
# print()

# a = 11
# b = 0
# for i in range(a, b, -2):
# 	print(i, end = " ")
# print()

# a = int(input())
# for i in range(-3, 3, 2):
# 	a = a * 3
# print(a)

# a = int(input())
# for i in range(6, a - 1, -1):
# 	print(i, end = " ")
# print()

# total = 0
# for i in range(4):
# 	a = float(input("Enter a number: "))
# 	total += a
# print(total)

# n = int(input("How many numbers are you going to enter? "))
# total = 0
# for i in range(n):
# 	a = float(input("Enter number No" + str(i + 1) + ": "))
# 	total += a
# if n > 0:
# 	average = total / n
# 	print("The average value is:", average)
# else:
# 	print("You didn't enter any number!")

# ------------- loop iterations --------------------
# for i in range(1, 3):
# 	for j in range(1, 4):
# 		print(i, j)

# i = 1
# for j in range(1, 4):
# 	print(i, j)

# i = 2
# for j in range(1, 4):
# 	print(i, j)

# for i in range(3):
# 	for j in range(4):
# 		print("I love you!Mum!")

# a = 1
# i = 5
# while i <= 7:
# 	for j in range(1, 5, 2):
# 		a *= 2
# 	i += 1
# print(a)

# positives_given = 0
# a = float(input("Enter a number: ")) # 1
# while positives_given != 5:
# 	if a > 0:
# 		positives_given += 1
# 	a = float(input("Enter a number: ")) # 5
# print("positives_given:", positives_given) # 5


# positives_given = 0
# while positives_given != 5:
# 	a = float(input("Enter a number: "))
# 	if a > 0:
# 		positives_given += 1
# print("positives_given:", positives_given)

# text = "I love Mum!"
# letter = input("Enter a letter to search: ")

# found = False
# for a in text:
# 	if a == letter:
# 		found = True
# 		break
# if found == True:
# 	print("Letter", letter, "found!")

# xxxxxx error xxxxxx
# i = 1
# while i != 5:
# 	print("HI, Python!")

# i = 1
# while i != 5:
# 	print("I love Mum!")
# 	i += 2

#------- right -------
# i = 1
# while i < 5:
# 	print("I love Mum!")
# 	i += 2

# chengfabiao
# i = 1
# for j in range(1, 10):
# 	print(i, "x", j, "=", i * j, end = "\t")

# for i in range(1, 10):
# 	for j in range(1, 10):
# 		print(i, "x", j, "=", i * j, end = "\t")
# 	print()

# 1+2+3+...+100
# s = 0
# i = 1

# while i <= 100:
# 	s += i
# 	i += 1

# print(s)

# s = 0
# for i in range(1, 101):
# 	s += i

# print(s)

# 2x4x6x8x10
# p = 1
# i = 2
# while i <= 10:
# 	p *= i
# 	i += 2
# print(p)

# p = 1
# for i in range(2, 12, 2):
# 	p *= i
# print(p)

# total / count
# total = 0
# count = 0
# for i in range(4):
# 	a = float(input("Enter a number: "))
# 	if a > 0:
# 		total += a
# 		count += 1

# if count != 0:
# 	print(total / count)
# else:
# 	print("No positives entered!")

# count_a = 0
# count_b = 0

# for i in range(3):
	# a = int(input("Enter number A: "))
	# b = int(input("Enter number B: "))
# 	if a > b:
# 		count_a += 1
# 	elif b > a:
# 		count_b += 1

# print(count_a, count_b)

# count1 = 0
# count2 = 0
# count3 = 0
# for i in range(5):
# 	a = float(input("Enter a number: "))
# 	if a <= 9:
# 		count1 += 1
# 	elif a <= 99:
# 		count2 += 1
# 	else:
# 		count3 += 1
# print(count1, count2, count3)

# count = 0
# total = 0
# while total <= 1000:
# 	a = float(input("Enter a number: "))
# 	count += 1
# 	total += a
# print(count)

# answer = "yes"
# while answer.upper() == "YES":
# 	a = int(input("Enter number A: "))
# 	b = int(input("Enter number B: "))

# 	result = a ** b
# 	print("The result is:", result)

# 	answer = input("Would you like to repeat?")

# w = int(input("Enter a weight: "))
# minimum = w
# for i in range(3):
# 	w = int(input("Enter a weight: "))
# 	if w < minimum:
# 		minimum = w
# print(minimum)

# fahrenheit = 0
# while fahrenheit <= 100:
# 	kelvin = (fahrenheit + 459.67) / 1.8
# 	print("Fahrenheit:", fahrenheit, "Kelvin:", kelvin)
# 	fahrenheit += 0.5

# grains = 1
# total = 1
# for i in range(63):
# 	grains *= 2
# 	total += grains
# print(grains)
# print(total)

import random
secret_number = random.randrange(1, 101)
attempts = 1
guess = int(input("Enter a guess: "))
while guess != secret_number:
	if guess > secret_number:
		print("Your guess is bigger than my secret number.Try again.")
	else:
		print("Your guess is smaller than my secret number.Try again.")

	attempts += 1
	guess = int(input("Enter a guess: "))

print("You get it!")
print("Attempts:", attempts)














