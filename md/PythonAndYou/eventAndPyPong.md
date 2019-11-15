

# 事件

很多程序需要对“发生的事情”做出反应：

- 移动或点击鼠标
- 按键
- 经过了一定时间

事件驱动程序event-driven program：“原地不动”（只是看起来不动，其实程序在不断扫描计算机内存中用来指示事件发生的部分），什么也不做，等待着有事件发生；一旦事件确实发生，它们就会做出反应，完成所有必要的工作来处理这个事件。如：Windows操作系统（或者其他GUI）

事件循环event loop：不断寻找事件的这个特殊循环叫做事件循环。

事件队列event queue：内存中存储事件的部分叫做事件队列。

事件处理器event handler：程序中处理某个事件的部分称为一个事件处理器。

- keyDown事件处理器：键盘上的方向键控制一艘船的移动
- mouseMove：用鼠标控制船

## 键盘事件

反弹球的例子，在增加事件之前先更新这个程序：

- 使用动画精灵
- 使用clock.tick()而不是time.delay()

注意：在新位置上重画球之前要从原位置“擦除”动画精灵有2种方法

- 一是在每个动画精灵的原位置上涂上背景颜色
- 二是直接重绘每一帧的整个背景——等于每一次都是从一个空屏幕开始

这里用了第二种方法：background

### 按键事件

pygame.event.get()：会得到所有事件的一个列表

for：循环迭代处理这个列表中的每一个事件

```python
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
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				my_ball.rect.top = my_ball.rect.top - 10
			elif event.key == pygame.K_DOWN:
				my_ball.rect.top = my_ball.rect.top + 10

	clock.tick(30)
	screen.blit(background, (0, 0))
	my_ball.move()
	screen.blit(my_ball.image, my_ball.rect)
	pygame.display.flip()
```

### 按键重复

在按键一直按下时生成多个KEYDOWN事件：两个时间

- 开始重复之前等待多长时间
- 多长时间重复一次

```python
...
delay = 100
interval = 50
pygame.key.set_repeat(delay, interval)
while ...
```

### 事件名和按键名

事件列表：.../pygame/docs/ref/event.html

按键名列表：.../pygame/docs/ref/key.html

常用事件：QUIT KEYDOWN KEYUP MOUSEMOTION MOUSEBUTTONUP MOUSEBUTTONDOWN

按键名：K_a K_b K_SPACE K_ESCAPE

## 鼠标事件

最常用：MOUSEMOTION MOUSEBUTTONUP MOUSEBUTTONDOWN

```python
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.MOUSEMOTION:
			my_ball.rect.center = event.pos
```

上面不需要按下鼠标就可以实现球跟着鼠标动，现在让球在鼠标按下时才起作用：

按下鼠标时移动鼠标——拖动dragging，但没有MOUSEDRAG事件类型：

```python
held_down = False
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN: # 检查鼠标按下
			held_down = True
		elif event.type == pygame.MOUSEBUTTONUP: # 检查鼠标松开
			held_down = False
		elif event.type == pygame.MOUSEMOTION: # 这里才是拖动
			if held_down:
				my_ball.rect.center = event.pos
```

### 定时器

定时器事件timer event：按固定的间隔生成事件，生成什么事件呢？用户事件user event。

```python
pygame.time.set_timer(pygame.USEREVENT, 1000)
direction = 1
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		# 定时器的事件处理器
		elif event.type == pygame.USEREVENT:
			my_ball.rect.centery = my_ball.rect.centery + (30 * direction)
			if my_ball.rect.top <= 0 or \
			my_ball.rect.bottom >= screen.get_rect().bottom:
				direction = -direction
```

## PyPong game

简单单机版本：

- 一个来回反弹的球
- 一个打球的球拍
- 一种控制球拍的方法
- 一种记录分数并在窗口上显示分数的方法
- 一种确定有几条“命”的方法——几次机会

现在实现前三个功能：

```python
import pygame, sys
from pygame.locals import *
#--------ball subclass definition-------------------------
class MyBallClass(pygame.sprite.Sprite):
	def __init__(self, image_file, speed, location):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(image_file)
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = location
		self.speed = speed
	
	def move(self):
		self.rect = self.rect.move(self.speed)
        # 在窗口两边反弹
		if self.rect.left < 0 or self.rect.right > screen.get_width():
			self.speed[0] = -self.speed[0]
		# 在窗口顶边反弹
		if self.rect.top < 0:
			self.speed[1] = -self.speed[1]


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
screen = pygame.display.set_mode([640, 480])
clock = pygame.time.Clock()
ball_speed = [10, 5]
myBall = MyBallClass('wackyball.bmp', ball_speed, [50, 50])
# 把球增加到一个组以便完成球和球拍之间的碰撞检测
ballGroup = pygame.sprite.Group(myBall)
paddle = MyPaddleClass([270, 400])

while 1:
	clock.tick(30)
	screen.fill([255, 255, 255])
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		# ctrl paddle中心跟随鼠标移动
		elif event.type == pygame.MOUSEMOTION:
			paddle.rect.centerx = event.pos[0]
	# ”打“球——球和球拍之间的碰撞检测
	if pygame.sprite.spritecollide(paddle, ballGroup, False):
		myBall.speed[1] = -myBall.speed[1]
	myBall.move()
    # 重绘
	screen.blit(myBall.image, myBall.rect)
	screen.blit(paddle.image, paddle.rect)
	pygame.display.flip()
```

现在实现全部功能：

```python
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
		global points, score_text # 全局变量
		self.rect = self.rect.move(self.speed)
		if self.rect.left < 0 or self.rect.right > screen.get_width():
			self.speed[0] = -self.speed[0]
		
		if self.rect.top < 0:
			self.speed[1] = -self.speed[1]
            # 球碰到顶边分数加1,并传给成绩文本
			points = points + 1
			score_text = font.render(str(points), 1, (0, 0, 0))


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
screen = pygame.display.set_mode([640, 480])
clock = pygame.time.Clock()
ball_speed = [10, 5]
myBall = MyBallClass('wackyball.bmp', ball_speed, [50, 50])
ballGroup = pygame.sprite.Group(myBall)
paddle = MyPaddleClass([270, 400])
lives = 3
points = 0

# create font object
font = pygame.font.Font(None, 50) # 创建字体对象
score_text = font.render(str(points), 1, (0, 0, 0)) # 渲染文本
textpos = [10, 10] # 设置文本位置
done = False # 建立一个变量，先为假
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
	myBall.move()

	# all re-draw
	if not done:
		screen.blit(myBall.image, myBall.rect)
		screen.blit(paddle.image, paddle.rect)
		screen.blit(score_text, textpos) # 把文本块移到这个位置
		
        # 生命计数器
        for i in range (lives):
			width = screen.get_width()
            # 放在右上角，剩几条命就显示几个球
			screen.blit(myBall.image, [width - 40 * i, 20])
		pygame.display.flip()

	# 如果球碰到底边就减一条命
	if myBall.rect.top >= screen.get_rect().bottom:
		lives = lives -1

		# 创建和绘制最终的分数文本
		if lives == 0:
			final_text1 = "Game Over"
			final_text2 = "Your final score is: " + str(points)
			ft1_font = pygame.font.Font(None, 70)
			ft1_surf = font.render(final_text1, 1, (0, 0, 0))
			ft2_font = pygame.font.Font(None, 50)
			ft2_surf = font.render(final_text2, 1, (0, 0, 0))
            # 文本居中
			screen.blit(ft1_surf, [screen.get_width()/2 - \
						ft1_surf.get_width()/2, 100])
			screen.blit(ft2_surf, [screen.get_width()/2 - \
						ft2_surf.get_width()/2, 200])
			pygame.display.flip()
			done = True # 当”命“用完时，避免球再次出现，结束游戏
		else:
			pygame.time.delay(2000)
			myBall.rect.topleft = [50, 50]
```

myBall.rect.top >= screen.get_rect().bottom：

- myBall是一个动画精灵，都包含一个rect
- screen是一个表面，不包含rect，可用get_rect()函数找到包围一个表面的rect

# 声音

在真实世界中，取不同的声音并把它们混合在一起的设备叫做”混音器“mixer。

程序产生声音2种方式：

- 生成或合成声音——制造不同音高和音量的声波来从头创建声音
- 播放一段录制的声音
  - 波形文件——*.wav pygame.mixer.Sound()
  - MP3文件——*.mp3 pygame.mixer.music.play()
  - WMA文件——*.wma
  - Ogg Vorbis文件*.ogg

```python
import pygame, sys
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode([640, 480])
pygame.time.delay(1000) # 延迟1秒让mixer完成初始化

splat = pygame.mixer.Sound("splat.wav") # 创建声音对象
splat.play() # no play
# (skier_env) hhh@eee:~/amtfbky/hfpy191008/child/mvfromgame191104$
# Fatal Python error: PyEval_SaveThread: NULL tstat
##########################################################################
# 在virtualenv虚拟环境里不能执行，害得我apt remove python2.7再加上apt autoremove
# 结果注销后不能进入桌面，本来准备重装；后在文字界面安装了lxde桌面，可以登入；在lxde里我
# 又装了dde，能登入deepin桌面了，右上角输入法的小键盘图标不见了，可以打字，但没有选字框
# 最后搜索用im-config命令一步步确定后搞定了
# 本来删除python27是为了安装python251,但make install后显示没有安装成功
# 追加：python2.5.1这又安装成功了，原因是sudo make install，这步要root权限
# 最搞笑的是折腾半天，结果splat.play()在没有进入虚拟环境就可以了，我不禁傻笑！！！
##########################################################################

pygame.mixer.music.load("bg_music.mp3") # 创建声音对象
pygame.mixer.music.set_volume(0.30)
pygame.mixer.music.play() # play ok

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
```

```python
import pygame, sys
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode([640, 480])
pygame.time.delay(1000) # 延迟1秒让mixer完成初始化

pygame.mixer.music.load("bg_music.mp3") # 创建声音对象
pygame.mixer.music.set_volume(0.30)
pygame.mixer.music.play() # play ok
splat = pygame.mixer.Sound("splat.wav") # 创建声音对象
splat.set_volume(0.50)
splat.play() # 这样会和背景音乐一起播放，不会等到背景音乐完了之后
# 我们希望一旦开始播放bgm时，Pygame就做好准备：如移动动画精灵或检查
# 是否有鼠标和键盘输入
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
```

让bgm播完再播音效，然后结束

```python
import pygame, sys
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode([640, 480])
pygame.time.delay(1000) # 延迟1秒让mixer完成初始化

pygame.mixer.music.load("bg_music.mp3") # 创建声音对象
pygame.mixer.music.set_volume(0.30)
pygame.mixer.music.play() # play ok
splat = pygame.mixer.Sound("splat.wav") # 创建声音对象
splat.set_volume(0.50)
# splat.play()

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	# 等bgm播完再播放音效，然后自动结束程序
	if not pygame.mixer.music.get_busy(): # 检查bgm是否播完
		splat.play()
		pygame.time.delay(1000) # 等待1秒让音效声结束
		sys.exit()
```

以上是一些声音播放的基础，接下来才是真正的游戏音乐！！！

## 重复音乐

只要程序在运行，bgm就一直播放：

还有很多地方需要添加声音：P245

- 球碰到两边的墙时
- 球碰到顶边而且玩家得分时
- 玩家漏球，球碰到底边时
- 新的一条命开始时
- 游戏结束时

```python
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
```

添加了不少的声音了，而且都可以正常工作，但游戏结束了，可以听到球好像还在墙上不停地反弹的声音！！！

原因：尽管球已经到达窗口底边，但它仍然在不停地移动！球在继续向下走，越走越远，没有什么来阻止它，所以它的y值会越来越大。虽然它在屏幕底边的“下面”，我们看不到，但是仍然能够听到它的声音！球仍在移动，所以当球的x值变得足够大或者足够小时，它还会在“左右两边”上反弹。这种情况发生在move()方法中，只要while循环在运行，这个方法就会一直运行。

解决：3种办法

- 游戏结束时把球的速度设置为[0,0]来阻止球继续移动
- 查看球是否在窗口底边以下，如果是，则停止播放hit_wall声音
- 检查done变量，如果游戏已经结束就不再播放hit_wall声音

