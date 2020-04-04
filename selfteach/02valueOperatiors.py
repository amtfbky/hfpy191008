"""
值～～～～
从本质上看，程序里的绝大多数语句包含着运算Evaluation
——对某个值进行评价：（运算）
    不是判断某人某事的好坏
    而是计算出某个值究竟是什么
接下来要学习的：
    无非就是熟悉各种数据类型，及其相应的操作
    无论是操作符还是函数都会返回一个相应的值及其相应的布尔值
    ——总而言之就是各种数据类型的运算而已

流程控制～～～～
    无论多复杂的流程控制用这两个东西就够了
    就好象无论多复杂的电路最终都是由通路和开路仅仅两个状态构成的一样
"""
from random import randrange

coin_user, coin_bot = 10, 10 # 可以用一个赋值符号分别为多个变量赋值
rounds_of_game = 0

def bet(dice, wager):    # 接收两个参数，一个是骰子点数，另一个用户的输入
    if dice == 7:
        print(f'The dice is {dice};\nDRAW!\n') # \n 是换行符号
        return 0
    elif dice < 7:
        if wager == 's':
            print(f'The dice is {dice};\nYou WIN!\n')
            return 1
        else:
            print(f'The dice is {dice};\nYou LOST!\n')
            return -1
    elif dice > 7:
        if wager == 's':
            print(f'The dice is {dice};\nYou LOST!\n')
            return -1
        else:
            print(f'The dice is {dice};\nYou WIN!\n')
            return 1

while True:         #  除 for 之外的另外一个循环语句
    print(f'You: {coin_user}\t Bot: {coin_bot}')
    dice = randrange(2, 13)   # 生成一个 2 到 12 的随机数
    wager = input("What's your bet? ")
    if wager == 'q':
        break
    elif wager in 'bs':  # 只有当用户输入的是 b 或者 s 得时候，才 “掷骰子”……
        result = bet(dice, wager)
        coin_user += result    # coin_user += result 相当于 coin_user = coin_user + result
        coin_bot -= result
        rounds_of_game += 1
    if coin_user == 0:
        print("Woops, you've LOST ALL, and game over!")
        break
    elif coin_bot == 0:
        print("Woops, the robot's LOST ALL, and game over!")
        break

print(f"You've played {rounds_of_game} rounds.\n")
print(f"You have {coin_user} coins now.\nBye!")
