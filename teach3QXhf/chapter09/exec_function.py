my_small_program = '''print('ham')
print('sandwich')'''

exec(my_small_program)

# 三明治
# 火腿
运行Python程序从文件中读入的小程序，也就是程序中又包含了程序！
这在写很长、很复杂的程序时可能很有用。
如：两个机器人（读入Python程序脚本，用exec来运行）在屏幕上移动并试图攻击对方。