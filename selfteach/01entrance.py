"""
逻辑关系应该能用符号表示——乔治。布尔
战略：藐视它

程序：按照一定顺序完成任务的流程（Procedures）
计算机能做布尔运算Boolean Operations：
    不只按照顺序执行任务
    根据不同情况执行不同的任务
可编程Programable：
    布尔运算及其相应的流程控制Control Flow
    没有布尔运算能力就没有流程控制，没有流程控制就不智能


"""
# from Ipython.core.interactiveshell import InteractiveShell
# InteractiveShell.ast_node_interactivity = "all"

# print(1 == 2)
# print(1 != 2)

# print('(True and False) yields:',  True and False)
# print('(True and True) yields:',  True and True)
# print('(False and True) yields:',  False and True)
# print('(True or False) yields:',  True or False)
# print('(False or True) yields:',  False or True)
# print('(False or False) yields:',  False or False)
# print('(not True) yields:',  not True)
# print('(not False) yields:',  not False)

# import random
# r = random.randrange(1, 1000)
# # 请暂时忽略以上两句的原理，只需要了解其结果：
# # 引入随机数，而后，每次执行的时候，r 的值不同

# if r % 2 == 0:
#     print(r, 'is even.')
# else:
#     print(r, 'is odd.')

# 打印出100以内所有的质数
# 算法：
#     1.设n为整数，n>=2
#     2.若n==2，n是质数
#     3.若n>2，就把n作为被除数，从2开始一直到n-1都作为除数，
# 逐一计算看余数是否＝0
#         3.1若余数等于0，不是质数
#         3.2若都不等于0，是质数
# 于是：
#     需要两个嵌套的循环：
#         1.让被除数n从2遍历到99（题目是100以内，不包含100）
#         2.在前者内部让除数i从2到n-1的循环

# for n in range(2, 100): #range(2,100)表示含左侧 2，不含右侧 100，是不是第三次看到这个说法了？
#     if n == 2:
#         print(n)
#         continue
#     for i in range(2, n):
#         if (n % i) == 0:
#             break
#     else:                  # 这里目前你可能看不懂…… 但先关注结果吧。
#         print(n)

# 算法改进：优化
#     从2作为除数开始试，试到n的开方之后的一个整数就可以了……

# for n in range(2, 100):
#     if n == 2:
#         print(n)
#         continue
#     for i in range(2, int(n ** 0.5)+1): #为什么要 +1 以后再说…… n 的 1/2 次方，相当于根号 n。
#         if (n % i) == 0:
#             break
#     else:
#         print(n)

# def is_prime(n):            # 定义 is_prime()，接收一个参数
#     if n < 2:              # 开始使用接收到的那个参数（值）开始计算……
#         return False       # 不再是返回给人，而是返回给调用它的代码……
#     if n == 2:
#         return True
#     for m in range(2, int(n**0.5)+1):
#         if (n % m) == 0:
#             return False
#     else:
#         return True

# for i in range(80, 100):
#     if is_prime(i):          # 调用 is_prime() 函数，
#         print(i)            # 如果返回值为 True，则向屏幕输出 i
