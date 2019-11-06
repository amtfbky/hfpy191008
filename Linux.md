# Linux

test1,test2,test3同属testgroup这个群组

-rw-r--r-- 1 root root 238 Jun 18 17:22 test.txt

-rwxr-xr-- 1 test1 testgroup 5238 Jun 19 10:25 testfile

分析：

- test1对testfile具有可读可写可执行的权力
- 而同群组的 test2, test3 两个人与 test1 同样是 testgroup 的群组账号，则仅可读可执行但不能写(亦即不能修改)
- 至于非 testgoup 这一个群组的人则仅可以读，不能写也不能执行

## 练习1

drwxr-xr-- 1 test1 testgroup 5238 Jun 19 10:25 groups/ 

testgroup群组的成员与其他人是否可以进入本目录？

分析：

- 文件所有者test1可以在本目录中进行任何工作；
- 而 testgroup 这个群组的账号，例如 test2, test3 亦可以进入本目录进行读取和执行，但不能在本目录下进行写入的动作；
- 至于other虽然有读取权限，但由于没有执行的权限，因此other的使用者不能进入此目录。

### 改变文件属性与权限

1.改变所属群组

chgrp [-R:recursive] dirname/filename ...

2.改变文件所有者

chown [-R] bin filename 把文件所有者改成bin这个用户

chown root:root filename 把文件所有者和所属群组改成root

那什么时候要改变文件所有者和所属群组呢？

```
cp .bashrc .bashrc_test
ls -al .bashrc*
-rw-r--r-- 1 root root 176 Jan  6  2007 .bashrc
-rw-r--r-- 1 root root 176 Nov  5 15:11 .bashrc.bak
```

Cp会复制原文件的属性与权限，那我们要把文件给别的用户，怎么办？

3.改变权限

- 权限分数对照表：r:4 w:2 x:1 chmod 754 filename
- u,g,o,a +-= r,w,x：chmod u+w,g-w,o+x filename，这样可以在不知道文件原先属性时方便修改，而不致于把破坏原先的权限

### 目录与文件的权限之意义

1.对文件的意义

文件包含文本文件、数据库文件、二进制可执行文件(binary program)等等。

意义：

- r(read)：读取
- w(write)：增、改，不含删
- x(eXecute)：被系统执行的权限

Windows是靠扩展名来判断是否有执行能力，如：.exe，.bat，.com等等；在Linux下，是看x这个权限来决定的。

2.对目录的意义

目录主要是记录文件名列表。

意义：

- r(read contents in dircetory)：读取目录结构列表的权限，所以ls这个指令得以执行
- w(modify contents of dircetory)：异动目录结构列表的权限：
  - 建立新的文件与目录
  - 删除已经存在的文件与目录(不论该文件的权限是多大)
  - 更名
  - 移动位置
- x(access directory)：目录可执行代表用户能否进入该目录

例1：进入目录的权限

drwxr--r-- 3 root root 4096 Jun 25 08:35 .ssh

普通账户可以查询此目录下的文件名列表，但不能切换到此目录。

因为一直涉及到普通用户和管理员用户，我们先了解一下新建普通用户(useradd)的基本知识：

```
在创建用户时，可以使用下面的命令行参数改变默认值或默认行为： 

-c comment 给新用户添加备注 
-d home_dir 为主目录指定一个名字（如果不想用登录名作为主目录名的话） 
-e expire_date 用YYYYY-MM-DD格式指定一个账户过期的日期 
-f inactive_days 指定这个帐户密码过期后多少天这个账户被禁用；0表示密码一过期就立即禁 
用，-1表示禁用这个功能 
-g initial_group 指定用户登录组的GID或组名 
-G group ... 指定用户除登录组之外所属的一个或多个附加组 
-k 必须和-m一起使用，将/etc/skel目录的内容复制到用户的HOME目录 
-m 创建用户的HOME目录 
-M 不创建用户的HOME目录（当默认设置里指定创建时，才用到） 
-n 创建一个同用户登录名同名的新组 
-r 创建系统账户 
-p passwd 为用户账户指定默认密码 
-s shell 指定默认登录shell 
-u uid 为账户指定一个唯一的UID 
```

```
# useradd -D
GROUP=100
HOME=/home
INACTIVE=-1
EXPIRE=
SHELL=/bin/bash
SKEL=/etc/skel
CREATE_MAIL_SPOOL=yes
```

useradd是Linux添加新用户的命令，这个命令提供了一次性创建新用户账户及设置用户HOME目录结构的简便方法。

1、useradd命令加参数-D参看系统的默认值

解释： 

1）新用户添加到GID为100的公共组 
2）新用户的HOME目录将会位于/homoe/username 
3）新用户账户密码在过期后不会被禁用 
4）新用户账户未被设置为某个日期后就过期 
5）新用户账户将bash shell作为默认shell 
6）系统会将/etc/skel目录下的内容复制到用户的HOME目录下 
7）系统为该用户账户在mail目录下创建一个用于接收邮件的文件

倒数第2个值很有意思。useradd命令允许管理员创建一个默认的HOME目录配置，然后把它作为创建新用户HOME目录的模板。这样，就能自动在每个新用户的HOME目录里放置默认的系统文件。在CentOS 5.3系统上，/etc/skel目录下有下列文件： 

```
# ls -la /etc/skel/
total 48
drwxr-xr-x  3 root root 4096 Nov  3 23:58 .
drwxr-xr-x 85 root root 4096 Nov  6 00:22 ..
-rw-r--r--  1 root root   33 Jan 22  2009 .bash_logout
-rw-r--r--  1 root root  176 Jan 22  2009 .bash_profile
-rw-r--r--  1 root root  124 Jan 22  2009 .bashrc
drwxr-xr-x  4 root root 4096 Dec 20  2008 .mozilla
```

同样，你可以用-D参数后面跟一个要修改的值的参数，来修改系统默认的新用户值。这些参数如下表：

```
-b default_home 更改默认的创建用户HOME目录的位置 
-e expiration_date 更改默认的新账户的过期日期 
-f inactive_days 更改默认的新用户从密码过期到账户被禁用的天数 
-g group 更改默认的组名称或GID 
-s shell 更改默认的登录shell 
```

如 #useradd -D -s /bin/tsch ，修改默认的shell为/bin/tsch。

另外，删除用户，使用userdel命令。默认情况下，userdel命令只会删除/etc/passwd文件中的信息，而不会删除系统中属于该账户的任何文件。 
如果加上-r，userdel会删除用户的HOME目录以及mail目录。然后，系统上仍可能存有归已删除用户所有的其他文件。这在有些环境中会造成问题。 
PS：在有大量用户的环境中使用-r参数时要特别小心。你永远不知道用户是否在他的HOME目录下存放了其他用户或其他程序要使用的重要文件。记住在删除用户的HOME之前一定要检查清楚！

注意：架设网站很容易在权限的设定上出错！就是只给r的权限，没有给x的权限，导致用户浏览不了文件的内容！！！但w的权限不可随便给！我们看一个例子：

-rwx------ 1 root root 4365 Sep 19 23:20 the_root.data

在你的家目录下有这么一个文件，你对它的权限是什么？能删除它吗？

分析：

- 你对该文件是others的身份，你权限为0
- 但最关键的一点是——你可以删除它，因为它在你的家目录下

#### 练习：普通用户删除权限

```
cd /tmp
mkdir testdir
chmod 744 testdir
touch testdir/testfile
chmod 600 testdir/testfile
ls -ald testdir testdir/testfile
su - user1
$ cd /tmp
$ ls -l testdir  # 权限不足
$ exit
chown user1 testdir  # 修改权限，让user1拥有此目录
su - user1
$ cd /tmp/testdir
ls -l  # 虽然可以查看，但文件不是user1的
rm testfile  # 删除这个文件
```

### 文件种类与扩展名

1.文件种类

- 正规文件(regular file)
  - 纯文本文件(ASCII)：cat filename
  - 二进制文件(binary)：Linux的可执行文件（scripts，文字型批处理文件不算），如：cat
  - 数据格式文件(data)：有些程序在动作的过程中会读取某些**特定格式**的文件，如：Linux在登入时，都会将登录的数据记录在/var/log/wtmp，last指令可以读出来；cat会读出乱码
- 目录
- 链接文件(link)：类似Windows的快捷方式
- 设备与装置文件(device)，通常集中在/dev
  - 区块(block)设备文件：一些存储数据，以提供系统随机存取的接口设备，如：硬盘 /dev/sda
  - 字符(character)设备文件：一些串行端口的接口设备，如：键盘、鼠标等等
- 数据接口文件(sockets)：通常被用在网络上的数据承接，如：启动一个程序来监听客户端的要求，而客户端就可以通过这个socket来进行数据的沟通，/var/run
- 数据输送文件(FIFO,pipe)：解决多个程序同时存取一个文件所造成的错误问题，first-in-first-out

2.扩展名

- *.sh
- \*Z,\*.tar,\*.tar.gz,\*.zip,\*tgz
- \*.html,\*.php,\*.py

3.Linux文件名的限制

避免特殊字符：\* ? > < ; & ! [ ] | \\ ' " ( ) { }

避免以-或+开头

### 目录配置

Filesystem Hierarchy Standard (FHS)标准：规范每个特定的目录下应该 要放置什举样子的数据

|        |        可分享的         |      不可分享的       |
| :----: | :---------------------: | :-------------------: |
| 不变的 |    /usr(软件旋转处)     |    /etc(配置文件)     |
|        |    /opt(第三方软件)     | /boot(开机与核心文件) |
| 可变的 |  /var/mail(user email)  |  /var/run(程序相关)   |
|        | /var/spool/news(新闻组) |  /var/lock(程序相关)  |

 

