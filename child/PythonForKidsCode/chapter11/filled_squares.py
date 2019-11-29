'''
把四边形边长和filled值设成参数
1.用if检查filled值，真则填色
2.用循环画四边形
3.再用if检查filled值，真则关闭填色
'''
import turtle
t = turtle.Pen()

def mysquare(size, filled):
    if filled == True:
        t.begin_fill()
    for x in range(0,4):
        t.forward(size)
        t.left(90)
    if filled == True:
        t.end_fill()
        
mysquare(50, True)
mysquare(150, False)
