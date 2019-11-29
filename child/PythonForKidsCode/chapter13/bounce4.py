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

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        #初始化小球移动的幅度
        self.x = 0
        self.y = -1
        #获取画布当前的高度
        self.canvas_height = self.canvas.winfo_height()
        
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        #通过ID返回画布上任何画好的东西的坐标
        pos = self.canvas.coords(self.id)
        #y1坐标，小球顶部触顶
        if pos[1] <= 0:
            #触顶反弹？
            self.y = 1
        #y2坐标，小球底部触底
        if pos[3] >= self.canvas_height:
            #触底反弹？
            self.y = -1
        
ball = Ball(canvas, 'red')

while 1:
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

