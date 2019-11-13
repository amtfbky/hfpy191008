# -*- coding:UTF-8 -*-
# 从此要开始习惯长代码了
# 动画精灵子类
# import pygame, sys
# from random import *
# #--------ball subclass definition-------------------------
# class MyBallClass(pygame.sprite.Sprite):
# 	def __init__(self, image_file, location, speed):
# 		pygame.sprite.Sprite.__init__(self)
# 		self.image = pygame.image.load(image_file)
# 		self.rect = self.image.get_rect()
# 		self.rect.left, self.rect.top = location
# 		self.speed = speed
	
# 	def move(self):
# 		self.rect = self.rect.move(self.speed)
# 		if self.rect.left < 0 or self.rect.right > width:
# 			self.speed[0] = -self.speed[0]
		
# 		if self.rect.top < 0 or self.rect.bottom > height:
# 			self.speed[1] = -self.speed[1]

# #--------main program--------------------------------------
# size = width, height = 640, 480
# screen = pygame.display.set_mode(size)
# screen.fill([255, 255, 255])
# img_file = "beach_ball.png"
# balls = []
# for row in range(0, 3):
# 	for column in range(0, 3):
# 		location = [column * 180 + 10, row * 180 + 10]
# 		speed = [choice([-2, 2]), choice([-2, 2])]
# 		ball = MyBallClass(img_file, location, speed)
# 		balls.append(ball)

# while True:
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:sys.exit()
# 	pygame.time.delay(20)
# 	screen.fill([255, 255, 255])
# 	for ball in balls:
# 		ball.move()
# 		screen.blit(ball.image, ball.rect)
# 	pygame.display.flip()


# 碰撞检测
import pygame, sys
from random import *
#--------ball subclass definition-------------------------
class MyBallClass(pygame.sprite.Sprite):
	def __init__(self, image_file, location, speed):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(image_file)
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = location
		self.speed = speed
	
	def move(self):
		self.rect = self.rect.move(self.speed)
		if self.rect.left < 0 or self.rect.right > width:
			self.speed[0] = -self.speed[0]
		
		if self.rect.top < 0 or self.rect.bottom > height:
			self.speed[1] = -self.speed[1]

def animate(group):
	screen.fill([255, 255, 255])
	for ball in group:
		ball.move()
	for ball in group:
		group.remove(ball)
		if pygame.sprite.spritecollide(ball, group, False):
			ball.speed[0] = -ball.speed[0]
			ball.speed[1] = -ball.speed[1]
		group.add(ball)
		screen.blit(ball.image, ball.rect)
	pygame.display.flip()
	# pygame.time.delay(50)
#--------main program--------------------------------------
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
screen.fill([255, 255, 255])
img_file = "beach_ball.png"
clock = pygame.time.Clock()
group = pygame.sprite.Group()
for row in range(0, 2):
	for column in range(0, 2):
		location = [column * 180 + 10, row * 180 + 10]
		speed = [choice([-5, 5]), choice([-5, 5])]
		ball = MyBallClass(img_file, location, speed)
		group.add(ball)

# while True:
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			frame_rate = clock.get_fps()
			print "frame rate = ", frame_rate
			sys.exit()
	animate(group)
	clock.tick(30)
# frame rate =  30.2114810944

