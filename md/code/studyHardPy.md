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

```python
for i in range(3):
	for j in range(4):
		print("I love you!Mum!") # 3x4=12
```

#### exercise

1.a=?

```python
a = 1
i = 5
while i <= 7: # 5 6 7
	for j in range(1, 5, 2): # 1 3
		a *= 2
	i += 1
print(a) # 64
```

### 7.4 技巧和窍门

#### 7.4.1 “终极”规则

initialize var

while Boolean_Expression(var):

​    \# Here goes a statement or block of statements

​    Update/alter var

- initialize var*是任何将初始值赋值给变量var的语句，如：var=input()，或var=value
- Boolean_Expression(var)是任何从简单到复杂的布尔表达式，这取决于变量var
- Update/alter var是任何用于更改var值的语句，如：var=input()，或var=value以及复合赋值运算符的赋值语句。该语句必须在计算循环结构的布尔表达式之前？？？

```python
# example1
a = int(input()) # Initialization of a
while a > 0: # A Boolean expression dependent on a
    print(a)
    a -= 1 # Update/alteration of a

# example2
total = 0 # Initialization of total
while total < 1000: # A Boolean expression dependent on total
    b = int(input())
    total += b # Update/alteration of total
    
# example3
a = int(input()) # Initialization of a
b = int(input()) # Initialization of b
while a + b > 0: # A Boolean expression dependent on a and b
    print(a, b)
    a = int(input()) # Update/alteration of a
	b = int(input()) # Update/alteration of b
```

例1：

提示反复输入数字，输到5次结束。

```python
positives_given = 0 # Initialization of positives_given
while positives_given != 5: # A Boolean expression dependent on positives_given
    # Here goes a statements or block of statements
	a = float(input("Enter a number: "))
	if a > 0:
		positives_given += 1 # Update/alteration of positives_given
print("positives_given:", positives_given)
```

#### 7.4.2 跳出循环

```python
text = "I love Mum!"
letter = input("Enter a letter to search: ")

found = False
for a in text: # no break
	if a == letter:
		found = True
        break # 到这里程序会跳出循环
if found == True:
	print("Letter", letter, "found!")
```

#### 7.4.3 无限循环及如何避免

```python
i = 1
while i != 5:
	print("HI, Python!") # Ctrl + C for stop

i = 1
while i != 5:
	print("I love Mum!") # Ctrl + C for stop
	i += 2
```

```python
i = 1
while i < 5:
	print("I love Mum!")
	i += 2
```

>### 注意
>
>永远不要使用比较运算符==和!=检查计数器变量i，可以使用比较运算符<、<、=>和>=。它们保证当计数器变量超过终止值时执行流退出循环。

#### 7.4.4 “由内而外”法

该方法帮助你由内而外地学习“算法思维”：首先操作和设计内部（嵌套）结构，然后，随着程序的开发，添加越来越多的结构，嵌套前一个结构。

```python
i = 1
for j in range(1, 10):
	print(i, "x", j, "=", i * j, end = "\t")
```

```python
for i in range(1, 10):
    """Here goes the code that displays one single line of the multiplication table"""
	for j in range(1, 10):
		print(i, "x", j, "=", i * j, end = "\t")
	print()
```

#### 7.4.5 exercise

1.1+2+3+...+100

```python
s = 0
i = 1

s += i
i += 1

s += i
i += 1

...

s += i
i += 1

print(s)
```

```python
s = 0
i = 1

while i <= 100:
	s += i
	i += 1

print(s)
```

```python
s = 0
for i in range(1, 101):
	s += i

print(s)
```

2.2x4x6x8x10

```python
p = 1
for i in range(2, 12, 2):
	p *= i
print(p)
```

3.平均值

```python
total = 0
count = 0
for i in range(10):
	a = float(input("Enter a number: "))
	if a > 0:
		total += a
		count += 1

if count != 0:
	print(total / count)
else:
	print("No positives entered!")
```

4.10对数字，count for a>b and a<b

```python
count_a = 0
count_b = 0

for i in range(10):
	a = int(input("Enter number A: "))
	b = int(input("Enter number B: "))
	if a > b:
		count_a += 1
	elif b > a: # else: b>a,b=a
		count_b += 1

print(count_a, count_b)
```

5.1~999,count1 for 1-9,count2 for 10-99,count3 for 100-999

```python
count1 = 0
count2 = 0
count3 = 0
for i in range(20):
	a = float(input("Enter a number: "))
	if a <= 9:
		count1 += 1
	elif a <= 99:
		count2 += 1
	else:
		count3 += 1
print(count1, count2, count3)
```

6.反复输入数字，直到它们的总和>1000，count for numbers；因为不知道确切的迭代次数，所以不能用for结构。

```python
count = 0 # This is not here due to the Ultimate Rule!
total = 0 # Initialization of total
while total <= 1000: # A Boolean expression dependent on total
    # here goes a statement or block of statements
	a = float(input("Enter a number: "))
	count += 1
	total += a # Update/alteration of total
print(count)
```

7.迭代用户期望的次数：输入两个数字，a **= b，repeat?

```python
answer = "yes" # Initialization of answer
while answer.upper() == "YES":
    """Here goes the code that prompts the user to enter two numbers and then calculates and displays the first number raised to the power of the second one.下面是一段代码，提示用户输入两个数字，然后计算并显示第一个数字，并将其提升为第二个数字的幂。"""
	a = int(input("Enter number A: "))
	b = int(input("Enter number B: "))

	result = a ** b
	print("The result is:", result)
	
    # Update/alteration of answer
	answer = input("Would you like to repeat?")
```

8.寻找体重最小值，并显示。

```python
w = int(input("Enter a weight: "))
minimum = w
for i in range(3):
	w = int(input("Enter a weight: "))
	if w < minimum:
		minimum = w
print(minimum)
```

9.将0-100（温度增量值为0.5）华氏温度转换为开尔文温度。

```python
fahrenheit = 0
while fahrenheit <= 100:
	kelvin = (fahrenheit + 459.67) / 1.8
	print("Fahrenheit:", fahrenheit, "Kelvin:", kelvin)
	fahrenheit += 0.5
```

>### 提示
>
>for结构的range()函数仅支持整形增量值，所以这里只能用while结构。

10.棋盘上的大米共多少粒：国际象棋第一个格子1粒米，第二个格子2粒米，第三个格子4粒米，依此类推，每一个格子的米粒数量是前一个格子的两倍。

```python
grains = 1
total = 1
for i in range(63):
	grains *= 2
	total += grains
print(total) # 18446744073709551615
```

11.guess secret:1-100

```python
import random
secret_number = random.randrange(1, 101)
attempts = 1
guess = int(input("Enter a guess: ")) # Initialization of guess
while guess != secret_number:
    # Here goes the rest of the code
	if guess > secret_number:
		print("Your guess is bigger than my secret number.Try again.")
	else:
		print("Your guess is smaller than my secret number.Try again.")

	attempts += 1
	guess = int(input("Enter a guess: ")) # Update/alteration of guess

print("You get it!")
print("Attempts:", attempts)
```

## 第八章 海龟绘图

Python的一个功能，在一个窗口内一只虚拟海龟四处移动并绘制形状。

3个属性：位置、方向和笔。

### 8.1 x-y平面

### 8.2 begin

```python
import turtle # Import turtle module

wn = turtle.Screen() # Create a graphics window
george = turtle.Turtle() # Create a new turtle. Let's call it "george"
george.shape("turtle") # Change George to a real turtle

george.forward(50) # Move George forward by 50 pixels

wn.exitonclick() # Wait for a user click on the graphics window
```

```python
import turtle

a = int(input("Enter the length of the base: "))
b = int(input("Enter the length of the height: "))
wn = turtle.Screen()
george = turtle.Turtle()
george.shape("turtle")

george.forward(a)
george.left(90)
george.forward(b)
george.left(90)
george.forward(a)
george.left(90)
george.forward(b) # rect

wn.exitonclick()
```

```python
import turtle

wn = turtle.Screen()
george = turtle.Turtle()
george.shape("turtle")

george.forward(100)
george.setheading(270)
george.forward(100)
george.setheading(135)
george.forward(141) # 直角三角形

wn.exitonclick()
```

```python
import turtle

wn = turtle.Screen()
george = turtle.Turtle()
george.shape("turtle")
turtle.delay(50) # slowly to see draw

# Draw a triangle
george.forward(100)
george.left(120)
george.forward(100)
george.left(120)
george.forward(100)
george.left(120)

wn.exitonclick()
```

```python
import turtle

wn = turtle.Screen()
george = turtle.Turtle()
george.shape("turtle")

# Change pen's color to blue
george.color("blue")
george.forward(200)
george.left(90)
george.forward(100)
george.left(90)
george.forward(200)
george.left(90)
george.forward(100)

# Move George to the top left corner of the tectangle
george.penup() # Pull pen up
george.backward(100)
george.pendown() # Pull pen down

# Draw the red roof
george.setheading(45)
# george.left(135)
george.color("red")
george.forward(141)
george.right(90)
george.forward(141) # house

wn.exitonclick()
```

```python
george.goto(-100, 200)
george.goto(0, 0)
george.goto(-100, -200)
george.goto(0, 0)
george.goto(100, -200)
george.goto(0, 0)
george.goto(100, 200)
george.goto(0, 0) # x
```

### 8.3 for-draw

```python
for i in range(4):
	george.forward(50)
	george.left(90)
```

```python
for i in range(4):
	george.forward(50)
	george.left(90)

# Move the turtle to pole position
george.penup()
george.backward(200)
george.pendown()

# First square
for i in range(4):
	george.forward(50)
	george.left(90)

# Move the turtle to pole position
# where next square will be drawn
george.penup()
george.forward(100)
george.pendown()

# second square
for i in range(4):
	george.forward(50)
	george.left(90)

george.penup()
george.forward(100)
george.pendown()
```

```python
george.penup()
george.backward(200)
george.pendown()

for square in range(2):
	# Draw a square
	for i in range(4):
		george.forward(50)
		george.left(90)

	george.penup()
	george.forward(100)
	george.pendown()
```

#### exercise

1.three no same square

```python
george.penup()
george.backward(330)
george.pendown()

for multiplier in range(1, 4):
	# Draw a square
    # 50 100 150
	for i in range(4):
		george.forward(50 * multiplier)
		george.left(90)

	george.penup()
	george.forward(50 * multiplier)
	george.forward(30)
	george.pendown()
```

2.no same house

```python
george.penup()
george.backward(330)
george.pendown()

for multiplier in range(1, 4):
	# Draw a rectangle
	george.forward(100 * multiplier)
	george.left(90)
	george.forward(50 * multiplier)
	george.left(90)
	george.forward(100 * multiplier)
	george.left(90)
	george.forward(50 * multiplier)

	# Move George to the top left corner of the rectangle
	george.penup()
	george.backward(50 * multiplier)
	george.pendown()

	# Draw the roof
	george.setheading(45)
	george.forward(70.5 * multiplier)
	george.right(90)
	george.forward(70.5 * multiplier)

	# Move next
	george.penup()
	george.setheading(270) # 360-90=downward
	george.forward(50 * multiplier)
	george.setheading(0) # 0=forward
	george.forward(30)
	george.pendown()
```

3.duobianxing

```python
george.pensize(2)
sides = 5 # 6 7 8 ...
for i in range(sides):
	george.forward(100)
	george.right(360 / sides)
```

4.wujiao star

```python
george.pensize(3)
points = 5 # 7 9 ...
for i in range(points):
	george.forward(150)
	george.right(180 / points * (points -1))
```

5.random star

```python
import random
turtle.delay(0)
for star in range(10):
	a = random.randrange(-200, 200)
	b = random.randrange(-200, 200)
	george.penup()
	george.goto(a, b)
	george.pendown()

	points = random.randrange(5, 23, 2)

	length = random.randrange(10, 100)
	for i in range(points):
		george.forward(length)
		george.right(180 / points * (points - 1))
```

6.if star

```python
george.pensize(3)
flag = False
for x in range(18):
	george.forward(100)

	if flag == False:
		george.right(110)
	else:
		george.left(150)

    # This statement reverses flag from True to False and vice versa
    # 此语句将标志从True反转为False，反之亦然
	flag = not flag
```

## 第九章　Python中的数据结构

变量虽是存储值的好方法，但一次只能保存一个值。

假如要存储1000个名字？

```python
name1 = input("Enter a name: ")
name2 = input("Enter a name: ")
name3 = input("Enter a name: ")
# ...
print(name1)
print(name2)
print(name3)
# ...
```

Python中可用的数据结构：列表、元组、集合、不可变集合和字符串（字符串是含有字母数字字符的集合）。

### 9.1　列表

什么是列表？

- 在一个通用名称下保存多个值的数据结构，一组项的集合
- 每个项称为一个元素
- 每个元素都以唯一的数字进行标定，这个数字称为索引位置，简称索引
- 可变（可更改），元素的值可改（增删改）

设计一个数据结构保存4个人的年龄

第一种方式，直接赋值：age = [3, 4, 5, 6]

第二种方式：

```python 
ages = [None] * 4 # 四个空元素
k = 0
ages[k] = 3
ages[k + 1] = 4
ages[k + 2] = 5
ages[k + 3] = 6
```

第三种方式：

```python
ages = [] # 空的列表
# 在内存中不保留任何位置，只是表明ages已经准备好接收新元素
ages.append(3)
ages.append(4)
ages.append(5)
ages.append(6)
```

### 9.2　元组

什么是元组？

- 和列表的主要区别是元组不可变（不可更改），一旦被创建，其元素的值就不能改变

names = ("Mary", "Peter", "John")

ages = (12, 13, 14)

students = ("Mary", 12, "Peter", 13, "John", 14)

### 9.3 从列表或元组中取值

varname[Index]

- 0,1,2,3,...
- -1,-2,-3,...
- [2:10:2]
- [2:10:-2]

#### exercise

1.

```python
a = [None] * 3
a[2] = 9
b = 0
a[b] = a[2] + 4
a[b + 1] = a[0] + 5
print(a)
```

2.

```python
l = [1,2,3]
print(l[50]) #IndexError: list index out of range
```

### 9.4 alter the value of an existing element

```python
l = [1,2,3] # list
l[1] = 999
print(l)

l = (1,2,3) # tuple
l[1] = 999 #TypeError: 'tuple' object does not support item assignment
print(l)
```

### 9.5 遍历列表和元组

1.the first method: for index in range(size): process structure_name[index]

```python
l = [1,2,3]
for i in range(3):
	print(l[i])

for i in range(3):
	l[i] = l[i] * 2 # alter the value of the list's element
	print(l[i])
```

2.the second method: for element in structure_name: process element

```python
l = [1,2,3]
for i in l:
	print(i)

for i in l[::-1]:
	print(i)
"""
for i in l:
	i *= 2
	print(l[i]) # 3 + error
	# Don't alter the value of the list's element
"""
```

#### exercise

1.sum

the first method:

```python
n = (1,2,3)
total = 0
for i in range(3):
	total += n[i]
print(total)
```

the second method:

```python
for i in n:
	total += i
print(total)
```

the third method:

```python
import math
total = math.fsum(n)
print(total)
```

2.nixu words

```python
# the first method
n = [None] * 20
for i in range(20):
	n[i] = input()
for i in range(19, -1, -1):
	print(n[i])

# the second method 
n = []
for i in range(3):
	n.append(input())
for j in n[::-1]:
	print(j)
```

3.nixu zheng numbers

```python
ELEMENTS = 50
values = []
for i in range(ELEMENTS):
	values.append(float(input()))

for value in values[::-1]:
	if value > 0:
		print(value)
```

4.sum

```python
# the first method
ELEMENTS = 50
values = [None] * ELEMENTS
for i in range(ELEMENTS):
	values[i] = float(input("Enter a value: ")) # 1
total = 0
for i in range(ELEMENTS):
	total += values[i] # 2
print(total)

# the second method
ELEMENTS = 50
values = [None] * ELEMENTS
total = 0
for i in range(ELEMENTS):
	values[i] = float(input("Enter a value: ")) # 1
	total += values[i] # 2
print(total)

# the third method
import math
ELEMENTS = 50
values = []
for i in range(ELEMENTS):
	values.append(float(input("Enter a value: ")))
total = math.fsum(values)
print(total)
```

5.average

```python
# the first method
ELEMENTS = 30
values = []
for i in range(ELEMENTS):
	values.append(float(input("Enter a value: ")))
total = 0
for i in range(ELEMENTS):
	total += values[i]
average = total / ELEMENTS
if average < 10:
	print("Average value is less than 10")
  
# the second method
import math
ELEMENTS = 30
values = []
for i in range(ELEMENTS):
	values.append(float(input("Enter a value: ")))
if math.fsum(values) / ELEMENTS < 10:
	print("Average value is less than 10")
```

6.element!=int(element)，判断实数，并显示实数索引

```python
ELEMENTS = 10
a = []
for i in range(ELEMENTS):
	a.append(float(input("Enter a value for element " + str(i) + ": ")))
for i in range(ELEMENTS):
	if a[i] != int(a[i]):
		print("A real found at index:", i)
```

7.显示奇数索引的元素

```python
# the first method
ELEMENTS = 10
values = []
for i in range(ELEMENTS):
	values.append(float(input("Enter a value for element " + str(i) + \
		": ")))
for i in range(1, ELEMENTS, 2):
	print(values[i])
  
# the second method
ELEMENTS = 10
values = []
for i in range(ELEMENTS):
	values.append(float(input("Enter a value for element " + str(i) + \
		": ")))
for i in values[1:ELEMENTS:2]:
	print(i)
```

### 9.6　字典

什么是字典？

- 字典与列表或元组之间的主要区别是字典元素使用键进行唯一标识
- 键不一定是整数值
- 每个键都与一个元素相关联（或映射）
- 键必须是不可变的数据类型（如字符串、整数、浮点数或元组）
- 在字典中键是唯一的，不能存在两个一样的键

创建字典：

第一种方法：

dict_name = {key0: value0, key1: value1, key2: value2,...,keyN: valueN}

如：stuedent = {"first_name": "Ann", "last_name": "Fox", "age": 15, "class": "3rd"}

第二种方法：

dict_name = {}

dict_name[key0] = value1
dict_name[key1] = value2
dict_name[key2] = value3
...
dict_name[keyN] = valueN

student["first_name"] = "Ann"

student["last_name"] = "Fox"

student["age"] = 15

student["class"] = "3rd"

### 9.7 从字典中取值

print("Ann Fox at ", student["class"], " class.")

print(student["weight"]) # error

### 9.8 alter the value of the element of dictionary

student["age"] = 16

```python
dict = {0: "a", 1: "b", 2: "c"}
dict[3] = "d"
print(dict)
```

### 9.9 遍历字典

```python
# the first method
"""
for key in structure_name:
	process structure_name[key]
"""
stuedent = {"first_name": "Ann", "last_name": "Fox", \
			"age": 15, "class": "3rd"}
for item in stuedent:
	print(item, stuedent[item])

# salaries
salaries = {"a": 5000, \
			"b": 6000, \
			"c": 7000, \
			"d": 8000}
for title in salaries:
	salaries[title] += 2000 # alter the value
	print(title, salaries[title])
# print(salaries)
# {'a': 7000, 'b': 8000, 'c': 9000, 'd': 10000}

# the second method
"""
for key, value in structure_name.items():
	process key, value
"""
grades = {"a": "A+", "b": "B+", "c": "C+", "d": "D+"}
for item, grade in grades.items():
	print(item, grade)

salaries = {"a": 5000, \
			"b": 6000, \
			"c": 7000, \
			"d": 8000}
for title, salary in salaries.items():
	salary += 2000  # no alter the value
	print(title, salary)
# print(salaries)
# {'a': 5000, 'b': 6000, 'c': 7000, 'd': 8000}
```

### 9.10 del len max/min sort

list del

```python
l = [1,2,3,4,5]
print(l[1])
del l[1]
print(l)
print(l[1])

del l[1:3]
print(l)

del l[:]
print(l)
```

dict del

```python
grades = {"a": "A+", "b": "B+", "c": "C+", "d": "D+"}
del grades["b"]
print(grades)
```

len(structure_name)

```python
print(len(l))

length = len(l[2:4])
print(length)

for i in range(len(l)):
	print(l[i], end = " ")
```

max/min(structure_name)

```python
print(max(l))

maximum = max(l[1:3])
print(maximum)

w = ("a", "b", "c")
print(max(w))
```

sort/sorted()

list_name.sort([reverse = True])

```python
l = [3,4,9,2,6,7]
# l.sort()
l.sort(reverse = True)
print(l)

# sorted()返回一个新的排序列表或元组，保持初始结构不变
l2 = sorted(l)
print(l)
print(l2)

l2 = sorted(l, reverse = True)
for element in l2:
	print(element, end = " ")

for element in sorted(l):
	print(element, end = " ")
```

### exercise

1.创建包含最大值的列表

用户各输入20个数值到a和b两个列表，再创建一个新列表：元素为a和b两个列表相应位置上最大值。

```python
ELEMENTS = 3
a = [None] * ELEMENTS
b = [None] * ELEMENTS

for i in range(ELEMENTS):
	a[i] = float(input("Enter a number A:"))

for i in range(ELEMENTS):
	b[i] = float(input("Enter a number B:"))

new_list = [None] * ELEMENTS
for i in range(ELEMENTS):
	if a[i] > b[i]:
		new_list[i] = a[i]
	else:
		new_list[i] = b[i]

for element in new_list:
	print(element)
```

2.哪天可能会下雪？

输入1月份31天中每天中午12:00记录的温度（华氏），显示可能会下雪的日期（低于36度）。

```python
DAYS = 31
t = [None] * DAYS
for i in range(DAYS):
	t[i] = int(input("Enter the temp: "))
for i in range(DAYS):
	if t[i] < 36:
		print(i + 1, end = "\t")
```

3.有没有可能下雪？

输入1月份31天中每天中午12:00记录的温度（华氏），是否有哪一天低于36度。

for i in range(DAYS):
	if t[i] < 36:
		print("There was a possibility of snow in January!")

这样的话，低于36度有几天就会显示几次这条消息。

第一种方法：计数低于36度的天数，如果不为0，则显示消息。

```python
count = 0
for i in range(DAYS):
	if t[i] < 36:
		count += 1

if count > 0:
	print("There was a possibility of snow in January!")
```

第二种方法：使用信号旗（标识），当信号旗被升起来（Flag＝True），就永远不会再降下来。

```python
flag = False
for i in range(DAYS):
	if t[i] < 36:
		flag = True

if flag == True:
	print("There was a possibility of snow in January!")
```

### 9.11 多个数据结构

#### 1.计算平均值

输入20名学生姓名和3门功课成绩，显示3门成绩平均值超过89分的学生姓名。

```python
STUDENTS = 20
names = [None] * STUDENTS
grades_lesson1 = [None] * STUDENTS
grades_lesson2 = [None] * STUDENTS
grades_lesson3 = [None] * STUDENTS

for i in range(STUDENTS):
	names[i] = input("Enter student name No" + str(i + 1) + ": ")
	grades_lesson1[i] = int(input("Enter grade for lesson 1: "))
	grades_lesson2[i] = int(input("Enter grade for lesson 2: "))
	grades_lesson3[i] = int(input("Enter grade for lesson 3: "))

for i in range(STUDENTS):
	total = grades_lesson1[i] + grades_lesson2[i] + grades_lesson3[i]
	average = total / 3.0
	if average > 89:
		print(names[i])
```

#### 2.同时使用列表和字典

输入30名学生成绩等级，根据下表显示每名学生成绩等级对应的百分范围。

| 等级 | 分值    |
| ---- | ------- |
| A    | 90～100 |
| B    | 80～89  |
| C    | 70～79  |
| D    | 60～69  |
| E/F  | 0～59   |

```python
STUDENTS = 30
grades_table = {"A": "90-100", "B": "80-89", "C": "70-79", \
				"D": "60-69", "E": "0-59", "F": "0-59"}
names = [None] * STUDENTS
grades = [None] * STUDENTS

for i in range(STUDENTS):
	names[i] = input("Enter student name No" + str(i + 1) + ": ")
	grades[i] = input("Enter his or her grade: ")

for i in range(STUDENTS):
	# grade = grades[i]
	# grade_as_percentage = grades_table[grade]

	# print(names[i], grade_as_percentage)
	print(names[i], grades_table[grades[i]]) # Ok
```

#### 3.查找列表中的最大值和最小值

3.1显示20个湖泊最深的深度。

```python
LAKES = 20
depths = [None] * LAKES
for i in range(LAKES):
	depths[i] = float(input("Enter depth of lake: "))

# maximum = depths[0]
# for i in range(1, LAKES):
# 	if depths[i] > maximum:
# 		maximum = depths[i]

maximum = max(depths) # Ok
print(maximum)
```

3.2 哪个湖泊最深？这里不能用max()

```python
LAKES = 20
names = [None] * LAKES
depths = [None] * LAKES

for i in range(LAKES):
	names[i] = input("Enter lake name: ")
	depths[i] = float(input("Enter depth of lake: "))

maximum = depths[0]
m_name = names[0]
for i in range(1, LAKES):
	if depths[i] > maximum:
		maximum = depths[i]
		m_name = names[i]

print(m_name)
```

3.3哪个湖泊最深？显示最深湖泊的所有信息：深度、名字、所属国和面积。

```python
# the first method
LAKES = 3
names = [None] * LAKES
depths = [None] * LAKES
countries = [None] * LAKES
areas = [None] * LAKES

for i in range(LAKES):
	names[i] = input("Enter lake name: ")
	depths[i] = float(input("Enter depth of lake: "))
	countries[i] = input("Enter country name: ")
	areas[i] = float(input("Enter area of lake: "))

maximum = depths[0]
m_name = names[0]
m_country = countries[0]
m_area = areas[0]
for i in range(1, LAKES):
	if depths[i] > maximum:
		maximum = depths[i]
		m_name = names[i]
		m_country = countries[i]
		m_area = areas[i]

print(maximum, m_name, m_country, m_area)

# the second method
maximum = depths[0]
# m_name = names[0]
# m_country = countries[0]
# m_area = areas[0]
index_of_max = 0
for i in range(1, LAKES):
	if depths[i] > maximum:
		maximum = depths[i]
		# m_name = names[i]
		# m_country = countries[i]
		# m_area = areas[i]
		index_of_max = i

# print(maximum, m_name, m_country, m_area)
print(depths[index_of_max], names[index_of_max], \
	countries[index_of_max], areas[index_of_max])
```

3.4.the shortest students

```python
STUDENTS = 100
names = [None] * STUDENTS
heights = [None] * STUDENTS
	
for i in range(STUDENTS):
	names[i] = input("Enter name for student No " + \
					str(i + 1) + ": ")
	heights[i] = float(input("Enter his or her heights: "))

minimum = min(heights) # Ok

print("The following students have got the shortest height:")
for i in range(STUDENTS):
	if heights[i] == minimum: # == min(heights): No
		print(names[i])
```

### 9.12 在数据结构中查找元素

#### 1.在可能包含多个相同值的列表中查找

```
# 公式：
needle = float(input("Enter a value to search: "))
found = False
for i in range(ELEMENTS):
	if haystack[i] == needle:
		print(needle, "found at position:", i)
		found = True
if found == False:
	print("nothing found!")
```

1.1显示所有相同名字的姓氏

```python
PEOPLE = 100
first_name = [None] * PEOPLE
last_name = [None] * PEOPLE

for i in range(PEOPLE):
	first_name[i] = input("Enter first name: ")
	last_name[i] = input("Enter last name: ")

needle = input("Enter a first name to search: ")

found = False
for i in range(PEOPLE):
	if first_name[i] == needle:
		print(last_name[i])
		found = True
if found == False:
	print("No one found!")
```

#### 2.在包含唯一值的数据结构中进行查找

```
# 公式：
needle = float(input("Enter a value to search: "))
found = False
for i in range(ELEMENTS):
	if haystack[i] == needle:
		print(needle, "found at position:", i)
		found = True
		break
		
if found == False:
	print("nothing found!")
```

2.1查找给定的社会安全号码（SSN）

在美国，SSN：一个9位数的身份号码用于社会保障。该程序基于SSN查找并显示相应的名字和姓氏。

```python
PEOPLE = 100
SSNs = [None] * PEOPLE
first_name = [None] * PEOPLE
last_name = [None] * PEOPLE

for i in range(PEOPLE):
	SSNs[i] = input("Enter SSN: ")
	first_name[i] = input("Enter first name: ")
	last_name[i] = input("Enter last name: ")

needle = input("Enter an SSN to search: ")

found = False
for i in range(PEOPLE):
	if SSNs[i] == needle:
		print(first_name[i], last_name[i])
		found = True
		break

if found == False:
	print("Nothing found!")
```

## 第十章　函数

### 10.1 什么是函数？

```
def get_sum(num1, num2):
	result = num1 + num2
	return result

def get_sum(num1, num2):
	return num1 + num2

def get_sum_dif(num1, num2):
	s = num1 + num2
	d = num1 - num2
	return s, d
```



### 10.2　调用函数

```python
def cube(num):
	result = num ** 3
	return result

x = float(input("Num: "))
 # the 1st
cb = cube(x)
y = cb + 1 / x
print(y)
# the 2nd
y = cube(x) + 1 / x
print(y)
# the 3rd
print(cube(x) + 1 / x)
```

```python
def get_msg():
	msg = "How do you do?"
	return msg

print("Nice to meet you!")
a = get_msg()
print(a)
```

```python
def display(color):
	msg = "There is " + color + " in the rainbow"
	return msg
print(display("red"))
print(display("yellow"))
print(display("blue"))
```

```python
def display(color, exists):
	neg = ""
	if exists == False:
		neg = "n't any"
	return "There is" + neg + " " + color + " in the rainbow"

print(display("red", True))
print(display("yellow", True))
print(display("black", False))
```

```python
def get_fullname():
	first_name = input("Enter first name: ")
	last_name = input("Enter last name: ")
	return first_name, last_name

fname, lname = get_fullname()
print("First name:", fname)
print("Last name:", lname)
```

### 10.3 no return

```
def display_sum(num1, num2):
	result = num1 + num2
	print(result)
```

### 10.4 use the no return

```python
def display_line():
	print("----------------------------")
print("Hello Python!")
display_line()
print("Nice to study you!")
display_line()
print("Would you like Coffow?")
display_line()
```

```python
def display_line(length):
	for i in range(length):
		print("-", end = "")
	print()

print("Hello Python!")
display_line(15)
print("Nice to study you!")
display_line(18)
print("Would you like Coffow?")
display_line(22)
```

>### 切记：
>
>没有返回值的函数，不能直接赋给变量：a = display_line(15)；
>
>也不能在语句中调用它：print(display_line(15))。

### 10.5　形参和实参

- 函数包含的参数叫形参
- 调用函数时传递给函数的参数叫实参
- 两者之间是一对一的匹配关系

```python
def divide(n1, n2):
	result = n1 / n2
	return result

x = float(input("Enter a number 1: "))
y = float(input("Enter a number 2: "))

w = divide(x, y)

print(w)
```

### 10.6　函数如何运行，即调用函数的步骤

1.主代码中语句的执行被中断

2.实参列表中变量的值或表达式的结果被传递（赋值）给形参列表中对应的形参（变量），同时执行流转向函数定义所在的位置

3.执行函数中语句

4.当执行流到达函数的末尾时：

- 将返回值从函数返回到主代码，执行流从调用该函数之前的地方继续执行
- 无返回值时，执行流只需从调用该函数之前的地方继续执行

```python
def maximum(n1, n2):
	m = n1
	if n2 > m:
		m = n2
	return m
a = float(input("Enter number1: "))
b = float(input("Enter number2: "))

c = maximum(a, b)
print(c)
```

### 10.7 sameVarName

```python
def f1():
	sameVarName = 1
	print(sameVarName)
def f2(sameVarName):
	print(sameVarName)
sameVarName = 3
print(sameVarName)
f1()
f2(2)
print(sameVarName)
```

```python
def f1(test):
	test += 1
	print(test)

test = 5
f1(test)
print(test)
```

>### 注意
>
>函数中变量只在被调用时才会创建，当被调用完，这些变量就会被清除。

### 10.8 函数调用函数

```python
def add(n1, n2):
	result = n1 + n2
	return result

def display_sum(n1, n2):
	print(add(n1, n2))

a = int(input("Enter number1: "))
b = int(input("Enter number2: "))

display_sum(a, b)
```

>### 提示
>
>函数编写顺序没有限制，display_sum()在add()之前是可以的。

### 10.9　默认参数值和关键字参数

形参使用默认值，即没有传递任何值给形参。

```python
def prepend_title(name, title = "Mr"):
	return title + " " + name
print(prepend_title("zhangsan"))
print(prepend_title("liping", "Ms"))
```

>### 提示
>
>默认值即“可选参数”，必须写在不可选参数的右侧。

```python
def prepend_title(first_name, last_name, title = "Mr", reverse = False):
	if reverse == False:
		return title + " " + first_name + " " + last_name
	else:
		return title + " " + last_name + " " + first_name
print(prepend_title("John", "King"))
print(prepend_title("Maria", "Myles", "Ms"))
print(prepend_title("Maria", "Myles", "Ms", True))
print(prepend_title("John", "King", reverse = True))
```

### 10.10 变量的作用域

- 变量的作用域指该变量的作用范围
- 在Python中，变量有局部（函数中的变量）或全局作用域（函数外的变量）
- 局部变量只能在函数中使用；全局变量可以在函数内和函数外的主代码中使用

```python
def display_val():
	print(test)

test = 8
display_val() # 8
print(test) # 8

# 内存中已经声明了全局变量test和局部变量test
def display_val():
	test = 9
	print(test)

test = 8
display_val() # 9
print(test) # 8
```

```python
def display_val():
	print(test)
	#UnboundLocalError: local variable 'test' referenced before assignment
	test = 9
	print(test)

test = 8
display_val()
print(test)
```

```python
def display_val():
	global test
	print(test) # 8
	test = 9
	print(test)

test = 8
display_val() # 9
print(test) # 9
```

>### 提示
>
>一个全局变量的值在函数内被改变，函数外的同名变量值也改变。

```python
def display_val():
	a = 8
	b = 3
	print(a, b)

def display_other_val():
	b = 2
	print(a, b)

a = 15
print(a)
display_val()
display_other_val()
print(a)
```

### exercise

1.sum

```python
def total(a, b):
	# s = a + b
	return a + b
n1 = float(input("Enter number1: "))
n2 = float(input("Enter number2: "))

# result = total(n1, n2)
print("The sum of", n1, "+", n2, "is", total(n1, n2))
```

2.简单的货币转换器

```python
def display_menu():
	print("1. Convert USD to EUR")
	print("2. Convert EUR to USD")
	print("3. Exit")
	print("-----------------------")
	print("Enter a choice: ", end = "")

while True:
	display_menu()
	choice = int(input())

	if choice == 3:
		print("Bye!")
		break
	else:
		amount = float(input("Enter an amount: "))
		if choice == 1:
			print(amount, "USD = ", amount * 0.94, "EUR")
		else:
			print(amount, "EUR = ", amount / 0.94, "USD")
```

3.较完整的货币转换器

```python
def display_menu():
	print("1. Convert USD to EUR")
	print("2. Convert USD to GBP")
	print("3. Convert USD to JPY")
	print("4. Convert USD to CAD")
	print("5. Exit")
	print("-----------------------")
	print("Enter a choice: ", end = "")

def USD_to_EUR(value):
	return value * 0.94
def USD_to_GBP(value):
	return value * 0.79
def USD_to_JPY(value):
	return value * 113
def USD_to_CAD(value):
	return value * 1.33

while True:
	display_menu()
	choice = int(input())

	if choice == 5:
		print("Bye!")
		break
	else:
		amount = float(input("Enter an amount in US dollars: "))
		if choice == 1:
			print(amount, "USD = ", USD_to_EUR(amount), "EUR")
		elif choice == 2:
			print(amount, "USD = ", USD_to_GBP(amount), "GBP")
		elif choice == 3:
			print(amount, "USD = ", USD_to_JPY(amount), "JPY")
		elif choice == 4:
			print(amount, "USD = ", USD_to_CAD(amount), "CAD")
```

4.求正整数的平均值

```python
def tst_int(n):
	if n == int(n):
		return True
	else:
		return False

total = 0
count = 0
a = float(input("Enter a number: "))
while tst_int(a) == True: # 如果函数返回False，退出循环
	if a > 0:
		total += a
		count += 1
	a = float(input("Enter a number: "))
if count > 0:
	print(total / count)
```

>### 提示
>
>注意if count > 0，如果一开始就输入了一个实数，count则为0，0不能作为除数，所以这样就避免了除零错误。

5.掷骰子：

- dice函数：返回1－6的随机整数
- search_and_count函数：接收一个整数和一个列表，并返回该整数在列表中的次数
- 使用100个随机整数（1－6）填充一个列表，用户输入一个整数（1－6）
- 显示用户给的整数在列表中存在多少次

```python
import random
ELEMENTS = 100
def dice():
	return random.randrange(1, 7)

def search_and_count(x, a):
	count = 0
	for i in range(ELEMENTS):
		if a[i] == x:
			count += 1
	return count

a = [None] * ELEMENTS

for i in range(ELEMENTS):
	a[i] = dice()

x = int(input("Enter a number 1-6: "))
print("Given value exists in the list")
print(search_and_count(x, a), "times")

```

## 第十一章　面向对象编程

### 11.1　什么是面向对象编程，OOP

- 一种聚焦于对象的编程风格
- 将数据和功能组合在一起，并将它们包围在称为对象的东西内
- 轻松维护代码，他人轻松使用

OOP聚焦于对象：用一辆汽车举例

- 属性：品牌、型号、颜色和车牌等等
- 动作：启动或熄火、加速或刹车或停车等等

在OOP中，这辆车就是一个对象，它具有特定属性（字段），执行特定动作（方法）。

那如何创建一个对象呢？

- 只需一个汽车的类，就象一枚图章
- 用这枚图章印出许多汽车，然后给它们涂上颜色，并用特定的属性填充每辆车的字段
- 创建一个新对象（类的实例）的过程称为“实例化”
- 类是一个模板，每个对象都是根据类创建的。每个类只执行一个任务，所以在构建整个应用程序时不止使用一个类

### 11.2　Python中的类和对象

```python 
class Car:
	# define four fields
	brand = ""
	model = ""
	color = ""
	license_plate = ""

	# define method turn_on
	def turn_on(self):
		print("The car turns on")

	# define method turn_off
	def turn_off(self):
		print("The car turns off")

	# define method accelerate
	def accelerate(self):
		print("The car accelerate")

# 实例化，创建汽车对象car1，car2
car1 = Car()
car2 = Car()

# 对象名称.字段或方法名称＝"值"
car1.brand = "Linken"
car1.model = "6"
car1.color = "red"
car1.license_plate = "CD7834"

car2.brand = "Hongqi"
car2.model = "Focus"
car2.color = "black"
car2.license_plate = "JK803"

print(car1.brand)
print(car2.brand)

# 调用对象的方法
car1.turn_on()
car2.accelerate()
```

### 11.3　构造方法和关键字self

\_\_init\_\_：构造方法

- Python中有一个具有特殊角色的方法
- 在创建对象时自动执行
- 在这个方法内可以完成任何的对象初始化操作

```python 
class Person:
	def __init__(self):
		print("An object was created")

p1 = Person()
p2 = Person()
```

self：关键字self是对一个对象本身的引用

```python
class Person:
	name = None
	age = None

	def say_info(self):
		print("I am ", self.name)
		print("I am ", self.age, "years old")

# Main code starts here
p1 = Person()
p1.name = "zhangsan"
p1.age = 9
p1.say_info() # call the method say_info() of the object p1

p2 = Person()
p2.name = "lisi"
p2.age = 10
p2.say_info() # call the method say_info() of the object p1
```

>### 提示
>
>self可以换成其它名称，但self是Python的一种约定俗成。

问题：为什么要在方法say_info()中以self.name和self.age的方式引用name和age呢？真的有必要用self关键字吗？

简单的答案：在方法中可能有两个额外的同名的（name和age）局部变量。因此需要一种方法来区分这些局部变量和对象的字段。

如果您还感到困惑，看下面的例子：

```python
class MyClass:
	b = None # this is a field

	def myMethod(self):
		b = "***" # this is a local variable
		print(b, self.b, b)

x = MyClass()
x.b = "Hello"
x.myMethod()
```

### 11.4 将初始值传递给构造方法

对象创建过程中可用构造方法的形参将初始值传递给构造方法。

```python
class hhh:
	name = None
	gender = None

	def __init__(self, n, g):
		self.name = n
		self.gender = g

hhh1 = hhh("abc", "male")
hhh2 = hhh("bcd", "male")
hhh3 = hhh("cde", "female")
hhh4 = hhh("def", "female")
```

>### 提示
>
>即使在构造方法中有三个形参，在调用构造方法的语句中也只有两个实参。这是Python的特点“多做、少写”，不需要传递对象本身。

在Python中，一个字段和一个局部变量（甚至一个方法参数）具有相同的名称是合法的。

```python
class hhh:
  # name和gender用于将值传递给构造方法的参数
	name = None
	gender = None
	def __init__(self, name, gender):
		# fields and arguments can have the same name
    # self.name和self.gender是用于在对象内存储值的字段
		self.name = name
		self.gender = gender

# 可以简写
class hhh:
	def __init__(self, name, gender):
		self.name = name
		self.gender = gender

hhh1 = hhh("abc", "male")
hhh2 = hhh("bcd", "male")
hhh3 = hhh("cde", "female")
hhh4 = hhh("def", "female")

print(hhh1.name, "-", hhh1.gender)
print(hhh2.name, "-", hhh2.gender)
print(hhh3.name, "-", hhh3.gender)
print(hhh4.name, "-", hhh4.gender)
```

### 11.5 类变量和实例变量

在构造方法之外声明字段是可以的。

```python
class HistoryEvents:
	day = None # this field is declared outside of the constructor
	           # It is called "class field"
	def __init__(self):
		print("object Instantiation")

h1 = HistoryEvents()
h1.day = "3rd of July"

h2 = HistoryEvents()
h2.day = "12th of October"

print(h1.day)
print(h2.day)
```

也可以在构造方法中声明该字段。

```python
class HistoryEvents:
	def __init__(self, day):
		print("object Instantiation")
		self.day = day # this field is declared inside the constructor
		               # It is called "instance field"

h1 = HistoryEvents("3rd of July")
h2 = HistoryEvents("12th of October")

print(h1.day)
print(h2.day)
```

>### 提示
>
>在构造方法外部声明的字段叫“类字段”；在构造方法内部声明的字段叫“实例字段”。

哪种编程风格更好？第二种！

- 编写类的正确方法
- 在某些情况下，当可变数据类型（如列表和字典）用作类字段时，可能会导致“不良结果”

```python 
class HistoryEvents:
	events = [] # class field shared by all instances

	def __init__(self, day):
		self.day = day # Instance field unique to each instance

h1 = HistoryEvents("3rd of July")
h1.events.append("3421: Declaration of Independence in United States")
h1.events.append("7899: French troops occupy Amsterdam")

h2 = HistoryEvents("12th of October")
h2.events.append("789: Byzantine troops occupy Antioch")
h2.events.append("324: Ohi Day in Greece")

print(h1.events) # 把四个事件都输出了
```

- 中Python中，永远不要将可变数据类型用作类字段
- 一般来说，必须尽可能少地使用类字段，类字段越少越好

```python
class HistoryEvents:
	def __init__(self, day):
		self.day = day   # Instance field unique to each instance
		self.events = [] # Instance field unique to each instance

h1 = HistoryEvents("3rd of July")
h1.events.append("3421: Declaration of Independence in United States")
h1.events.append("7899: French troops occupy Amsterdam")

h2 = HistoryEvents("12th of October")
h2.events.append("789: Byzantine troops occupy Antioch")
h2.events.append("324: Ohi Day in Greece")

# print(h1.events)
print(h2.events)
```

### 11.6 Getter、Setter方法与属性

- 字段是直接在类中声明的变量
- 面向对象编程的准则宣称一个类的数据应该被隐藏起来防止被意外地更改
- 当你编写给其他程序员使用的类，你并不想让他们知道类里有什么！类的内部操作应该对外界隐藏
- 通过不暴露字段，可以隐藏类的内部实现
- 字段应该保持类的私有性，外界通过get和set方法访问它们

```python
class FahrenheitToCelsius:
	def __init__(self, value):
		self.temperature = value

	def get_temperature(self):
		return 5.0 / 9.0 * (self.temperature - 32.0)

x = FahrenheitToCelsius(-500)
print(x.get_temperature())
```

这个类几乎是完美的，但有一个漏点：它没有考虑到温度不能低于－459.67华氏度（即－273.15摄氏度，绝对零度）。因此，对物理学一无所知的新手程序员可能就会将－500华氏度的值传递给构造方法。

这个类的一个稍微不同的版本可以部分地解决该问题。

```python 
class FahrenheitToCelsius:
	def __init__(self, value):
		self.set_temperature(value)

	def get_temperature(self):
		return 5.0 / 9.0 * (self.temperature - 32.0)

	def set_temperature(self, value):
		if value >= -459.67:
			self.temperature = value
		else:
			raise ValueError("There is no temperature below -459.67")

x = FahrenheitToCelsius(-50)
print(x.get_temperature())
```

这一次使用set_temperature()方法设置字段temperature的值。虽好一些，但还是有问题：

- 程序员必须小心谨慎，每当要更改字段temperature的值时都要记得使用set_temperature()方法
- 问题在于字段temperature的值仍然可通过其名称直接更改

```python
class FahrenheitToCelsius:
	def __init__(self, value):
		self.set_temperature(value)

	def get_temperature(self):
		return 5.0 / 9.0 * (self.temperature - 32.0)

	def set_temperature(self, value):
		if value >= -459.67:
			self.temperature = value
		else:
			raise ValueError("There is no temperature below -459.67")

x = FahrenheitToCelsius(-50)
print(x.get_temperature())

# x.set_temperature(-50)
# print(x.get_temperature())

x.temperature = -500 # 这里直接更改
print(x.get_temperature())
```

这个时候就应该使用属性！

- 属性是一个类成员，它为读取、写入或计算我们要保持私有的字段的值提供了一种灵活的机制
- 属性提供了对字段的公开访问，同时隐藏其内部实现

```python
class FahrenheitToCelsius:
	def __init__(self, value):
		self.set_temperature(value)

	def get_temperature(self):
		return 5.0 / 9 * (self._temperature - 32)

	def set_temperature(self, value):
		if value >= -459.67:
			self._temperature = value
		else:
			raise ValueError("There is no temperature below -459.67")

# define a property
temperature = property(get_temperature, set_temperature)
# NameError: name 'get_temperature' is not defined
# 一直弄不懂这里，为什么一直显示上面这句错误

# main code starts here
x = FahrenheitToCelsius(-50)

print(x.temperature)
x.temperature = -500
print(x.temperature)
```

语句temperature = property(get_temperature, set_temperature)的作用：

- 当一条语句尝试访问属性temperature的值时，将自动调用get_temperature()方法
- 当语句尝试将值赋给属性temperature时，将自动调用set_temperature()方法

所以，现在一切都Ok了？不，还有更好的！！！

```python 
class FahrenheitToCelsius:
	def __init__(self, value):
		self.temperature = value # 第三：=value no (value)

	@property
	def temperature(self):
		return 5.0 / 9 * (self._temperature - 32)
		# 第一：9 no 9.0 第二：_tem no tem　第五：32 no 32.0

	@temperature.setter
	def temperature(self, value):
		if value >= -459.67:
			self._temperature = value
		else:
			raise ValueError("There is no temperature below -459.67")

# main code starts here
x = FahrenheitToCelsius(-50)

# print(x.temperature)

# x.temperature = -60
# print(x.temperature)

x.temperature = -500
print(x.temperature)
```

