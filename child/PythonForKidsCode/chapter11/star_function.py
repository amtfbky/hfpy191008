'''
给星星填上颜色：
和给四边形填色一样把星星边长和filled作为参数
第二个星星不填色，给第一星星画上轮廓
'''
import turtle
t = turtle.Pen()

def mystar(size, filled):
    if filled:
        t.begin_fill()
    for x in range(1,19):
        t.forward(size)
        if x % 2 == 0:
            t.left(175)
        else:
            t.left(225)
    if filled:
        t.end_fill()

t.color(0.9, 0.75, 0)
mystar(120, True)
t.color(0,0,0)
mystar(120, False)
