from tkinter import *
import random
import time

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
# tk.mainloop()

class Ball:
    '''
    1-Ball类，两个参数：画布和颜色
    2-把画布保存到一个OB变量中，在上面画球
    3-在画布上画一个用颜色参数填色的小球
    4-保存tkinter画小球返回的id，用来移动小球
    '''
    def __init__(self, canvas, color):
        self.canvas = canvas
        #椭圆左上角和右下角坐标
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        #把图形移到画布中心
        self.canvas.move(self.id, 245, 100)
        
    def draw(self):
        pass
        
ball = Ball(canvas, 'red')

while 1:
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

