import copy

class Animal:
    def __init__(self, name, number_of_legs, color):
        self.name = name
        self.number_of_legs = number_of_legs
        self.color = color

harry = Animal('hippogriff', 6, 'pink')
carrie = Animal('chimera', 4, 'green polka dots')
billy = Animal('bogill', 0, 'paisley')
my_animals = [ harry, carrie, billy ]
more_animals = copy.copy(my_animals) # no deepcopy
# print(more_animals[0].name)
# print(more_animals[1].name)

# 浅拷贝不会拷贝被拷贝对象中的对象
# 原列表的元素即对象一改动，"新列表"也改动
# my_animals[0].name = 'ghoul'
# print(my_animals[0].name)
# print(more_animals[0].name)

# 浅拷贝不会拷贝被拷贝对象中的对象
# 原列表改动，"新列表"却没有变化
# sally = Animal('sphinx', 4, 'sand')
# my_animals.append(sally)
# print(len(my_animals)) #4
# print(len(more_animals)) #3

# deepcopy会创建被拷贝对象中的所有对象的拷贝
# 原列表的元素即对象的改动不会影响到新列表
more_animals = copy.deepcopy(my_animals)
my_animals[0].name = 'wyrm'
print(my_animals[0].name)
print(more_animals[0].name)

#喀迈拉（古希腊故事中狮头、羊身、蛇尾的吐火怪物）绿色圆点花纹
#佩斯利（旋涡纹）图案
# 斯芬克斯，狮身人 沙色
# （欧洲的）龙