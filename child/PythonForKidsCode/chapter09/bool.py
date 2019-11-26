# print(bool(0))
# print(bool(3))
# print(bool(323.33))
# print(bool(-10))
# print(bool(None))
# print(bool('a'))
# print(bool(' '))
# print(bool('what do you call a pig doing karate? Pork Chop!'))
# 你管练空手道的猪叫什么?猪排!

# silly_list = [] # tuple and dict also False
# print(bool(silly_list))

year = input("Year of birth: ")
if not bool(year.rstrip()):
	print("You need to enter a value for your year of birth.")
