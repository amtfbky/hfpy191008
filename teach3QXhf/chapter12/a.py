# -*- coding: UTF-8 -*-
'''
用from 模块名 import *，就不用模块名使用模块的内容了
Tk类创建一个基本的窗口，可在上面增加东西如按钮、输入框或画布
这是tkinter模块最主要的类
Button创建了一个按钮，把tk作为第一个参数
还要pack让按钮显示
+++++++++++++++++++++++++++++++++++++++++++++
画图：canvas画布
#ffd800，金色，16进制表示法
print('%x' % 15)，把15转成十六进制f
print('%02x' % 15)，把15转成十六进制，有两位0f

'''
# from tkinter import *
from tkinter import *           # 导入 Tkinter 库
# import tkinter.colorchooser
# import random
import time
# c = tkinter.colorchooser.askcolor()
tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
# canvas.create_line(0, 0, 500, 500)                                # 创建两个列表
# canvas.create_rectangle(10, 10, 50, 50)
# def random_rectangle(width, height, fill_color):
#     x1 = random.randrange(width)
#     y1 = random.randrange(height)
#     x2 = x1 + random.randrange(width)
#     y2 = y1 + random.randrange(height)
#     canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color)

# create_arc--------------4
# no 360,beacause arc let 360=0
# canvas.create_arc(10, 10, 200, 100, extent=180, style=ARC)
# canvas.create_arc(10, 10, 200, 80, extent=45, style=ARC)
# canvas.create_arc(10, 80, 200, 160, extent=90, style=ARC)
# canvas.create_arc(10, 160, 200, 240, extent=135, style=ARC)
# canvas.create_arc(10, 240, 200, 320, extent=180, style=ARC)
# canvas.create_arc(10, 320, 200, 400, extent=359, style=ARC)

# create_polygon-----------5
# canvas.create_polygon(10, 10, 100, 10, 100, 110, fill="", 
#         outline="black")
# close the begin point and end point
# canvas.create_polygon(200, 10, 240, 30, 120, 100, 140, 120, fill="", 
#         outline="black")

# create_text-----------6
# canvas.create_text(150, 100, text='There once was a man from Toulouse,')
# canvas.create_text(130, 120, text='Who rode around on a moose.', fill='green')
# canvas.create_text(150, 150, text='He said, "It\'s my curse,"', font=('Times', 15))
# canvas.create_text(200, 200, text='But it could be worse,', font=('Helvetica', 20))
# canvas.create_text(220, 250, text='My cousin rides round', font=('Courier', 22))
# canvas.create_text(220, 300, text='on a goose.', font=('Courier', 30) )

# image-------------7
# my_image = PhotoImage(file='gif')
# NW=northwest西北方向-画图的起始点（缺省是中心）
# canvas.create_image(0, 0, anchor=NW, image=myimage)

# 创建基本的动画（但这不是tkinter的专长）--8
mytriangle = canvas.create_polygon(10, 10, 10, 60, 50, 35)
# 用itemconfig来改变图形填充和轮廓颜色
canvas.itemconfig(mytriangle, fill='blue', outline='green')
def movetriangle(event):
    # key symbol键的符号
    if event.keysym == 'Up':
        # 把id改成要操作的对象名mytriangle则不会搞错id
        canvas.move(1, 0, -3)
    elif event.keysym == 'Down':
        canvas.move(1, 0, 3)
    elif event.keysym == 'Left':
        canvas.move(1, -3, 0)
    else:
        canvas.move(1, 3, 0)
# 监听事件调用movetriangle函数
# canvas.bind_all('<KeyPress-Return>', movetriangle)
canvas.bind_all('<KeyPress-Up>', movetriangle)
canvas.bind_all('<KeyPress-Down>', movetriangle)
canvas.bind_all('<KeyPress-Left>', movetriangle)
canvas.bind_all('<KeyPress-Right>', movetriangle)
# for x in range(0, 60):
#     # id=1,x=5,y=0;x=-5 come back
#     # x=5/-5,y=5/-5,画布高宽度均为400
#     canvas.move(1, 5, 0)
#     # 重绘，否则只会显示循环后的位置，不会显示平滑移动
#     tk.update()
#     # 每次重绘间隔十二分之一秒
#     time.sleep(0.05)

# random_rectangle---------1
# for x in range(0, 10):
#     random_rectangle(500, 500)

# colorchooser---------3
# random_rectangle(500, 500, c[1])

# fill_color----------2
# random_rectangle(500, 500, 'red')
# random_rectangle(500, 500, 'blue')
# random_rectangle(500, 500, 'orange')
# random_rectangle(500, 500, 'yellow')
# random_rectangle(500, 500, 'pink')
# random_rectangle(500, 500, 'purple')
# random_rectangle(500, 500, 'violet')
# random_rectangle(500, 500, 'magenta')
# random_rectangle(500, 500, 'cyan')

tk.mainloop()                 # 进入消息循环
