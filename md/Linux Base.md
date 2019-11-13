# Linux Base

## install

CentOS-5.3-x86_64-bin-DVD.iso

md5:6d4fd59688ed8644514010316d6a5698

sha1:f8ca12b4acc714f4e4a21f3f35af083952ab46e0

### 1.磁盘分区

​	/boot	100MB	primary

​	/		10GB	primary

​	/home	5GB		primary

​	swap	1GB		logical

### 2.图形界面安装

### 3.安装后配置

#### 3.1关闭selinux

​	vi /etc/selinux/config

#### 3.2配置本地源+安装vim

​	mount /dev/cdrom /mnt

​	mkdir /etc/yum.repo.d/bak

​	mv /etc/yum.repo.d/*repo /etc/yum.repo.d/bak

​	vi /etc/yum.repo.d/local.repo

```shell
[centos]

name=centos

baseurl=file:///mnt

enabled=1

gpgcheck=0

```



​	yum clean

​	yum list

​	yum install vim-X11 vim-common vim-enhanced vim-minimal

#### 3.3配置远程连接

​	vim  /etc/sysconfig/network-scripts/ifcfg-eth0

```shell
DEVICE=eth0

BOOTPROTO=static

BROADCAST=192.168.43.255

HWADDR=08:00:27:CF:2D:91

IPADDR=192.168.43.88

NETMASK=255.255.255.0

NETWORK=192.168.43.0

GATEWAY=192.168.43.1

ONBOOT=yes

```

## 一、Linux的文件权限与目录配置

甜点：Linux最优秀的地方之一，就是多人多任务环境。

难点：各个使用者文件的保密性。

### 1.基本概念

-rw-r--r-- 1 root root  22K Nov  1 13:09 install.log

文件类型和权限：-rwxrwx--- r可读Read，w可写Write，x可执行Execute，-减号代表没有权限

​	第一个字符：d目录，-普通文件，l链接文件，b块文件（可随机存取的设备），c一次性读取设备

​	接下来分三组：第一组是文件所有者的权限；第二组是文件所有者所属群组的权限；第三组是其他所有者的权限

链接数：每个文件都会把它的权限和属性记录到文件系统的i-node中，这个数字就是记录有多少个文件名链接到这个文件。在文件系统中会再详细讲解。

文件所有者：User

文件所属群组：Group

其他所有者：Other

文件大小

文件最后被修改的时间

文件名称：.config隐藏文件，ls -a可查看