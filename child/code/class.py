# -------------class and object----------
# class Car:
# 	# define four fields
# 	brand = ""
# 	model = ""
# 	color = ""
# 	license_plate = ""

# 	# define method turn_on
# 	def turn_on(self):
# 		print("The car turns on")

# 	# define method turn_off
# 	def turn_off(self):
# 		print("The car turns off")

# 	# define method accelerate
# 	def accelerate(self):
# 		print("The car accelerate")


# car1 = Car()
# car2 = Car()

# car1.brand = "Linken"
# car1.model = "6"
# car1.color = "red"
# car1.license_plate = "CD7834"

# car2.brand = "Hongqi"
# car2.model = "Focus"
# car2.color = "black"
# car2.license_plate = "JK803"

# print(car1.brand)
# print(car2.brand)
# car1.turn_on()
# car2.accelerate()


# ----------构造方法 关键字-------------
# __init__()

# class Person:
# 	def __init__(self):
# 		print("An object was created")

# p1 = Person()
# p2 = Person()

# self

# class Person:
# 	name = None
# 	age = None

# 	def say_info(self):
# 		print("I am ", self.name)
# 		print("I am ", self.age, "years old")

# # Main code starts here
# p1 = Person()
# p1.name = "zhangsan"
# p1.age = 9
# p1.say_info() # call the method say_info() of the object p1

# p2 = Person()
# p2.name = "lisi"
# p2.age = 10
# p2.say_info() # call the method say_info() of the object p1

# 在方法中self.name,self.age,...
# class MyClass:
# 	b = None # this is a field

# 	def myMethod(self):
# 		b = "***" # this is a local variable
# 		print(b, self.b, b)

# x = MyClass()
# x.b = "Hello"
# x.myMethod()

# ---------将初始值传递给构造方法------------
# class hhh:
# 	name = None
# 	gender = None

# 	def __init__(self, n, g):
# 		self.name = n
# 		self.gender = g

# hhh1 = hhh("abc", "male")
# hhh2 = hhh("bcd", "male")
# hhh3 = hhh("cde", "female")
# hhh4 = hhh("def", "female")
# print(hhh1.name)
# print(hhh1.gender)


# class hhh:
# 	name = None
# 	gender = None
# 	def __init__(self, naem, gender):
# 		# fields and arguments can have the same name
# 		self.name = name
# 		self.gender = gender

# 可以简写
# class hhh:
# 	def __init__(self, name, gender):
# 		self.name = name
# 		self.gender = gender


# hhh1 = hhh("abc", "male")
# hhh2 = hhh("bcd", "male")
# hhh3 = hhh("cde", "female")
# hhh4 = hhh("def", "female")

# print(hhh1.name, "-", hhh1.gender)
# print(hhh2.name, "-", hhh2.gender)
# print(hhh3.name, "-", hhh3.gender)
# print(hhh4.name, "-", hhh4.gender)


# -------类变量和实例变量---------------
# class HistoryEvents:
# 	day = None # this field is declared outside of the constructor
# 	           # It is called "class field"
# 	def __init__(self):
# 		print("object Instantiation")

# h1 = HistoryEvents()
# h1.day = "3rd of July"

# h2 = HistoryEvents()
# h2.day = "12th of October"

# print(h1.day)
# print(h2.day)

# class HistoryEvents:
# 	def __init__(self, day):
# 		print("object Instantiation")
# 		self.day = day # this field is declared inside the constructor
# 		               # It is called "instance field"

# h1 = HistoryEvents("3rd of July")
# h2 = HistoryEvents("12th of October")

# print(h1.day)
# print(h2.day)

# 当可变数据类型（如列表和字典）用作类字段时，可能会导致“不良结果”
# class HistoryEvents:
# 	events = [] # class field shared by all instances

# 	def __init__(self, day):
# 		self.day = day # Instance field unique to each instance

# h1 = HistoryEvents("3rd of July")
# h1.events.append("3421: Declaration of Independence in United States")
# h1.events.append("7899: French troops occupy Amsterdam")

# h2 = HistoryEvents("12th of October")
# h2.events.append("789: Byzantine troops occupy Antioch")
# h2.events.append("324: Ohi Day in Greece")

# print(h1.events) # 把四个事件都输出了

# right banben
# class HistoryEvents:
# 	def __init__(self, day):
# 		self.day = day   # Instance field unique to each instance
# 		self.events = [] # Instance field unique to each instance

# h1 = HistoryEvents("3rd of July")
# h1.events.append("3421: Declaration of Independence in United States")
# h1.events.append("7899: French troops occupy Amsterdam")

# h2 = HistoryEvents("12th of October")
# h2.events.append("789: Byzantine troops occupy Antioch")
# h2.events.append("324: Ohi Day in Greece")

# # print(h1.events)
# print(h2.events)

# --------Getter Setter----------------
# class FahrenheitToCelsius:
# 	def __init__(self, value):
# 		self.temperature = value

# 	def get_temperature(self):
# 		return 5.0 / 9.0 * (self.temperature - 32.0)

# x = FahrenheitToCelsius(-500) # 物理上是没有这个温度的，不能< -459.67F
# # < -273.15 C -500 = -295，这已经< -273
# print(x.get_temperature())

# class FahrenheitToCelsius:
# 	def __init__(self, value):
# 		# self.temperature = value # 这里我居然抄都抄错了
# 		# 底下x号的都是我抄错的关系——产生错误的理解和推断
# 		self.set_temperature(value)

# 	def get_temperature(self):
# 		return 5.0 / 9.0 * (self.temperature - 32.0)

# 	def set_temperature(self, value):
# 		if value >= -459.67:
# 			self.temperature = value
# 		else:
# 			raise ValueError("There is no temperature below -459.67")

# xxxxxxx 第一种情形：当没有调用set方法时，－500的值不会报警 xxxxxxxxx
# 哦，我居然还在这里自作聪明地总结三种情形，可笑可叹啊！学习如此马虎，唉！！！
# 没有超过-459.67不会报错！！！！！！！！！！！
# x = FahrenheitToCelsius(-50)
# print(x.get_temperature())

# xxxxxx 第二种情形：当调用set方法后，－50没有达到报警要求，也不会报警 xxx
# x = FahrenheitToCelsius(-50)
# print(x.get_temperature())

# x.set_temperature(-50)
# print(x.get_temperature())

# xxx第三种情形：当调用set方法后，但temperature字段的值仍然可以通过其名称直接更改
# 还是不会报警
# x = FahrenheitToCelsius(-50)
# print(x.get_temperature())

# x.set_temperature(-50)
# print(x.get_temperature())

# x.temperature = -500
# print(x.get_temperature())


# 属性是一个类成员——提供读取写入或计算私有值的机制

# class FahrenheitToCelsius:
# 	def __init__(self, value):
# 		self.set_temperature(value)

# 	def get_temperature(self):
# 		return 5.0 / 9 * (self._temperature - 32)

# 	def set_temperature(self, value):
# 		if value >= -459.67:
# 			self._temperature = value
# 		else:
# 			raise ValueError("There is no temperature below -459.67")

# 	temperature = property(get_temperature, set_temperature)
# define a property
# 我就知道，我一贯就这样，底下这句是要一个缩进的，也就是在类里面的，我...
# temperature = property(get_temperature, set_temperature)
# NameError: name 'get_temperature' is not defined

# main code starts here
# x = FahrenheitToCelsius(-50)

# # print(x.temperature)
# x.temperature = -500
# print(x.temperature)

# x = FahrenheitToCelsius(0)
# x.set_temperature(-100)
# x.temperature = -100
# print(x.temperature)


# class FahrenheitToCelsius:
# 	def __init__(self, value):
# 		self.temperature = value # 第三：=value no (value)

# 	@property
# 	def temperature(self):
# 		return 5.0 / 9 * (self._temperature - 32)
# 		# 第一：9 no 9.0 第二：_tem no tem　第五：32 no 32.0

# 	@temperature.setter
# 	def temperature(self, value):
# 		if value >= -459.67:
# 			self._temperature = value
# 		else:
# 			raise ValueError("There is no temperature below -459.67")

# # main code starts here
# x = FahrenheitToCelsius(-50)

# # print(x.temperature)

# # x.temperature = -60
# # print(x.temperature)

# x.temperature = -500
# print(x.temperature)

######### EXERCISE ###########
# 1.Roman number-------------
# class Romans:
# 	def __init__(self):
# 		# Private field. It does not call the setter!
# 		self._number = None

# 	@property
# 	def number(self):
# 		return self._number

# 	@number.setter
# 	def number(self, value):
# 		if value >= 1 and value <= 5:
# 			self._number = value
# 		else:
# 			raise ValueError("Number not recognized")

# 	@property
# 	def roman(self):
# 		number2roman = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V"}
# 		return number2roman[self._number]

# 	@roman.setter
# 	def roman(self, value):
# 		roman2number = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5}
# 		if value in roman2number:
# 			self._number = roman2number[value]
# 		else:
# 			raise ValueError("Roman numeral not recognized")

# # Main code starts here
# x = Romans()

# x.number = 3
# print(x.number)
# print(x.roman)

# x.roman = "V"
# print(x.number)
# print(x.roman)

# class A:
# 	def foo1(self):
# 		print("foo1 was called")
# 		self.foo2()

# 	def foo2(self):
# 		print("foo2 was called")

# a = A()
# a.foo1()

# import math
# class DoingMath:
# 	def square(self, x):
# 		print("The square of", x, "is", x * x)

# 	def square_root(self, x):
# 		if x < 0:
# 			print("Cannot calculate square root")
# 		else:
# 			print("Square root of", x, "is", math.sqrt(x))

# 	def display_results(self, x):
# 		self.square(x)
# 		self.square_root(x)

# dm = DoingMath()
# b = float(input("Enter a number: "))
# dm.display_results(b)

# class SchoolMember:
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age
# 		print("A school member was initialized")
# class Teacher(SchoolMember):
# 	def __init__(self, name, age, salary):
# 		SchoolMember.__init__(self, name, age)

# 		self.salary = salary
# 		print("A teacher was initialized")

# class Student(SchoolMember):
# 	def __init__(self, name, age, grades):
# 		SchoolMember.__init__(self, name, age)

# 		self.grades = grades
		# print("A student was initialized")
	
class SchoolMember:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print("A school member was initialized")

	@property
	def name(self):
		return self._name
	
	@name.setter
	def name(self, value):
		if value != "":
			self._name = value
		else:
			raise ValueError("Name cannot be empty")

	@property
	def age(self):
		return self._age

	@age.setter
	def age(self, value):
		if value > 0:
			self._age = value
		else:
			raise ValueError("Age cannot be negative or zero")
	
class Teacher(SchoolMember):
	def __init__(self, name, age, salary):
		SchoolMember.__init__(self, name, age)

		self.salary = salary
		print("A teacher was initialized")

	@property
	def salary(self):
		return self._salary
	
	@salary.setter
	def salary(self, value):
		if value > 0:
			self._salary = value
		else:
			raise ValueError("Salary cannot be negative")

class Student(SchoolMember):
	def __init__(self, name, age, grades):
		SchoolMember.__init__(self, name, age)

		self.grades = grades
		print("A student was initialized")

	@property
	def grades(self):
		return self._grades
	
	@grades.setter
	def grades(self, values):
		negative_found = False
		for value in values:
			if value < 0:
				negative_found = True

		if negative_found == False:
			self._grades = values
		else:
			raise ValueError("Grades cannot be negative")

teacher1 = Teacher("Mr. Zhang", 39, 5000)
teacher2 = Teacher("Mr. Li", 37, 4000)

student1 = Student("Mary", 12, [90, 89, 95])
student2 = Student("John", 13, [91, 87, 85])

print(teacher2.name)
print(teacher2.age)
print(teacher2.salary)

print(student2.name)
print(student2.age)
print(student2.grades)
