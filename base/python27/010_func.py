# -*- coding:UTF-8 -*-

# 时间：20191112
# 课题：函数 P150
# 分析：把程序分解成较小的部分有3种方法
#	函数就象是代码的积木——反复地使用
# 	对象把程序中的各部分描述为自包含的单元
#	模块包含程序各部分的单独的文件

# 函数可以任意调用
# def printMyAddress():
# 	print "张三"
# 	print "1号，长安街"
# 	print "天安门，北京"
# 	print "邮编 100000"
# 	print

# printMyAddress()
# printMyAddress()
# printMyAddress()
# printMyAddress()

# 参数是你交给函数的一条信息
# 灵活更改人名，其它不变
# def printMyAddress(name):
# 	print name
# 	print "1号，长安街"
# 	print "天安门，北京"
# 	print "邮编 100000"
# 	print

# printMyAddress("李四")

# 传递部分（调用函数）时——实参argument
# 接收部分（函数内部）时——形参parameter
# 向街道上的每个人发信，人名和门牌号就要变化
# def printMyAddress(name, num):
# 	print name
# 	print num+"号",
# 	print "长安街"
# 	print "天安门，北京"
# 	print "邮编 100000"
# 	print

# printMyAddress("李四", "1")
# printMyAddress("王五", "2")
# printMyAddress("赵六", "3")
# printMyAddress("钱七", "4")

# 更多的参数：把所有参数集中到一个列表传递给函数！！！

# 函数返回的值：结果result或返回值return value
def calculateTax(price, tax_rate):
	taxTotal = price + (price * tax_rate)
	return taxTotal

# totalPrice = calculateTax(7.99, 0.06)
# print totalPrice
# total = calculateTax(7.99, 0.06) + calculateTax(6.59, 0.08)
# print total

# 创建和使用有返回值的函数
# def calculateTax(price, tax_rate):
# 	total = price + (price * tax_rate)
# 	# print my_price # 打印全局变量
# 	# my_price = 888 # 新的局部变量
# 	# print my_price
# 	global my_price # 强制为全局变量
# 	my_price = my_price + 8
# 	print my_price
# 	return total

# my_price = float(raw_input("Enter a price: "))
# totalPrice = calculateTax(my_price, 0.06)
# print "price = ", my_price, "Total price = ", totalPrice

# 函数运行时，函数之外的名字被搁置一边没有用到；只有函数内部的名字会被用到
# 程序中使用（或可使用）变量的部分——这个变量的作用域
# 局部变量
# print price # 打印这个变量会报错，为什么？？？

# 全局变量global variable

# 强制为全局变量

# excise
# def fozu():
# 	print "                            _ooOoo_               "
# 	print "                           o8888888o               "
# 	print "                           88  .  88              "
# 	print "                           (| -_- |)                   "
# 	print "                            O\\ = /O                    "
# 	print "                        ____/`---'\\____               "
# 	print "                      .   ' \\| |// `.             "
# 	print "                       / \\||| : |||// \\          "
# 	print "                     / _||||| -:- |||||- \\          "
# 	print "                       | | \\\\\\ - /// | |            "
# 	print "                     | \\_| ''\\---/'' | |           "
# 	print "                      \\ .-\\__ `-` ___/-. /           "
# 	print "                   ___`. .' /--.--\\ `. . __            "
# 	print "                ."" '< `.___\\_<|>_/___.' >'"".         "
# 	print "               | | : `- \\`.;`\\ _ /`;.`/ - ` : | |     "
# 	print "                 \\ \\ `-. \\_ __\\ /__ _/ .-` / /     "
# 	print "         ======`-.____`-.___\\_____/___.-`____.-'======  "
# 	print "                            `=---='  "
# 	print
# 	print "      ......................阿弥陀佛.......................  "

# fozu()

# def l(name, addr, street, city, sheng, post, country):
# 	print name
# 	print addr
# 	print street
# 	print city
# 	print sheng
# 	print post
# 	print country

# l('lisi', 5, 'changanjie', 'beijing', 'Beijing', 100000, 'China')

def oh(wu, er, yi):
	print wu
	print er
	print yi
	
	# return "total is ${0}".format(wu*5+er*2+yi)
	print "total is $",
	return wu * 5 + er * 2 + yi

total = oh(3, 4, 5) # 函数返回值必须赋值给一个变量名，再打印
print total
