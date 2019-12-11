# -*- coding:UTF-8 -*-

# 从其它类继承属性或方法的类，叫派生类derived class或子类subclass
# 游戏：
#	玩家一路上捡起不同的东西，如食物、金币或衣服
#	建一个类，GameObject，有name等属性和pickUp()等方法
#	为金币建立一个子类Coin，它自动有name等属性和pickUp()等方法
#	Coin类还需要一个value属性和一个spend()方法

# "空"函数或方法——代码桩code stub
# 计划，用于编写比较复杂的代码
class GameObject:
	def __init__(self, name):
		self.name = name

	def pickUp(self, player):
		"""
		put code here to add the object to the player's
		collection
		"""
		pass

class Coin(GameObject):
	def __init__(self, value):
		GameObject.__init__(self)
		self.value = value

	def spend(self, buyer, seller):
		"""
		put code here to remove the coin from the buyer's
		money and add it to the seller's money
		"""
		pass