# -------- list ------------

# name1 = input("Enter a name: ")
# name2 = input("Enter a name: ")
# name3 = input("Enter a name: ")
# ...
# print(name1)
# print(name2)
# print(name3)
# ...

# ages = [None] * 4 # 四个空元素
# k = 0
# ages[k] = 3
# ages[k + 1] = 4
# ages[k + 2] = 5
# ages[k + 3] = 6

# ages = []
# ages.append(3)
# ages.append(4)
# ages.append(5)
# ages.append(6)

# a = [None] * 3
# a[2] = 9
# b = 0
# a[b] = a[2] + 4
# a[b + 1] = a[0] + 5
# print(a)

# l = [1,2,3]
# print(l[50]) #IndexError: list index out of range

#Alter the value of an existing element 
# l = [1,2,3]
# l[1] = 999
# print(l)

# l = (1,2,3)
# l[1] = 999 #TypeError: 'tuple' object does not support item assignment
# print(l)

# --------- for -------------
# l = [1,2,3]
# for i in range(3):
# 	print(l[i])

# for i in range(3):
# 	l[i] = l[i] * 3
# 	print(l[i])

# for i in l:
# 	print(i)

# for i in l[::-1]:
# 	print(i)

# for i in l:
# 	i *= 2
# 	print(l[i]) # 3 + error

# exercise
# sum------------
# n = (1,2,3)
# total = 0
# for i in range(3):
# 	total += n[i]
# print(total)

# for i in n:
# 	total += i
# print(total)

# import math
# total = math.fsum(n)
# print(total)

# nixu words-----------
# n = [None] * 3
# for i in range(3):
# 	n[i] = input()
# for i in range(2, -1, -1):
# 	print(n[i])

# n = []
# for i in range(3):
# 	n.append(input())
# for j in n[::-1]:
# 	print(j)

# nixu numbers--------
# ELEMENTS = 5
# values = []
# for i in range(ELEMENTS):
# 	values.append(float(input()))
# for value in values[::-1]:
# 	if value > 0:
# 		print(value)

# sum-----------------
# ELEMENTS = 5
# values = [None] * ELEMENTS
# for i in range(ELEMENTS):
# 	values[i] = float(input("Enter a value: "))
# total = 0
# for i in range(ELEMENTS):
# 	total += values[i]
# print(total)

# ELEMENTS = 5
# values = [None] * ELEMENTS
# total = 0
# for i in range(ELEMENTS):
# 	values[i] = float(input("Enter a value: "))
# 	total += values[i]
# print(total)

# import math
# ELEMENTS = 5
# values = []
# for i in range(ELEMENTS):
# 	values.append(float(input("Enter a value: ")))
# total = math.fsum(values)
# print(total)

# average
# ELEMENTS = 3
# values = []
# for i in range(ELEMENTS):
# 	values.append(float(input("Enter a value: ")))
# total = 0
# for i in range(ELEMENTS):
# 	total += values[i]
# average = total / ELEMENTS
# if average < 10:
# 	print("Average value is less than 10")


# import math
# ELEMENTS = 3
# values = []
# for i in range(ELEMENTS):
# 	values.append(float(input("Enter a value: ")))
# if math.fsum(values) / ELEMENTS < 10:
# 	print("Average value is less than 10")

# element!=int(element)----------------
# ELEMENTS = 3
# a = []
# for i in range(ELEMENTS):
# 	a.append(float(input("Enter a value for element " + str(i) + ": ")))
# for i in range(ELEMENTS):
# 	if a[i] != int(a[i]):
# 		print("A real found at index:", i)

# range(1, ELEMENTS, 2)
# ELEMENTS = 5
# values = []
# for i in range(ELEMENTS):
# 	values.append(float(input("Enter a value for element " + str(i) + \
# 		": ")))
# for i in range(1, ELEMENTS, 2):
# 	print(values[i])

# ELEMENTS = 5
# values = []
# for i in range(ELEMENTS):
# 	values.append(float(input("Enter a value for element " + str(i) + \
# 		": ")))
# for i in values[1:ELEMENTS:2]:
# 	print(i)


# --------- dict ----------------
# dict = {0: "a", 1: "b", 2: "c"}
# dict[3] = "d"
# print(dict)

# for -------------------
# stuedent = {"first_name": "Ann", "last_name": "Fox", \
# 			"age": 15, "class": "3rd"}
# for item in stuedent:
# 	print(item, stuedent[item])

# grades = {"a": "A+", "b": "B+", "c": "C+", "d": "D+"}
# for item, grade in grades.items():
# 	print(item, grade)


# salaries = {"a": 5000, \
# 			"b": 6000, \
# 			"c": 7000, \
# 			"d": 8000}
# for title in salaries:
# 	salaries[title] += 2000 # alter the value
# 	print(title, salaries[title])
# print(salaries)

# for title, salary in salaries.items():
# 	salary += 2000 # no alter the value
# 	print(title, salary)
# print(salaries)


# del---list/tuple/dict------------
l = [1,2,3,4,5]
# print(l[1])
# del l[1]
# print(l)
# print(l[1])

# del l[1:3]
# print(l)

# del l[:]
# print(l)

# grades = {"a": "A+", "b": "B+", "c": "C+", "d": "D+"}
# del grades["b"]
# print(grades)

# len----------------
# print(len(l))

# length = len(l[2:4])
# print(length)

# for i in range(len(l)):
# 	print(l[i], end = " ")

# max/min------------
# print(max(l))

# maximum = max(l[1:3])
# print(maximum)

# w = ("a", "b", "c")
# print(max(w))

# sort/sorted----------
# l = [3,4,9,2,6,7]
# l.sort()
# l.sort(reverse = True)
# print(l)

# l2 = sorted(l, reverse = True)
# # print(l)
# # print(l2)

# for element in l2:
# 	print(element, end = " ")

# for element in sorted(l):
# 	print(element, end = " ")

# exercise
# 1.max of two list's elements--------
# ELEMENTS = 3
# a = [None] * ELEMENTS
# b = [None] * ELEMENTS

# for i in range(ELEMENTS):
# 	a[i] = float(input("Enter a number A:"))

# for i in range(ELEMENTS):
# 	b[i] = float(input("Enter a number B:"))

# new_list = [None] * ELEMENTS
# for i in range(ELEMENTS):
# 	if a[i] > b[i]:
# 		new_list[i] = a[i]
# 	else:
# 		new_list[i] = b[i]

# for element in new_list:
# 	print(element)

# 2.snow days-----------------
# DAYS = 3
# t = [None] * DAYS
# for i in range(DAYS):
# 	t[i] = int(input("Enter the temp: "))

# for i in range(DAYS):
# 	if t[i] < 36:
# 		print(i + 1, end = "\t")

# 3.would you snow?----------
# for i in range(DAYS):
# 	if t[i] < 36:
# 		print("There was a possibility of snow in January!")
##### no no no
# 1st method----
# count = 0
# for i in range(DAYS):
# 	if t[i] < 36:
# 		count += 1

# if count > 0:
# 	print("There was a possibility of snow in January!")

# 2nd method-----
# flag = False
# for i in range(DAYS):
# 	if t[i] < 36:
# 		flag = True

# if flag == True:
# 	print("There was a possibility of snow in January!")

# ########## a few of data structures ###########
# 1.average of score > 89------
# STUDENTS = 3
# names = [None] * STUDENTS
# grades_lesson1 = [None] * STUDENTS
# grades_lesson2 = [None] * STUDENTS
# grades_lesson3 = [None] * STUDENTS

# for i in range(STUDENTS):
# 	names[i] = input("Enter student name No" + str(i + 1) + ": ")
# 	grades_lesson1[i] = int(input("Enter grade for lesson 1: "))
# 	grades_lesson2[i] = int(input("Enter grade for lesson 2: "))
# 	grades_lesson3[i] = int(input("Enter grade for lesson 3: "))

# for i in range(STUDENTS):
# 	total = grades_lesson1[i] + grades_lesson2[i] + grades_lesson3[i]
# 	average = total / 3.0
# 	if average > 89:
# 		print(names[i])

# 2.table of score--------
# STUDENTS = 3
# grades_table = {"A": "90-100", "B": "80-89", "C": "70-79", \
# 				"D": "60-69", "E": "0-59", "F": "0-59"}
# names = [None] * STUDENTS
# grades = [None] * STUDENTS

# for i in range(STUDENTS):
# 	names[i] = input("Enter student name No" + str(i + 1) + ": ")
# 	grades[i] = input("Enter his or her grade: ")

# for i in range(STUDENTS):
# 	# grade = grades[i]
# 	# grade_as_percentage = grades_table[grade]

# 	# print(names[i], grade_as_percentage)
# 	print(names[i], grades_table[grades[i]])

# 3.1 the lake's depths ------------
# LAKES = 3
# depths = [None] * LAKES
# for i in range(LAKES):
# 	depths[i] = float(input("Enter depth of lake: "))

# # maximum = depths[0]
# # for i in range(1, LAKES):
# # 	if depths[i] > maximum:
# # 		maximum = depths[i]

# maximum = max(depths)

# print(maximum)

# 3.2 the best depthe lake-------
# LAKES = 3
# names = [None] * LAKES
# depths = [None] * LAKES

# for i in range(LAKES):
# 	names[i] = input("Enter lake name: ")
# 	depths[i] = float(input("Enter depth of lake: "))

# maximum = depths[0]
# m_name = names[0]
# for i in range(1, LAKES):
# 	if depths[i] > maximum:
# 		maximum = depths[i]
# 		m_name = names[i]

# print(m_name)

# 3.3 the lake of msg----------
# LAKES = 2
# names = [None] * LAKES
# depths = [None] * LAKES
# countries = [None] * LAKES
# areas = [None] * LAKES

# for i in range(LAKES):
# 	names[i] = input("Enter lake name: ")
# 	depths[i] = float(input("Enter depth of lake: "))
# 	countries[i] = input("Enter country name: ")
# 	areas[i] = float(input("Enter area of lake: "))

# maximum = depths[0]
# # m_name = names[0]
# # m_country = countries[0]
# # m_area = areas[0]
# index_of_max = 0
# for i in range(1, LAKES):
# 	if depths[i] > maximum:
# 		maximum = depths[i]
# 		# m_name = names[i]
# 		# m_country = countries[i]
# 		# m_area = areas[i]
# 		index_of_max = i

# # print(maximum, m_name, m_country, m_area)
# print(depths[index_of_max], names[index_of_max], \
# 	countries[index_of_max], areas[index_of_max])

# 4.the shortest student-------------
# STUDENTS = 3
# names = [None] * STUDENTS
# heights = [None] * STUDENTS
	
# for i in range(STUDENTS):
# 	names[i] = input("Enter name for student No " + \
# 					str(i + 1) + ": ")
# 	heights[i] = float(input("Enter his or her heights: "))

# minimum = min(heights)

# print("The following students have got the shortest height:")
# for i in range(STUDENTS):
# 	if heights[i] == minimum:
# 		print(names[i])

# ############ search data ############

# 1.search the same first name-------
# PEOPLE = 3
# first_name = [None] * PEOPLE
# last_name = [None] * PEOPLE

# for i in range(PEOPLE):
# 	first_name[i] = input("Enter first name: ")
# 	last_name[i] = input("Enter last name: ")

# needle = input("Enter a first name to search: ")

# found = False
# for i in range(PEOPLE):
# 	if first_name[i] == needle:
# 		print(last_name[i])
# 		found = True
# if found == False:
# 	print("No one found!")

# 2.SSN
PEOPLE = 3
SSNs = [None] * PEOPLE
first_name = [None] * PEOPLE
last_name = [None] * PEOPLE

for i in range(PEOPLE):
	SSNs[i] = input("Enter SSN: ")
	first_name[i] = input("Enter first name: ")
	last_name[i] = input("Enter last name: ")

needle = input("Enter an SSN to search: ")

found = False
for i in range(PEOPLE):
	if SSNs[i] == needle:
		print(first_name[i], last_name[i])
		found = True
		break

if found == False:
	print("Nothing found!")




















