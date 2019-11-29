import turtle
t = turtle.Pen()
'''
步骤：
1.创建一个18，次的循环
2.向前移动100个像素
3.if偶数左转175度；
否则左转225度
'''

for x in range(1, 19):
    t.forward(100)
    if x % 2 == 0:
        t.left(175)
    else:
        t.left(225)


