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
    '''
    用来指定物体在游戏屏幕上位置的类
    它会保存游戏中某一物体的左上角和右下角坐标
    '''
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

'''
######## 冲突检测 ########
1-保存了精灵的位置后，需要判断一个精灵是否与另一个精灵的位置冲突
如：火柴人在屏幕上跳来跳去是否撞到了平台上
可以拆成两个小一点的问题：
    检测两个精灵是否在垂直方向或水平位置上冲突
'''
#判断一组x坐标是否与另一组x坐标交叉
def within_x(co1, co2):
    #精灵甲的最左边x1是否在精灵乙的左右边x1x2之间
            #甲最右边x2是否在乙的左右边x1x2之间
            #甲乙对调，即乙的最左边是否在甲的左右边之间
            #乙的最右边是否在甲的左右边之间
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

#左侧相撞
def collided_left(co1, co2):
    #用within_y函数判断两个坐标在纵向是否有重叠
    if within_y(co1, co2):
        #判断甲最左侧是否撞到了乙的右侧
        if co1.x1 <= co2.x2 and co1.x1 >= co2.x1:
            return True
    return False

def collided_right(co1, co2):
    if within_y(co1, co2):
        if co1.x2 >= co2.x1 and co1.x2 <= co2.x2:
            return True
    return False

def collided_top(co1, co2):
    #水平方向是否有重叠
    if within_x(co1, co2):
        #判断甲的顶部是否撞到乙的底部
        if co1.y1 <= co2.y2 and co1.y1 >= co2.y1:
             return True
    return False

def collided_bottom(y, co1, co2):
    #水平方向是否有重叠
    if within_x(co1, co2):
        #把参数y加上第一个坐标即精灵甲的y2位置
        y_calc = co1.y2 + y
        '''
        新值若在乙的y1y2之间，即甲底部撞上乙顶部
        这个情况是：
            火柴人可能会从平台上掉下来，我们要能够判断他是否会掉到底，而不是他是否已经掉到底了
            如果他从一个平台上走下来一直停在半空中的话，游戏就不真实了
            当检查他的下面时，要判断他是否会撞上平台；如果不会，他就摔死了！
        '''
        if y_calc >= co2.y1 and y_calc <= co2.y2:
            return True
    return False

g = Game()
g.mainloop()
