'''
1.color画笔颜色
    三个参数：RGB
    亮红色1 0 0
2.begin/end_fill区域填色
3.circle指定大小的圆
4.setheading海龟面向

'''
import turtle
t = turtle.Pen()

# t.color(1,0,0) 
# t.begin_fill() 
# t.forward(100) 
# t.left(90) 
# t.forward(20) 
# t.left(90) 
# t.forward(20) 
# t.right(90) 
# t.forward(20) 
# t.left(90) 
# t.forward(60) 
# t.left(90) 
# t.forward(20) 
# t.right(90) 
# t.forward(20) 
# t.left(90) 
# t.forward(20) 
# t.end_fill()
# t.color(0,0,0)
# t.up() 
# t.forward(10) 
# t.down()
# t.begin_fill() 
# t.circle(10) 
# t.end_fill()
# t.setheading(0) 
# t.up() 
# t.forward(90) 
# t.right(90)
# t.forward(10) 
# t.setheading(0)
# t.begin_fill() 
# t.down() 
# t.circle(10) 
# t.end_fill()

def mycircle(red, green, blue):
    t.color(red, green, blue)
    t.begin_fill()
    t.circle(50)
    t.end_fill()

# mycircle(0, 1, 0) #亮绿色
# mycircle(0, 0.5, 0) #深绿色
mycircle(0.9, 0.75, 0) #金色
# mycircle(1, 0.7, 0.75) #淡粉色
# mycircle(1, 0.5, 0) #橙色
# mycircle(0.9, 0.7, 0.15) #橙色









