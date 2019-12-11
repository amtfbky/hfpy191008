## 1.多用户多任务分时操作系统

Windows、Linux、Mac OS X等

任务：电脑时间资源的使用者，各种进程

### 1.1用户身份

Windows也具备，甚至比Linux做得要好，只不过很多人不注意！

故障修复需要**单用户模式**：操作系统不用确认用户的身份，可以进行各种操作。

#### 超级用户root

/root

#### 普通用户

可以有2的32次方-1个

/home

#### 特殊用户

bobody、admin、ftp

#### 用户组

在更高的层面来抽象用户所能够访问文件的数量，结合不同的用户组，就能给每个用户构建出独一无二的文件访问列表；不同的用户之间还能做到交错纵横，有条不紊：用户之间的协作上和隐私的保护上达到了一个良好的平衡。

#### 待遇差别（用户）

是否分配home目录和shell，是否设置密码？能访问到的文件，即访问限制。

注：有些用户根本就不用，占坑，只是为了兼容。

### 1.2查看

/etc/passwd文件查看用户

保存密码的文件/etc/shadow，俗称影子文件

用户名:密码:UID:GID:用户全名:home目录:shell

/etc/group

组名:用户组密码:GID:组内的用户名

/etc/gshadow

#### 1.3管理用户和组

增adduser、useradd

在Ubuntu中adduser是一个脚本封装了useradd二进制程序，更加智能。

CentOS中两个相同

#useradd xxx （默认值：UID GID /home/xxx shell=/bin/bash）

#passwd

root可以直接修改用户密码，不需要使用到用户的密码。

#usermod 修改用户的配置

#userdel 删除用户 -r“抄家”（删除/home目录）

sudo：给某个用户赋予sudo特权/etc/sudoers

wheel