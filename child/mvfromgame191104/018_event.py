# -*- coding:UTF-8 -*-

import pygame, sys
pygame.init()
screen = pygame.display.set_mode([640, 480])
background = pygame.Surface(screen.get_size())
background.fill([255, 255, 255])
clock = pygame.time.Clock()
class Ball(pygame.sprite.Sprite):
	def __init__(self, image_file, location, speed):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(image_file)
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = location
		self.speed = speed
	
	def move(self):
		if self.rect.left <= screen.get_rect().left or \
				self.rect.right >= screen.get_rect().right:
			self.speed[0] = -self.speed[0]
			# 底下二行如没在if里，球则往右下方落下消失不见
			newpos = self.rect.move(self.speed)
			self.rect = newpos

my_ball = Ball('beach_ball.png', [10, 0], [20, 20])
# 未加定时器之前
# delay = 100
# interval = 50
# pygame.key.set_repeat(delay, interval)

# 定时器
pygame.time.set_timer(pygame.USEREVENT, 1000)
direction = 1

# held_down = False # dragging
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		# 按键事件
		# elif event.type == pygame.KEYDOWN:
		# 	if event.key == pygame.K_UP:
		# 		my_ball.rect.top = my_ball.rect.top - 10
		# 	elif event.key == pygame.K_DOWN:
		# 		my_ball.rect.top = my_ball.rect.top + 10
		
		# 鼠标事件，不按而拖动
		# elif event.type == pygame.MOUSEMOTION:
		# 	my_ball.rect.center = event.pos

		# dragging
		# elif event.type == pygame.MOUSEBUTTONDOWN:
		# 	held_down = True
		# elif event.type == pygame.MOUSEBUTTONUP:
		# 	held_down = False
		# elif event.type == pygame.MOUSEMOTION:
		# 	if held_down:
		# 		my_ball.rect.center = event.pos

		# 定时器的事件处理器
		elif event.type == pygame.USEREVENT:
			my_ball.rect.centery = my_ball.rect.centery + (30 * direction)
			if my_ball.rect.top <= 0 or \
			my_ball.rect.bottom >= screen.get_rect().bottom:
				direction = -direction
	clock.tick(30)
	screen.blit(background, (0, 0))
	my_ball.move()
	screen.blit(my_ball.image, my_ball.rect)
	pygame.display.flip()