# -*- coding:utf-8 -*-

# for multiplier in range (5, 8):
# 	for i in range (1, 11):
# 		print i, 'x', multiplier, '=', i * multiplier
# 	print

# numStars = int(raw_input ("How many stars do you want?"))
# # for i in range (1, numStars + 1): # 想打印5颗星，第一种方法：把numStars + 1
# for i in range (0, numStars): # 第二种方法：把起始数改为0
# 	print '*',

# numLines = int(raw_input ('How many lines of stars do you want? '))
# numStars = int(raw_input ('How many stars per line? '))
# for line in range(0, numLines):
# 	for star in range(0, numStars):
# 		print '*',
# 	print

# numBlocks = int(raw_input ('How many blocks of stars do you want? '))
# numLines = int(raw_input ('How many lines of stars do you want? '))
# numStars = int(raw_input ('How many stars per line? '))
# for block in range(0, numBlocks):
# 	for line in range(0, numLines):
# 		for star in range(0, numStars):
# 			print '*',
# 		print
# 	print

# numBlocks = int(raw_input ('How many blocks of stars do you want? '))
# for block in range(1, numBlocks + 1):
# 	for line in range(0, block * 2):
# 		for star in range(0, (block + line) * 2):
# 			print '*',
# 		print
# 	print

# 打印循环变量，助于理解循环
# numBlocks = int(raw_input ('How many blocks of stars do you want? ')) # 3
# for block in range(1, 4):
# 	# print 'block = ', block
# 	for line in range(0, block * 2):
# 		for star in range(0, (block + line) * 2):
# 			print '*',
# 		# print '    line = ', line, 'star = ', star
# 		print
# 	print

# 更直观理解
# for i in range(1, 4):
# 	for j in range(0, i * 2):
# 		for k in range(0, (i + j) * 2):
# 			print 'i'+str(i)+'j'+str(j)+'k'+str(k)+'*',
# 		print
# 	print



# 热狗组合
# print "\t热狗 \t小面包 \t番茄酱 \t芥末酱 \t洋葱"
# count = 1
# for dog in [0, 1]:
# 	for bun in [0, 1]:
# 		for ketchup in [0, 1]:
# 			for mustard in [0, 1]:
# 				for onion in [0, 1]:
# 					print "#", count, "\t",
# 					print dog, "\t", bun, "\t", ketchup, "\t", mustard, "\t", onion
# 					count = count + 1

# 计算卡路里
# dog_cal = 140
# bun_cal = 120
# mus_cal = 20
# ket_cal = 80
# onion_cal = 40

# print "\t热狗 \t小面包 \t番茄酱 \t芥末酱 \t洋葱 \t卡路里"
# count = 1
# for dog in [0, 1]:
# 	for bun in [0, 1]:
# 		for ketchup in [0, 1]:
# 			for mustard in [0, 1]:
# 				for onion in [0, 1]:
# 					tot_cal = ((dog * dog_cal) +
# 						(bun * bun_cal) +
# 						(mustard * mus_cal) +
# 						(ketchup * ket_cal) +
# 						(onion * onion_cal))
# 					print "#", count, "\t",
# 					print dog, "\t", \
# 						bun, "\t", \
# 						ketchup, "\t", \
# 						mustard, "\t", \
# 						onion, "\t", \
# 						tot_cal
# 					count = count + 1

# excise
# for i in range(5):
# 	for j in range(3):
# 		print '*',

# 九九乘法表
# for i in range(10): # 0,1,2,3,4,5,6,7,8,9
# 	for j in range(1, i+1): # 1,1;1,2;1,3;1,4;...
# 		print str(i)+'x'+str(j)+'='+str(i * j)+"\t",
# 	print

# 打印数字和一行和数字同量的星号
import time
for i in range(4, 0, -1):
	print i,
	for j in range(i, 0, -1):
		print '*',
		time.sleep(0.1)
	print
