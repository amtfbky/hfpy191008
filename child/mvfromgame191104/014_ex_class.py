# -*- coding:UTF-8 -*-

# 属性：帐户名、帐号、余额；方法：存钱、取钱、显示余额
# class BankAccount:
# 	def __init__(self, name, num, yue):
# 		self.name = name
# 		self.num = num
# 		self.yue = yue

# 	def __str__(self):
# 		msg = self.name + "，帐号：" + \
# 		str(self.num) + " 存了" + \
# 		str(self.cun) + "元；取了" + \
# 		str(self.qu) + "元；余额" + \
# 		str(yue2) + "元。"
# 		return msg

# 	def Cun(self, cun):
# 		self.cun = cun
# 		return self.cun

# 	def Qu(self, qu):
# 		self.qu = qu
# 		return self.qu

# 	def Yue(self):
# 		global yue2
# 		yue2 = self.yue + self.cun - self.qu
# 		return yue2

# some = BankAccount('lisi', 123456789, 50)
# print some.Cun(1000)
# print some.Qu(100)
# print some.Yue()
# print some

# 子类InterestAccount，计算利息，每年调用一次并更新余额
class BankAccount:
	def __init__(self, name, num, yue):
		self.name = name
		self.num = num
		self.yue = yue

	def __str__(self):
		msg = self.name + "，帐号：" + \
		str(self.num) + " 存了" + \
		str(self.cun) + "元；取了" + \
		str(self.qu) + "元；余额" + \
		str(yue2) + "元；"
		return msg

	def Cun(self, cun):
		self.cun = cun
		return self.cun

	def Qu(self, qu):
		self.qu = qu
		return self.qu

	def Yue(self):
		global yue2
		yue2 = self.yue + self.cun - self.qu
		return yue2
class InterestAccount(BankAccount):
	def __init__(self, tax_Interest):
		# BankAccount.__init__(self)
		self.tax_Interest = tax_Interest

	def __str__(self):
		# 这里要调用父类的属性self.name和self.num，怎么办？？？
		msg = "结息余额 " + str(yue3) + " 元。"
		return msg

	def addInterest(self):
		global yue3
		yue3 = yue2 + yue2 * self.tax_Interest

some = BankAccount('lisi', 123456789, 10000)
lixi = InterestAccount(0.001)
some.Cun(1000)
some.Qu(100)
some.Yue()
lixi.addInterest()
print some
print lixi
