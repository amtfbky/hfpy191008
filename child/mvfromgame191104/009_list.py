# -*- coding:utf-8 -*-

# friends = [] # 列表可包含任何类型的数据：数字、字符串、对象，甚至其它列表
# friends.append("孙悟空") # 变量名.操作函数名(参数)
# # print friends # \xe5\xad\x99\xe6\x82\x9f\xe7\xa9\xba
# print str(friends).decode('string-escape')
# friends.append("猪八戒")
# print str(friends).decode('string-escape')
# # python3:print str(varname).decode(‘string-escape’)‘

# # 索引
# print friends[0]

# 分片
l = [1,2,3,4,5]
# print l[2]
# print type(l[2])
# print l[2:3]
# print type(l[2:3])
# print l[1:3] # 这个新的列表是原列表的部分副本

# 分片简写
# print l[:2]
# print l[2:]
# print l[:]

# 修改列表元素，没有建立新的列表
# l[2] = 10
# print l

# 增加元素
# l.append('this is append')
# print l

# l.extend(['extend1', 'extend2', 'extend3'])
# print l

# 插入元素，类似append
# l.insert(2, 'this is insert')
# print l

# append和extend的区别
# l.extend(['a', 'b', 'c'])
# print l # [1, 2, 3, 4, 5, 'a', 'b', 'c']
# l.append(['a', 'b', 'c'])
# print l # [1, 2, 3, 4, 5, ['a', 'b', 'c']]

# 删除元素，不需要知道元素在哪个位置
# l.remove(3)
# print l

# del允许用索引删除元素
# del l[2]
# print l

# pop()取出最后一个元素
# last = l.pop()
# print l
# print last

# pop()可以提供一个索引
# a = l.pop(1)
# print a
# print l

# 搜索列表，in关键字
# if 'a' in ['a', 'b']:
# 	print 'found it.'
# else:
# 	print 'no found.'

# 查找索引
# print ['a', 'b', 'c'].index('a')

# 循环处理列表
# for i in l:
# 	print i,

# 排序
# n = ['李四', '张三', '王五']
# n.sort() # 改变原始列表，没有创建一个新的列表
# # print n # ['\xe5\xbc\...', '\xe6\x9d\...', '\xe7\x8e\...']
# print str(n).decode('string-escape') # ['张三', '李四', '王五']
# 逆排序
# n = ['李四', '张三', '王五']
# # n.reverse() # 第一种方法
# n.sort(reverse = True) # 第二种方法
# print str(n).decode('string-escape') # ['王五', '张三', '李四']

# 建立列表副本，然后对副本排序，这样就可以保留原列表
# original_list = ['香港', '台湾', '大陆']
# new_list = original_list[:]
# # 新和旧各自指向一个列表，如果不切片，则指向同一个列表

# print str(original_list).decode('string-escape')
# new_list.sort()
# print str(new_list).decode('string-escape')

# 另一种排序方法——sorted()，可保留原列表
# original = [3,5,29,2,13,4]
# newer = sorted(original)
# print original
# print newer

# ***** 不可改变的列表：元组——不能排序、增删 P146 *****
# 双重列表：数据表
# zhangsan = [34, 23, 21, 53]
# lisi = [23, 24, 32, 21]
# wangwu = [54, 43, 22, 26]

# math = [34, 23, 54]
# science = [23, 24, 43]
# reading = [21, 32, 22]
# spelling = [53, 21, 26]

# classMarks = [zhangsan, lisi, wangwu]
# print classMarks

# for studentMarks in classMarks:
# 	print studentMarks

# print classMarks[0]
# print classMarks[0][2]

# excise
# l = []
# i = 1
# while i <= 5:
# 	name = raw_input("Enter 5 names:")
# 	l.append(name) # 循环添加名字
# 	i += 1
# 这里为了省去输入名字的麻烦，直接把名字建立了列表
l = ['zhangsan', 'lisi', 'wangwu', 'zhaoliu', 'qianqi']
# for n in l:
# 	print n,
# print
# l2 = sorted(l) # 保留原列表，新列表才能遍历，如果l2=l.sort()，l2则不能遍历
# for n in l2:
# 	print n,

# 只显示第三个名字
# print l[2]

n = int(raw_input("Replace one name. Which one?(1~5): "))
l[n-1] = raw_input("New name: ")
print "The names are ",
for name in l:
	print name,
