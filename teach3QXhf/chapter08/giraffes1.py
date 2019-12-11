# 对象是程序组织代码的方法，它把复杂的想法拆分开来使其更容易被题解
# 在Python里，对象是由“类”定义的，类是把对象分组归类的方法

class Things:
    pass

class Inanimate(Things):
    pass

class Animate(Things):
    pass

class Animals(Animate):
    def breathe(self):
        print('breathing')
    def move(self):
        print('moving')
    def eat_food(self):
        print('eating food')

class Mammals(Animals):
    def feed_young_with_milk(self):
        print('feeding young')

class Giraffes(Mammals):
    def eat_leaves_from_trees(self):
        print('eating leaves')
    
    # calls the move and eat_food
    def find_food(self):
        self.move()
        print("I've found food!")
        self.eat_food()

    def dance_a_jig(self): #吉格舞
        self.move()
        self.move()
        self.move()
        self.move()
        
reginald = Giraffes()
# harold = Giraffes()
# reginald.move()
# harold.eat_leaves_from_trees()
reginald.find_food()
reginald.dance_a_jig()

'''哺乳动物
长颈鹿
雷金纳德
哈罗德'''