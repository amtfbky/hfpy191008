# -*- coding:utf-8 -*-

print float(23)
print int(23.0)

a = 5.99
b = int(a)
print a
print b

a = '3.9'
b = float(a)
print a
print b

a = '3.7'
b = 3.7
print type(a)
print type(b)

# cel = 5.0 / 9 * (fahr - 32)
# cel float(5) / 9 * (fahr - 32)
# cel 5 / float(9) * (fahr - 32)

# excise
# int()将小数转换为整数，结果是下取整
# cel = float(5 / 9 * (fahr - 32))，cel = 5 / 9 * float(fahr - 32)，可以吗？为什么？
# 挑战题：除了int()不使用任何其他函数，对一个数四舍五入（即不会只是下取整）

print float('12.34')
print int(56.78)

# 用int()从一个字符串创建整数
print int(float('8.9'))

