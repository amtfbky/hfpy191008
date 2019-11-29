'''
创建窗口
'''
from tkinter import *
import random
import time

tk = Tk()
#窗口标题
tk.title("Game")
#窗口大小不可调整
tk.resizable(0, 0)
#把包含画布的窗口放到所有其它窗口之前-topmost
tk.wm_attributes("-topmost", 1)
#后面两个参数确保画布之外没有边框，美观一些
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
#让画布按前一行给出的宽高度参数来调整其自身大小
canvas.pack()
#为动画做好初始化
while 1:
    tk.update()
