# -*- coding:utf-8 -*-

import random
secret = random.randint(1, 100)
guess = 0
tries = 0

print "AHOY! I'm the Dread Pirate Roberts, and I have a secret!"
print "It is a number from 1 to 99. I'll give you 6 tries."
while guess != secret and tries < 6:
    guess = input("what's your guess?")
    if guess < secret:
        print "Too low, ye scurvy dog!"
    elif guess > secret:
        print "Too high, landlubber!"
    tries = tries + 1

if guess == secret:
    print "Avast! Ye got it! Found my secret, ye did!"
else:
    print "No more guesses! Better luck next time, matey!"
    print "The secret number was", secret

"""
太低了，你这个坏蛋！
喂我是可怕的海盗罗伯茨，我有个秘密！
它是一个从1到99的数字。我给你6次机会。
太高了，软垫(不谙航海的人)！
前卫你明白了找到我的秘密了！
别再猜了下次好运，伙计！
"""