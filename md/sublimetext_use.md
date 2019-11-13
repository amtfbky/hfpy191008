# 选择类

- Ctrl+D 选中光标所占的文本，继续操作则会选中下一个相同的文本。
- Alt+F3 (Mac的Alt不好使，未找到答案)选中文本按下快捷键，即可一次性选择全部的相同文本进行同时编辑。举个栗子：快速选中并更改所有相同的变量名、函数名等。
- Ctrl+L 选中整行，继续操作则继续选择下一行，效果和 Shift+↓ 效果一样。
- Ctrl+Shift+L 先选中多行(**但不要全选上**)，再按下快捷键，会在每行行尾插入光标，即可同时编辑这些行。
- Ctrl+Shift+M 选择括号内的内容（继续选择父括号）。举个栗子：快速选中删除函数中的代码，重写函数体代码或重写括号内里的内容。
- Ctrl+M 光标移动至括号内结束或开始的位置。
- Ctrl+Enter 在下一行插入新行。举个栗子：即使光标不在行尾，也能快速向下插入一行。
- Ctrl+Shift+Enter 在上一行插入新行。举个栗子：即使光标不在行首，也能快速向上插入一行。
- Ctrl+Shift+[ 选中代码，按下快捷键，折叠代码。
- Ctrl+Shift+] 选中代码，按下快捷键，展开代码。
- Ctrl+K+0 展开所有折叠代码。
- Ctrl+← 向左单位性地移动光标，快速移动光标。
- Ctrl+→ 向右单位性地移动光标，快速移动光标。
- shift+↑ 向上选中多行。
- shift+↓ 向下选中多行。
- Shift+← 向左选中文本。
- Shift+→ 向右选中文本。
- Ctrl+Shift+← 向左单位性地选中文本。
- Ctrl+Shift+→ 向右单位性地选中文本。
- Ctrl+Shift+↑ 将光标所在行和上一行代码互换（将光标所在行插入到上一行之前）。
- Ctrl+Shift+↓ 将光标所在行和下一行代码互换（将光标所在行插入到下一行之后）。
- Ctrl+Alt+↑ 向上添加多行光标，可同时编辑多行。
- Ctrl+Alt+↓ 向下添加多行光标，可同时编辑多行。

 

# 编辑类

 

- Ctrl+J 合并选中的多行代码为一行。举个栗子：将多行格式的CSS属性合并为一行。
- Ctrl+Shift+D 复制光标所在整行，插入到下一行。
- Tab 向右缩进。
- Shift+Tab 向左缩进。
- Ctrl+K+K 从光标处开始删除代码至行尾。
- Ctrl+Shift+K 删除整行。
- Ctrl+/ 注释单行。
- Ctrl+Shift+/ 注释多行。
- Ctrl+K+U 转换大写。
- Ctrl+K+L 转换小写。
- Ctrl+Z 撤销。
- Ctrl+Y 恢复撤销。
- Ctrl+U 软撤销，感觉和 Gtrl+Z 一样。
- Ctrl+F2 设置书签
- Ctrl+T 左右字母互换。
- F6 单词检测拼写




# **搜索类**

 

- Ctrl+F 打开底部搜索框，查找关键字。
- Ctrl+shift+F 在文件夹内查找，与普通编辑器不同的地方是sublime允许添加多个文件夹进行查找，略高端，未研究。
- Ctrl+P 打开搜索框。举个栗子：1、输入当前项目中的文件名，快速搜索文件，2、输入@和关键字，查找文件中函数名，3、输入：和数字，跳转到文件中该行代码，4、输入#和关键字，查找变量名。
- Ctrl+G 打开搜索框，自动带：，输入数字跳转到该行代码。举个栗子：在页面代码比较长的文件中快速定位。
- Ctrl+R 打开搜索框，自动带@，输入关键字，查找文件中的函数名。举个栗子：在函数较多的页面快速查找某个函数。
- Ctrl+： 打开搜索框，自动带#，输入关键字，查找文件中的变量名、属性名等。
- Ctrl+Shift+P 打开命令框。场景栗子：打开命名框，输入关键字，调用sublime text或插件的功能，例如使用package安装插件。
- Esc 退出光标多行选择，退出搜索框，命令框等。




# 显示类

 

- - Ctrl+Tab 按文件浏览过的顺序，切换当前窗口的标签页。
  - Ctrl+PageDown 向左切换当前窗口的标签页。
  - Ctrl+PageUp 向右切换当前窗口的标签页。
  - Alt+Shift+1 窗口分屏，恢复默认1屏（非小键盘的数字）
  - Alt+Shift+2 左右分屏-2列
  - Alt+Shift+3 左右分屏-3列
  - Alt+Shift+4 左右分屏-4列
  - Alt+Shift+5 等分4屏
  - Alt+Shift+8 垂直分屏-2屏
  - Alt+Shift+9 垂直分屏-3屏
  - Ctrl+K+B 开启/关闭侧边栏。
  - F11 全屏模式
  - Shift+F11 免打扰模式

# sublime text 3 mac 快捷键

command+shift+n：new_window
command+shift+w：close_window
command+o：打开文件或文件夹
command+w：关闭当前文件
command+shift+t：撤回关闭的文件
command+alt+s：保存当前文件夹中的所有文件
command+k, command+b：打开侧边栏
command+z：撤销
command+shift+z：反-撤销
command+u：软撤销（包括光标的位置）
command+shift+u：反-软撤销（包括光标的位置）
command+shift+v：粘贴（并格式化）
command+option+v：粘贴（从粘贴板中选择）
command+alt+left：上一个文件
command+alt+right：下一个文件
command+shift+l：所有选中行的后面添加光标
command+[：向前缩进
command+]：向后缩进
command+l: 选择当前行
command+d: 选择当前单位
command+shift+space: 选择当前多个相似单位
ctrl+shift+m: 选择{}区域(主要用于js)
ctrl+m: 选择{}开始标签和闭合标签
command+shift+j: 选择同级元素下的区域或{}下的区域
command+shift+a: 选择子元素下的区域(使用html)
command+alt+.: 闭合标签
command+alt+f: 替换(当前文件)
command+shift+f: 替换(跨文件)
ctrl+command+up: 当前行上移一行
ctrl+command+down: 当前行下移一行
ctrl+g: 定位到某一行

alt+command+2||3||4: 左右分2||3||4页
command+alt+shift+2||3||4: 上下分2||3||4页
alt+command+1: 取消分页

"command+k", "command+x": 添加标记
"command+k", "command+g": 删除全部标记
"command+k", "command+w" 删除光标与标记点之间的内容
"command+k", "command+a": 选择光标与标记点之间的内容

"command+alt+o": 开启重写(光标变为_)

1.control+alt+enter 打开Emmet(Zencoding)

2.super+shift+m 自定义sublimeCodeIntel查询键

3.super+n  新建文件，super+s  保存文件，super+o  打开文件

4.super+alt+s  保存所有打开文件

5.super+kb  关闭或打开左侧边栏

6.super+shift+v  缩进粘贴

7.super+alt+left/right  查看左边或右边的文件

8.super+l  选中一行，多按向下选中多行

9.super+d  向下选中当前字符串，可以一次进行多个字符串替换

10.super+kd  跳过下一个选中的字符串

11.ctrl+shift+m  选中括号里面的内容

12.super+enter | super+shift+enter  向下或上另起一行

13.super+p | super+shift+p  最常用，不解释

14.super+f | super+alt+f  搜索字符串

15.super+g | super+shift+g  查找下一个/上一个

16.super+shift+d  复制当前行到下一行

17.super+delete  删除该行