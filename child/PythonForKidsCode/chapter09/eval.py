# eval: evaluate
# eval('print("wow")') # print("wow")

# print(eval('10*3'))

# print(eval('''if True:
# 	print("no work")'''))
# Traceback (most recent call last):
#   File "eval.py", line 7, in <module>
#     print("no work")'''))
#   File "<string>", line 1
#     if True:
#      ^
# SyntaxError: invalid syntax

calculation = input('Enter a calculation: ')
print(eval(calculation))