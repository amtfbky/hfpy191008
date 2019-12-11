"""
============ 文件与异常 ============

open()与for文句结合=非常容易读取文件
创建一个迭代器从文件向你的代码输入数据行，一次传入一行数据

-------- 处理异常 ---------
exception
不能忽略，而是要捕获异常，确保程序健壮
先尝试运行，再恢复
try:
    code
except:

需要考虑的只是IOError和ValureError

------- 特定指定异常 --------
try:
    ...
except IOError:如果出现的是不同类型的错误，...
    ...

"""
import os

os.getcwd()
os.chdir('../xxx/xxx')

file1 = open('sketch.txt')
#1.读取前两行
print(file1.readline(), end='')
print(file1.readline(), end='')

#2.“退回”到文件起始位置，用for处理文件
file1.seek(0)
for i in file1:
    print(i, end='')

#3.查看数据的规律，用:分割
for i in file1:
    (role, spoken) = i.split(':')
    print(role, end='')
    print(' said: ', end='')
    print(spoken, end='')

#4.错误ValueError“值过多”，有两个:，split()不知道如何处理
#split()有个可选参数控制数据行分解成几个部分
for i in file1:
    #注意可选参数1,表示只处理一个:
    (role, spoken) = i.split(':', 1)
    print(role, end='')
    print(' said: ', end='')
    print(spoken, end='')

#5.又有错误了（需要不只一个值），缺少:
#处理错误：逻辑处理、疏导错误
#5.1额外逻辑
for i in file1:
    #这对有:的句子管用，但其它的情况呢？有点脆弱
    #比如这个数据文件被删除了——IOError（重命名文件试试）
    #5.1.1增加检查文件是否存在if os.path.exists('xxx'):
    if not i.find(':') == -1:
        (role, spoken) = i.split(':', 1)
        print(role, end='')
        print(' said: ', end='')
        print(spoken, end='')

#5.2
#5.2.1try:...except:print('the file is missing')
for i in file1:
    try:
        #保护下面四句代码
        (role, spoken) = i.split(':', 1)
        print(role, end='')
        print(' said: ', end='')
        print(spoken, end='')
    except:
        pass
file1.close()
