# 把起始体重和每年增加的重量当作参数创建一个函数

def calculate_weight(weight, increase):
    for year in range(1, 16):
        weight = weight + increase
        moon_weight = weight * 0.165
        print('Year %s is %s' % (year, moon_weight))

calculate_weight(40, 0.5)