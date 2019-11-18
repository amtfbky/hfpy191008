## 第一章　变量与常量

### 1.1　什么是变量

#### 1.1.1　变量的定义

- 计算机内存中一个位置
- 计算机在执行程序时在此位置存储值并对其进行更改

假设变量是三个透明盒子A，B，C，分别装着三个数字10，2，3，现在要求你计算其中的10＋2，然后把结果放到C盒子中。

一、查看前两个盒子并检查它们的值

二、计算机的CPU计算10＋2

三、将结果放入C盒子里，会怎样？

#### 1.1.2　变量的特性

- 变量可以保存不同的值
- 一次只能保存一个值
- 只能等到赋给它新值，它才会改变
- 它帮助程序员与计算机内存中的数据进行交互

### 1.2　变量类型

变量类型的多样性是因为每种变量容纳的数据具有不同的类型。

整数

实数，也称浮点数

布尔

字符，字符系列就是字符串

### 1.3　Python中变量命名规则

- 只能包含英文大小写、数字和下划线，如：
- 大小写敏感，如：
-  不能有空格，一般将多个单词用下划线连接或驼峰写法，如：
-  可以下划线开头，数字则不行，如：
- 要有意义，和变量所含数据的含义和作用有关，如：

### 1.4　声明变量

#### 1.4.1　什么是声明

- 在内存中保留位置，在大多数情况下，程序员要指定数据类型，以便编译器或解释器知道要预留多少空间
- 接下来就是在该位置存储变量内容，这么一个过程叫做声明

#### 1.4.2　Python中怎么声明变量

Python不需要声明变量，首次使用变量会自动声明，如：

Num = 1

这条语句声明变量并将其初始化为1

## 第二章　输入与输出

### 2.1　print

```python
print(“hello world”)
```

```python
name = "张三"
print(name, "是个坏小子")
```

```python
name1 = "张三"
name2 = "李四"
print(name1, "是个坏小子，", name2, "也是个坏种")
```

这里可以看出：

- 要显示一个字符串，就必须用单引号或者双引号
- 要显示变量的内容，就不能加引号了

```python
print("求和2+3=：", 2 + 3)
```

可以在print()语句中计算数学表达式的结果。

### 2.2　print的default可以改变吗？

```python 
print("3rd", "July", "2019")
print("3rd", "July", "2019", sep = "/")
```

3rd July 2019

3rd/July/2019

在print()中，自定义分隔符

```python 
name = "Mary"
print("hello", name)
print("hi", name)
print("how do you do?", name)
```

hello Mary

hi Mary

how do you do? Mary

在name后面其实有一个参数，会自动打印一个“换行符”。

```python
name = "Mary"
print("hello", name, end = ";")
print("hi", name, end = ";")
print("how do you do?", name, end = ".")
```

hello Mary;hi Mary;how do you do? Mary.

在name后面设置end参数，就不会自动换行了

```python
print("how do you do?\nI'm fine.\nAnd you?")
```

how do you do?

I'm fine.

And you?

也可以加上特殊的字符系列\n（打印换行符）

```python
print("1\tone\n2\ttwo")
```

1	one

2	two

还有个有趣的特殊字符系列\t，制表符用于对齐输出

用户输入及提示

```python
name = input("What's your name? ")
print("Hello,", name)
```

What's your name? Mary

Hello, Mary

执行流程：

- 当执行input()时，显示What's your name?，流程停止，等待用户输入名字
- print()尚未执行，只要用户不输入，计算机就一直等待
- 当用户输入名字并按下回车键，才会执行print()

```python
name = input("name: ") # 提示要有文字说明，否则用户不知道要输入什么，这是用户友好
age = int(input("age: "))
defen = float(input("defen: "))
print(name, "age: ", age, "defen: ", defen)
```

name: Mary

age: 8

defen: 99.5

Mary age: 8 defen: 99.5

## 第三章　运算符

### 3.1　赋值运算符

在数学中，a = 15和15 = a是等价的

在Python中：

- a = 15，将15赋给a，或设置a等于15
- 等号左侧的变量表示内存中一个可存储值的区域；右侧可以有数字、变量、字符串甚至复杂的数学表达式

| 赋值语句          | 语句说明                                             |
| ----------------- | ---------------------------------------------------- |
| a = 15            | 将15赋给a                                            |
| b = c             | 将变量c的内容赋值给变量b                             |
| d = "Hello world" | 将字符串赋值给变量d                                  |
| a = b + c         | 计算变量b和c的内容的和，将和赋值给a                  |
| m = a + 2         | 计算变量a的内容与2的和，将和赋值给m，变量a的内容不变 |
| n = n + 1         | 计算变量n的内容与1的和，将和赋值给n＝将变量n的值加1  |
| a = b = c = 8     | 将单个值赋给多个变量                                 |
| a, b, c = 1, 2, 3 | 将多个值赋给多个变量                                 |

### 3.2　算术运算符

| 算术运算符 | 说明 | 式子 |
| ---------- | ---- | ---- |
| +          | 加   | 1+2  |
| -          | 减   | 2-1  |
| *          | 乘   | 2*3  |
| /          | 除   | 6/2  |
| **         | 幂   | 2**3 |

在Python算式中，小括号代表运算优先，没有中括号和大括号。

a = 8 * (3 + 9 * ( 2 + 4 * (7 - 6 / 2)))

### 3.3 算术运算符的优先级

由高到低：** -> *,/ -> +,-

a = 8 / 4 * 2

等级一样，按从左到右执行

a = 8 / (4 * 2)

这样就是小括号里的优先运算

运算顺序总结：

1.括号内的运算总是最先执行

2.执行幂运算

3.先乘除后加减，等级一样的从左到右执行

a = (15 + 3) - 3 + 2 ** 3 / 2 * 5

### 3.4 复合赋值运算符

| 运算符 | 说明           | 式子          |
| ------ | -------------- | ------------- |
| +=     | 加法赋值运算符 | a += 1,a += b |
| -=     | 减法赋值运算符 | a -= 1        |
| *=     | 乘法赋值运算符 | a *= 2        |
| /=     | 除法赋值运算符 | a /= 2        |
| **=    | 幂同仁运算符   | a **= 2       |

### 3.5 字符串运算符

将两个字符串合并为一个字符串——拼接，它有两个运算符

```python
a = "Hello, "
b = "nice to meet you!"
c = a + b
print(c)
```

这是拼接运算符

```python
a = "Hello, "
a += "nice to meet you!"
print(a)
```

这是拼接赋值运算符

练习一下：

```python
# ex1
# Data input - Prompt the user to enter values for base and height
base = float(input("Enter the length of Base: "))
height = float(input("Enter the length of Height: "))

# Data processing - Calculate the area of the rectangle
area = base * height

# Results output - Display the result on user's screen
print("The area of the rectangle is", area)
```

```python
# ex2
# Data input - Prompt the user to enter a value for radius
radius = float(input("Enter the length of Radius: "))

# Data processing - Calculate the area of the circle
area = 3.14159 * radius ** 2

# Results output - Display the result on user's screen
print("The area of the circle is", area)
```

```python
# ex3
# Data input - Prompt the user to enter a temperature value
# in degrees Fahrenheit
fahrenheit = float(input("Enter a temperature in Fahrenheit: "))

# Data processing - Calculate the degrees Celsius equivalent
celsius = 5 / 9 * (fahrenheit -32)

# Results output - Display the result on user's screen
print("The temperature in Celsius is", celsius)
```

## 第四章　操作数字

### 4.1　函数和方法

整数值

```python
a = 8.9
b = int(a)
print(b)

print(int(89))
print(int(8.9))
print(int(-8.9))

c = "8"
d = "9"
print(c + d)
print(int(c) + int(d))
```

最大值max，最小值min

```python
a = 1
b = 2
c = 3
d = 4
e = max(a, b, c, d)
print(e)

print(max(1, 2, 3, 4))

seq = [1, 2, 3, 4]
print(max(seq))
```

实数值

```python
a = "2.2"
b = "3.3"
print(a + b)
print(float(a) + float(b))
```

数值范围

```python
# Assign sequence [1, 2, 3, 4, 5] to variable a
a = range(1, 6)

# Assign sequence [0, 1, 2, 3, 4, 5] to variable b
b = range(6)

# Assign sequence [0, 10, 20, 30, 40] to variable c
c = range(0, 50, 10)

# Assign sequence [100, 95, 90, 85] to variable d
d = range(100, 80, -5)
```

随机整数

```python 
import random # import random module

# Display a random integer between 10 and 100
print(random.randrange(10, 101))

# Assign a random integer between 0 and 10 to variable x
x = random.randrange(11)
# and display it
print(x)

# Display a random integer between -20 and 20
print(random.randrange(-20, 21))

# Display a random odd integer between 1 and 97
print(random.randrange(1, 99, 2))

# Display a random even integer between 0 and 98
print(random.randrange(0, 100, 2))
```

>#### 提示
>
>随机数在计算机游戏中广泛地应用，如：一个“敌人”可能在随机的时间出现，或沿随机的方向移动；在其它如模拟程序、统计程序、安全领域的数据加密等等也是广泛应用。

求和

```python
import math

seq = [2.2, 3, 4]
print(math.fsum(seq))
```

平方根

```python
import math

print(math.sqrt(9))
print(math.sqrt(81))
```

## 第五章　操作字符串

### 5.1　索引

```python
s = "abcdefghijklmnopqrstuvwxyz"
print(s[0])
print(s[9])
print(s[25])
print(s[-1])
print(s[-26])

name = "Mary"
letter1, letter2, letter3, letter4 = name
print(letter1)
print(letter2)
print(letter3)
print(letter4)
```

>### 提示
>
>name变量的字符串字符数量必须匹配要被赋值的变量数，否则Python会报错

### 5.2　切片

公式：subject[[beginIndex] : [endIndex]]

```python
n = "123456789"
print(n[3:6]) # 456
print(n[:6]) # 123456
print(n[6:]) # 789
print(n[2:8:2]) # 357
print(n[6:-2]) # 7
print(n[-6:-3]) # 456
print(n[-6:]) # 456789
print(n[:-3]) # 123456
```

### 练习

第一种方式

```python
s = "abcd"
s_reversed = s[3] + s[2] + s[1] + s[0]
print(s_reversed)
```

第二种方式

```python
s = "abcd"
a, b, c, d = s
s_reversed = d + c + b + a
print(s_reversed)
```

第三种方式

```python
s = "abcd"
s_reversed = s[::-1] # 用－1作为参数step的值
print(s_reversed)
```

### 5.3　函数和方法

字符串替换

subject.replace(search, replace)

在subject中搜索内容，并用replace替换search

```python
a = "I am newbie in Go. Python rocks!"
b = a.replace("Go", "C++")
print(b)
print(a)
```

字符计数

len(subject)

此函数返回subject的长度，即subject包含的字符数（包括空格字符、符号、数字等）

```python
a = "abcd efg hik, lmn32"
print(len(a))

b = "opq rst uv, wxyz543"
c = len(b)
print(c)
```

查找字符串的位置

```python
a = "I am newbie in Python rocks!"
i = a.find("newbie")
print(i) # 5
print(a.find("Python")) # 15
print(a.find("rocks")) # 22
```

转换为大小写字符串

```python
a = "What's Your Name?"
b = a.lower()
print(b)
print(a)

c = a.upper()
print(c)
print(a)

d = a.replace("Your", "his").upper() # 链接方法
print(d)
print(a)
```

将数字转换为字符串

```python
age = int(input("Enter your age: "))
new_age = age + 5
msg = "You'll be " + str(new_age) + " years old in 5 years from now."
print(msg)
```

### 练习

1.用户输入姓名，取姓名的前3个字母（大写）和一个随机的3位整数创建一个登录ID。

分析：这就要用到切片、大写、取随机数三个方法，3位整数的数字范围介于100～99之间。

```python
import random
last_name = input("Enter your name: ")

# Get a random integer between 100 and 999
random_int = random.randrange(100, 1000)

# Create login ID
login_id = last_name[:3].upper() + str(random_int)
print(login_id)
```

2.切换名字的顺序：查找、切片

```python
full_name = input("Enter your full name: ")

# Find the position of space character. This is also the number
# of characters first name contains
space_pos = full_name.find(" ")

# Get space_pos number of characters starting from position 0
name1 = full_name[:space_pos]

# Get the rest of the characters starting from position space_pos + 1
name2 = full_name[space_pos + 1:]

full_name = name2 + " " + name1
print(full_name)
```

3.创建一个随机单词

```python
import random
a = "abcdefghijklmnopqrstuvwxyz"
random_letter1 = a[random.randrange(26)] # len(a)=26
# random_letter1 = a[random.randrange(len(a))] 嵌套
random_letter2 = a[random.randrange(26)]
random_letter3 = a[random.randrange(26)]
random_letter4 = a[random.randrange(26)]
random_word = random_letter1 + random_letter2 + \
							random_letter3 + random_letter4
print(random_word)
```

## 第六章　分支结构

顺序结构转向决策结构（选择结构）：在一种情况下执行一个程序，在另一种情况下执行一个程序。

### 6.1　提出简单问题：布尔表达式

Operand1 Comparison_Operator Operand2，如：2 != 3，3 > 2

| 比较运算符 | 说明             |
| ---------- | ---------------- |
| ==         | 相等（不是赋值） |
| !=         | 不相等           |
| >          | 大于             |
| <          | 小于             |
| >=         | 大于等于         |
| <=         | 小于等于         |

当你写出一个式子，计算机的理解是：

- a > b，“a大于b吗？”
- s == "abc"，“s等于abc吗？”，也就是“s的内容是abc吗？”
- 2 != 3，“2不等于3吗？”
- a == 3，“a等于3吗？”

计算机很勤劳，不光提出问题，还自动判断并给出答案。

虽然计算机给了答案，但我们也先要学习如何给一个式子作出判断：

| a    | b    | a == 8 | a >= b |
| ---- | ---- | ------ | ------ |
| 8    | 9    | True   | False  |
| 3    | 8    | False  | False  |
| -2   | -3   | False  | True   |
| -4   | 6    | False  | False  |
| 8    | 8    | True   | False  |
| 12   | 7    | False  | True   |

### 6.3　提出复杂问题：复合布尔表达式

Boolean_Expression1 Logical_Operator Boolean_Expression2，如：a == 2 and b > 3

and运算符

| 布尔表达式1(BE1) | 布尔表达式2(BE2) | BE1 and BE2 |
| ---------------- | ---------------- | ----------- |
| False            | False            | False       |
| False            | True             | False       |
| True             | False            | False       |
| True             | True             | True        |

or运算符

| 布尔表达式1 | 布尔表达式2 | BE1 and BE2 |
| ----------- | ----------- | ----------- |
| False       | False       | False       |
| False       | True        | True        |
| True        | False       | True        |
| True        | True        | True        |

not运算符

| 布尔表达式(BE) | not BE |
| -------------- | ------ |
| False          | True   |
| True           | False  |

### 6.4 成员关系运算符

| 成员关系运算符 | 说明                                          |
| -------------- | --------------------------------------------- |
| in             | 在指定系列中找到值返回True，否则返回False     |
| not in         | 在指定系列中没有找到值返回True，否则返回False |

如：a in [1, 2, 3，]a in "abc"，a in ["a", "b", "c"，]a not in ["a", "b", "c"]

### 6.5　逻辑运算符的优先顺序

not > and > or，如：name == "Mary" or age > 8 and not name == "Aaron"

### 6.6 算术、比较和逻辑运算符的优先顺序

算术运算符 > 比较运算符和成员运算符 > 逻辑运算符，如：a * b + 3 > 15 or not(c == b / 2) and c > 8

设：a = 1, b = -3, c = 8

第一步：1 * -3 + 3 = -3 + 3 = 0,-3 / 2 = -1.5

第二步：0 > 15:False,c == -1.5:False,c > 8:False

第三步：False or not False and False

第四步：False or True and False

第五步：False or False

结果：False

### 6.6　将自然语句转换为布尔表达式

根据年龄分组：岁

- 9～12: age >= 9 and age <= 12
- <8 or >11: age < 8 or age > 11
- 8 or 10 or 12: age == 8 or age == 10 or age == 12
- 6~8 or 10~12: age >= 6 and age <= 8 or age >= 10 and age <= 12
- not 10 and not 12: age != 10 and age != 12 或：age not in [10, 12]

### 6.7 if结构：一条路径

if Boolean_Expression:

​    \# Here goes a statement or block of statements

```python
age = int(input("Enter your age: "))

if age < 18:
	print("You are underage!")
	print('You have to wait foe a few more years.')

name = input("Enter your name of an olympian: ")

if name == "Zeus": # name = "Zeus" x
	print("You are the king of the Gods!")

print("You live on Mount olympian.")
```

#### 练习

1.

```python
a = int(input()) # 2 4

b = 3
if a * 2 > 6:
	b = a * 3
	a = a * 2

print(b, a)
```

2.找出体重最轻的人

```python
# 不使用min()
w1 = int(input("Enter the weight of the 1st person: "))
w2 = int(input("Enter the weight of the 2nd person: "))
w3 = int(input("Enter the weight of the 3rd person: "))
w4 = int(input("Enter the weight of the 4th person: "))
# memorize the weight of the first person
minimum = w1

# If second one is lighter, forget everything and memorize this weight
if w2 < minimum:
	minimum = w2
# If third one is lighter, forget everything and memorize this weight
if w3 < minimum:
	minimum = w3
# If fourth one is lighter, forget everything and memorize this weight
if w4 < minimum:
	minimum = w4

print(minimum)
```

```python
# 使用min()
w1 = int(input("Enter the weight of the 1st person: "))
w2 = int(input("Enter the weight of the 2nd person: "))
w3 = int(input("Enter the weight of the 3rd person: "))
w4 = int(input("Enter the weight of the 4th person: "))
print(min(w1, w2, w3, w4))
```

3.找出体重最重的人的名字

```python
w1 = int(input("Enter the weight of the 1st person: "))
n1 = input("Enter the name of the person: ")
w2 = int(input("Enter the weight of the 2nd person: "))
n2 = input("Enter the name of the 2nd person: ")
w3 = int(input("Enter the weight of the 3rd person: "))
n3 = input("Enter the name of the 3rd person: ")

maximum = w1
m_name = n1 # this variable holds the name of the heaviest person

if w2 > maximum:
	maximum = w2
	m_name = n2 # Someone else is heavier, Keep his or her name.

if w3 > maximum:
	maximum = w3
	m_name = n3 # Someone else is heavier, Keep his or her name.

print("The heaviest person is", m_name)
print("His or her weight is", maximum)
```

### 6.8 if-else结构：两条路径

if Boolean_Expression:

​    \# Here goes a statement or block of statements 1

else:

​    \# Here goes a statement or block of statements 2

```python
age = int(input("Enter your age: "))
if age >= 18:
	print("You are an adult!")
else:
	print("You are underage!")
```

#### 练习

1.

```python
a = int(input()) # 3 -3 0
if a > 0:
	print("Positive")
else:
	print("Negative")
```

>### 提示
>
>这个程序不是很正确，0不是一个负值！也不是一个正值。

2.谁是最大值？

第一种方法：if-else

```python
a = float(input("Enter number A: "))
b = float(input("Enter number B: "))

if b > a:
	maximum = b
else:
	maximum = a

print("Greatest value:", maximum)
```

第二种方法：if

```python
a = float(input("Enter number A: "))
b = float(input("Enter number B: "))

maximum = a
if b > a:
	maximum = b

print("Greatest value:", maximum)
```

第三种方法：Python化

```python
a = float(input("Enter number A: "))
b = float(input("Enter number B: "))

maximum = max(a, b)
print("Greatest value:", maximum)
```

3.将加仑转换为公升，反之亦然

```python
COEFFICIENT = 3.785

print("1: Gallons to liters")
print("2: Liters to gallons")
choice = int(input("Enter choice: "))

quantity = float(input("Enter quantity: "))

if choice == 1:
	result = quantity * COEFFICIENT
	print(quantity, "gallons =", result, "liters")
else:
	result = quantity / COEFFICIENT
	print(quantity, "liters =", result, "gallons")
```

### 6.9 if-elif结构

if-elif结构用于扩展选择分支的数量。

if Boolean_Expression_1:

​    \# Here goes a statement or block of statements 1

elif Boolean_Expression_2:

​    \# Here goes a statement or block of statements 2

elif Boolean_Expression_3:

​    \# Here goes a statement or block of statements 3

......

elif Boolean_Expression_N:

​    \# Here goes a statement or block of statements N

else:

​    \# Here goes a statement or block of statements N + 1

#### 练习

1.

```python
a = int(input()) # 5 2 1
b = int(input()) # 8 0 -1

if a > 3:
	print("Message #1")
elif a > 1 and b <= 10:
	print("Message #2")
	print("Message #3")
elif b == 0: # 虽然可能是True，但它永远不会被检查
	print("Message #4")
else:
	print("Message #5")

print("The end!")
```

2.计算位数，0～999

```python
a = int(input("Enter an integer (0 - 999): "))

if a <= 9:
	count = 1
elif a <= 99:
	count = 2
else:
	count = 3

print("You entered a ", count, "-digit number", sep = "")
```

让程序更完善些，在用户输入的数字不介于0～999之间时显示错误信息。

```python
a = int(input("Enter an integer (0 - 999): "))

if a < 0 or a > 999:
	print("Wrong number!")
elif a <= 9:
	print("You entered a 1-digit number")
elif a <= 99:
	print("You entered a 2-digit number")
else:
	print("You entered a 3-digit number")
```

3.星期几，输入1～7之间的数字，显示相应的星期几；如果输入的数字无效，则显示一条错误信息。

```python
day = int(input("Enter a number between 1 and 7: "))

if day == 1:
	print("Sunday")
elif day == 2:
	print("Monday")
elif day == 3:
	print("Tuesday")
elif day == 4:
	print("Wednesday")
elif day == 5:
	print("Thursday")
elif day == 6:
	print("Friday")
elif day == 7:
	print("Saturday")
else:
	print("Invalid Number")
```

4.过路费，坑爹

收费站系统自动识别车辆并收费：M摩托车￥1，C汽车￥2，T卡车￥3；如果用户输入的不是这三个字符，报错。

```python
v = input("Enter the type of vehicle (M, C, T): ")

if v == "M":
	print("You need to pay $1")
elif v == "C":
	print("You need to pay $2")
elif v == "T":
	print("You need to pay $3")
else:
	print("Invalid vehicle")
```

### 6.10　嵌套结构

#### 练习

1.1，2，3

```python
a = int(input("Enter a number: "))
if a < 1 or a > 3:
	print("Invalid Number")
else:
	print("Valid Number")

	if a == 1: # this is the nested if-elif structure
		print("1st choice selected")
	elif a == 2:
		print("2nd choice selected")
	else:
		print("3rd choice selected")
```

2.

```python
a = int(input()) # 11 19 31
b = 10
if a < 30:
	if a < 15:
		b = b + 2
	else:
		b -= 1
else:
	b += 1

print(b)
```

3.Positive,Negative,Zero

The 1st Mothod:

```python
a = float(input("Enter a number: "))

if a > 0:
	print("Positive")
else:
	if a < 0:
		print("Negative")
	else:
		print("Zero")
```

The 2nd Mothod:

```python
a = float(input("Enter a number: "))

if a > 0:
	print("Positive")
elif a < 0:
	print("Negative")
else:
	print("Zero")
```

3.最科学的计算器

```python
a = float(input("Enter 1st number: "))
op = input("Enter type of operation: ") # Variable op is of type string
b = float(input("Enter 2nd number: "))

if op == "+":
	print(a + b)
elif op == "-":
	print(a - b)
elif op == "*":
	print(a * b)
elif op == "/":
	if b == 0:
		print("Error: Division by zero")
	else:
		print(a / b)
```

## 第七章　循环

一种允许多次执行语句或语句块直到满足指定条件的结构。

### 7.1 while结构

while Boolean_Expression:

​    \# Here goes a statement or block of statements

#### exercise

1.计算迭代的总次数

```python
i = 1
while i < 4:
	print("hi,how do you do?")
	i += 1

print("Over!")
```

2.计算四个数字的总和

```python
total = 0
i = 1
# while i <= total_number_of_iterations:
while i <= 4:
	# here goes a statement or block of statements
	a = float(input("Enter a number: "))
	total = total + a
	i += 1
print(total)
```

3.计算20个正数的总和

```python
total = 0 
i = 1
while i <= 20:
	a = float(input("Enter a number: "))
	if a > 0:
		total = total + a
	i += 1
print(total)
```

4.计算N个数字的总和

```python
n = int(input("How many numbers are you going to enter? "))
total = 0
i = 1
while i <= n:
	a = float(input("Enter a number: "))
	total += a
	i += 1
print(total)
```

5.计算未知数量的数字之和a! = -1

```python
total = 0
a = float(input())
if a != -1:
	total += a
	a = float(input())
	if a != -1:
		total += a
		a = float(input())
		if a != -1:
			total += a
			a = float(input())
			...
			...
print(total)
```

```python
total = 0
a = float(input())
while a != -1:
	total += a
	a = float(input())

print(total)
```

6.计算五个数字的乘积

```python
n = 1

a = float(input())
n *= a

a = float(input())
n *= a

a = float(input())
n *= a

a = float(input())
n *= a

a = float(input())
n *= a

print(n)
```

```python
n = 1
i = 1
while i <= 5:
	a = float(input())
	n *= a
	i += 1
print(n)
```

### 7.2 for结构

比while结构更具可读性和更方便的特殊语句。

for var in sequence:

​    \# Here goes a statemnet or block of statements

```python
for i in [1, 2, 3, 4, 5]:
	print(i, end = " ")

for letter in "Python":
	print(letter, end = "-")
```

for var in range([initial_value,] final_value [, step]):
	\# Here goes a statement or block of statements

- initial_value是序列的起始值，可选，如果省略，其默认值为0
- 该序列一直到final_value，但不包括final_value
- step是序列中每个数字之间的差值，可选，如果省略，其默认值为1

```python
for i in range(0, 11, 1):
	print(i, end = " ")
print()

for i in range(0, 11):
	print(i, end = " ")
print()

for i in range(11):
	print(i, end = " ")
print()
```

```python
for i in range(2, 12, 2): # step=2
	print(i, end = " ")
print()
```

```python
a = 11
b = 0
for i in range(a, b, -2): # step=-2
	print(i, end = " ")
print()
```

#### exercise

1.3次迭代

```python
a = int(input())
for i in range(-3, 3, 2): # -3,-1,1
	a = a * 3
print(a)
```

2.

```python
a = int(input()) # 3
for i in range(6, a - 1, -1): #	 2 3 4 5 6
  			      #	-5-4-3-2-1
	print(i, end = " ")
print()
```

3.计算4个数字的和

```python
total = 0
for i in range(4):
	a = float(input("Enter a number: "))
	total += a
print(total)
```

4.求N个数的平均值

```python
n = int(input("How many numbers are you going to enter? "))
total = 0
for i in range(n):
	a = float(input("Enter number No" + str(i + 1) + ": ")) # i + 1,a = *
	total += a
if n > 0:
	average = total / n
	print("The average value is:", average)
else:
	print("You didn't enter any number!")
```

>### 提示
>
>如果用户输入n＝0或负值，可以避免错误。

### 7.3　嵌套

嵌套循环是指被包含在另一个循环中的循环，也可以说是一个位于外循环中的内循环。外循环控制内循环的完整迭代次数。

迭代步骤：

- 外循环的第一次迭代触发内循环开始迭代直到完成迭代
- 然后外循环的第二次迭代触发内循环开始迭代直到再次完成
- 这个过程重复进行，直到外循环完成所有的迭代

```python
for i in range(1, 3): # 1,2
	for j in range(1, 4): # 1,2,3
		print(i, j)
```

```python
i = 1 # outer loop assigns value 1 to variable i
for j in range(1, 4): # and inner loop performs three iterations
	print(i, j)

i = 2 # outer loop assigns value 2 to variable i
for j in range(1, 4): # and inner loop starts over and
                      # performs three new iterations
	print(i, j)
```


