from tkinter import *
import random
import time

class Game:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Mr. Stick Man Races for the Exit")
        self.tk.resizable(0, 0)
        self.tk.wm_attributes("-topmost", 1)
        self.canvas = Canvas(self.tk, width=500, height=500, highlightthickness=0)
        self.canvas.pack()
        self.tk.update()
        self.canvas_height = 500
        self.canvas_width = 500
        #装载背景图形
        self.bg = PhotoImage(file="background.gif")
        #图形宽高
        w = self.bg.width()
        h = self.bg.height()
        #5行5列背景图片铺满画布
        for x in range(0, 5):
            for y in range(0, 5):
                self.canvas.create_image(x * w, y * h, image=self.bg, anchor='nw')
        self.sprites = []
        self.running = True

    def mainloop(self):
        while 1:
            if self.running == True:
                #遍历所有精灵列表中的精灵
                for sprite in self.sprites:
                    #移动精灵，但现在还没创建任何精灵
                    sprite.move()
                self.tk.update_idletasks()
                self.tk.update()
                time.sleep(0.01)

g = Game()
g.mainloop()
