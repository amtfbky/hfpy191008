'''
把正方形的边长作为一个参数
'''
import turtle
t = turtle.Pen()

def mysquare(size):
    for x in range(0,4):
        t.forward(size)
        t.left(90)
        
# mysquare(25) 
# mysquare(50) 
# mysquare(75) 
# mysquare(100) 
t.begin_fill()
mysquare(125)
t.end_fill()
