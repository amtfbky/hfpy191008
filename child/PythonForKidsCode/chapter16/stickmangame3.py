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
        self.bg = PhotoImage(file="background.gif")
        w = self.bg.width()
        h = self.bg.height()
        for x in range(0, 5):
            for y in range(0, 5):
                self.canvas.create_image(x * w, y * h, image=self.bg, anchor='nw')
        self.sprites = []
        self.running = True

    def mainloop(self):
        while 1:
            if self.running == True:
                for sprite in self.sprites:
                    sprite.move()
                self.tk.update_idletasks()
                self.tk.update()
                time.sleep(0.01)

class Coords:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

def within_x(co1, co2):
    if (co1.x1 > co2.x1 and co1.x1 < co2.x2) \
            or (co1.x2 > co2.x1 and co1.x2 < co2.x2) \
            or (co2.x1 > co1.x1 and co2.x1 < co1.x2) \
            or (co2.x2 > co1.x1 and co2.x2 < co1.x1):
        return True
    else:
        return False

def within_y(co1, co2):
    if (co1.y1 > co2.y1 and co1.y1 < co2.y2) \
            or (co1.y2 > co2.y1 and co1.y2 < co2.y2) \
            or (co2.y1 > co1.y1 and co2.y1 < co1.y2) \
            or (co2.y2 > co1.y1 and co2.y2 < co1.y1):
        return True
    else:
        return False

def collided_left(co1, co2):
    if within_y(co1, co2):
        if co1.x1 <= co2.x2 and co1.x1 >= co2.x1:
            return True
    return False

def collided_right(co1, co2):
    if within_y(co1, co2):
        if co1.x2 >= co2.x1 and co1.x2 <= co2.x2:
            return True
    return False

def collided_top(co1, co2):
    if within_x(co1, co2):
        if co1.y1 <= co2.y2 and co1.y1 >= co2.y1:
             return True
    return False

def collided_bottom(y, co1, co2):
    if within_x(co1, co2):
        y_calc = co1.y2 + y
        if y_calc >= co2.y1 and y_calc <= co2.y2:
            return True
    return False

class Sprite:
    '''
    精灵父类有两个函数：
        move用来移动精灵
        coords返回精灵当前在屏幕上的位置
    '''
    #参数game让每个精灵都能访问游戏中其它精灵的列表
    def __init__(self, game):
        #把game参数保存在一个对象变量中
        self.game = game
        #表示游戏是否结束
        self.endgame = False
        self.coordinates = None
    def move(self):
        #虽然move函数什么也不做，但确保子类都有这个功能
        #尽管有时子类中的函数什么也不做
        pass
    def coords(self):
        return self.coordinates

class PlatformSprite(Sprite):
    '''
    平台类：
        有一个game参数和父类一样
        一个图形
        xy坐标
        图形的宽高
    '''
    def __init__(self, game, photo_image, x, y, width, height):
        #调用父类的__init__函数
        #创建一个PlatformSprite对象就会有父类中所有对象变量
        Sprite.__init__(self, game)
        #把photo_image参数保存到对象变量中
        self.photo_image = photo_image
        #用game对象中的canvas变量上的create_image来画出图形
        self.image = game.canvas.create_image(x, y, image=self.photo_image, anchor='nw')
        #创建一个Coords对象
        self.coordinates = Coords(x, y, x + width, y + height)

g = Game()
#代表游戏的变量g，使用platform1.gif，位置，宽高
platform1 = PlatformSprite(g, PhotoImage(file="platform1.gif"), 0, 480, 100, 10)
#把创建的对象加入到game对象中的精灵列表
g.sprites.append(platform1)
g.mainloop()
