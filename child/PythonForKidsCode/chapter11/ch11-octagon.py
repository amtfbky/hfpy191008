'''
八边形
360/8=45
'''
import turtle
t = turtle.Pen()
def octagon(size, points):
    for x in range(0, points):
        t.forward(size)
        t.right(360 / points)

octagon(100, 10)
