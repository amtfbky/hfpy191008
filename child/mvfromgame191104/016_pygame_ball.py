# -*- coding:UTF-8 -*-


# 100个长宽粗细不等颜色不一的矩形错落叠加，构成一幅艺术图
# import pygame, sys, random
# from pygame.color import THECOLORS
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# screen.fill([255, 255, 255])
# for i in range(100):
#     width = random.randint(0, 250)
#     height = random.randint(0, 100)
#     top = random.randint(0, 400)
#     left = random.randint(0, 500)
#     color_name = random.choice(THECOLORS.keys())
#     color = THECOLORS[color_name]
#     line_width = random.randint(1, 3)
#     pygame.draw.rect(screen, color, [left, top, width, height], line_width)
# pygame.display.flip()
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()

# 球向右动了100个像素单位，原来的地方被白色矩形盖住了
# import pygame, sys
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# screen.fill([255, 255, 255])
# my_ball = pygame.image.load('beach_ball.png')
# screen.blit(my_ball, [50, 50])
# pygame.display.flip()
# pygame.time.delay(2000)
# screen.blit(my_ball, [150, 50])
# pygame.draw.rect(screen, [255, 255, 255], [50, 50, 90, 90], 0)
# pygame.display.flip()
# while True:
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			sys.exit()

# 球可以动起来了
# import pygame, sys
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# screen.fill([255, 255, 255])
# my_ball = pygame.image.load('beach_ball.png')
# x = 50
# y = 50
# screen.blit(my_ball, [x, y])
# pygame.display.flip()
# for looper in range(1, 100):
# 	pygame.time.delay(20)
# 	pygame.draw.rect(screen, [255, 255, 255], [x, y, 90, 90], 0)
# 	x = x + 5
# 	screen.blit(my_ball, [x, y])
# 	pygame.display.flip()
# while True:
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			sys.exit()


# 球碰到边框反弹
# 分析：左边界，x=0；右边界，x=640-90=550
# 让球一直反弹，并加速
# import pygame, sys
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# screen.fill([255, 255, 255])
# my_ball = pygame.image.load('beach_ball.png')
# x = 50
# y = 50
# x_speed = 10
# while True:
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			sys.exit()
# 	pygame.time.delay(20)
# 	pygame.draw.rect(screen, [255, 255, 255], [x, y, 90, 90], 0)
# 	x = x + x_speed
# 	if x > screen.get_width() - 90 or x < 0:
# 		x_speed = - x_speed
# 	screen.blit(my_ball, [x, y])
# 	pygame.display.flip()

# 球会上下左右反弹
# import pygame, sys
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# screen.fill([255, 255, 255])
# my_ball = pygame.image.load('beach_ball.png')
# x = 50
# y = 50
# x_speed = 10
# y_speed = 10
# while True:
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			sys.exit()
# 	pygame.time.delay(20)
# 	pygame.draw.rect(screen, [255, 255, 255], [x, y, 90, 90], 0)
# 	x = x + x_speed
# 	y = y + y_speed
# 	if x > screen.get_width() - 90 or x < 0:
# 		x_speed = - x_speed
# 	if y > screen.get_height() - 90 or y < 0:
# 		y_speed = - y_speed
# 	screen.blit(my_ball, [x, y])
# 	pygame.display.flip()

# 让球成走马灯：向右跑出右边界后从左边界出来
# import pygame, sys
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# screen.fill([255, 255, 255])
# my_ball = pygame.image.load('beach_ball.png')
# x = 50
# y = 50
# x_speed = 5
# while True:
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			sys.exit()
# 	pygame.time.delay(20)
# 	pygame.draw.rect(screen, [255, 255, 255], [x, y, 90, 90], 0)
# 	x = x + x_speed
# 	if x > screen.get_width():
# 		x = -90
# 	screen.blit(my_ball, [x, y])
# 	pygame.display.flip()
