# -*- coding:UTF-8 -*-
import pygame, sys

#--------ball subclass definition-------------------------
class MyBallClass(pygame.sprite.Sprite):
	def __init__(self, image_file, speed, location):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(image_file)
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = location
		self.speed = speed
	
	def move(self):
		global points, score_text
		self.rect = self.rect.move(self.speed)
		if self.rect.left < 0 or self.rect.right > screen.get_width():
			self.speed[0] = -self.speed[0]
			hit_wall.play() # 1
		
		if self.rect.top < 0:
			self.speed[1] = -self.speed[1]
			points = points + 1
			score_text = font.render(str(points), 1, (0, 0, 0))
			get_point.play() # 2


#-------paddle--------------------------------------------
class MyPaddleClass(pygame.sprite.Sprite):
	def __init__(self, location):
		pygame.sprite.Sprite.__init__(self)
		image_surface = pygame.surface.Surface([100, 20])
		image_surface.fill([0, 0, 0])
		self.image = image_surface.convert()
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = location


pygame.init()
pygame.mixer.init()
hit = pygame.mixer.Sound("hit_paddle.wav")
hit.set_volume(0.8)
hit_wall = pygame.mixer.Sound("hit_wall.wav")
hit_wall.set_volume(0.8)
get_point = pygame.mixer.Sound("get_point.wav")
get_point.set_volume(0.8)
splat = pygame.mixer.Sound("splat.wav")
splat.set_volume(0.8)
new_life = pygame.mixer.Sound("new_life.wav")
new_life.set_volume(0.8)
bye = pygame.mixer.Sound("game_over.wav")
bye.set_volume(0.8)

screen = pygame.display.set_mode([640, 480])
clock = pygame.time.Clock()
ball_speed = [10, 5]
myBall = MyBallClass('wackyball.bmp', ball_speed, [50, 50])
ballGroup = pygame.sprite.Group(myBall)
paddle = MyPaddleClass([270, 400])
lives = 3
points = 0

# create font object
font = pygame.font.Font(None, 50)
score_text = font.render(str(points), 1, (0, 0, 0))
textpos = [10, 10]
done = False
while 1:
	clock.tick(30)
	screen.fill([255, 255, 255])
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		# ctrl paddle
		elif event.type == pygame.MOUSEMOTION:
			paddle.rect.centerx = event.pos[0]

	if pygame.sprite.spritecollide(paddle, ballGroup, False):
		myBall.speed[1] = -myBall.speed[1]
		hit.play()
	myBall.move()

	# all re-draw
	if not done:
		screen.blit(myBall.image, myBall.rect)
		screen.blit(paddle.image, paddle.rect)
		screen.blit(score_text, textpos)
		for i in range (lives):
			width = screen.get_width()
			screen.blit(myBall.image, [width - 40 * i, 20])
		pygame.display.flip()

	# 如果球碰到底边就减一条命
	if myBall.rect.top >= screen.get_rect().bottom:
		if not done:
			splat.play() # 3，确保声音只播放一次
		# elif not done:
		# 	hit_wall.play() # error1
		lives = lives -1
		if lives == 0:
			if not done:
				bye.play() # 5，确保声音只播放一次

		# 创建和绘制最终的分数文本
		if lives == 0:
			# bye.play() # 5
			final_text1 = "Game Over"
			final_text2 = "Your final score is: " + str(points)
			ft1_font = pygame.font.Font(None, 70)
			ft1_surf = font.render(final_text1, 1, (0, 0, 0))
			ft2_font = pygame.font.Font(None, 50)
			ft2_surf = font.render(final_text2, 1, (0, 0, 0))
			screen.blit(ft1_surf, [screen.get_width()/2 - \
						ft1_surf.get_width()/2, 100])
			screen.blit(ft2_surf, [screen.get_width()/2 - \
						ft2_surf.get_width()/2, 200])
			pygame.display.flip()
			done = True
		else:
			pygame.time.delay(1000)
			new_life.play() # 4
			myBall.rect.topleft = [50, 50]
			screen.blit(myBall.image, myBall.rect)
			pygame.display.flip()
			pygame.time.delay(1000)


