# -*- coding:utf-8 -*-

import random

def guessN():
	secret = random.randint(1, 100)
	guess = 0
	tries = 0

	print "让我们来猜一个数字，它从1到99，给你6次机会。"

	# 如果玩家...
	# 注意缩进！
	while guess != secret and tries < 6:
		guess = input("请输入一个数字： ")
		if guess < secret:
			print "小了，往大的猜！"
		elif guess > secret:
			print "大了，往小的猜！"
		tries = tries + 1  # 用掉一次机会

	if guess == secret:
		print "你猜到了，真棒！"
	else:
		print "不能再猜了！希望你下次好运！"
		print "这秘密的数字是： ", secret