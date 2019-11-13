# -*- coding:UTF-8 -*-

# 多态和继承inheritance
# 多态：同一个方法，不同的行为
# 对于不同的类，可以有同名的两个（或多个）方法
# 取决于这些方法分别应用到哪个类，它们可以有不同的行为

# 计算不同形状的面积，如三角形和正方形，创建两个类
class Triangle:
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def getArea(self):
		area = self.width * self.height / 2.0
		return area

class Square:
	def __init__(self, size):
		self.size = size

	def getArea(self):
		area = self.size * self.size
		return area

myTriangle = Triangle(4, 5)
mySquare = Square(7)
print myTriangle.getArea()
print mySquare.getArea()