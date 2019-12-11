# -*- coding:utf-8 -*-

import easygui
#flavor = easygui.buttonbox("what is your favorite ice cream flavor?",
# flavor = easygui.choicebox("what is your favorite ice cream flavor?",
# 	choices = ['Vanilla', 'Chocolate', 'Strawberry'])
# flavor = easygui.enterbox("what is your favorite ice cream flavor?",
# 	default = 'Vanilla')

# easygui.msgbox ("You picked " + flavor)

name = easygui.enterbox("姓名")
house = easygui.enterbox("房号")
street = easygui.enterbox("街道")
city = easygui.enterbox("城市")
sheng = easygui.enterbox("省份")
post = easygui.enterbox("邮编")

easygui.msgbox(name + '\n'
	+ house + ' ' + street + '\n'
	+ city + ', '+ sheng + '\n'
	+ post)
