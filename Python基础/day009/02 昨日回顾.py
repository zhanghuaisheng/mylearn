# 1.文件操作
# open() --打开
# file = 文件名或路径
# mode= 操作文件的moshi
#     r w a rb wb ab r+ w+ a+
#encoding = 编码
# 文件中存储的都是字符串

# 路径
# 绝对路径:从磁盘根部查找
# 相对路径:当前运行的文件目录查找
# .\  当前
# ..\ 父目录(上一级)

# 转义:
# 1.\\
# 2.r

# 读操作(r,rb)
# read()全读
# read(3)  单位取决于读取方式
# readline 读取一行
# readlines 全部读取，存放列表
# for i in f：
# 文件在不移动光标的情况下只能读取一遍

# 写操作
# 清空写(w,wb)
# 1.在open时清空文件中的内容（一次）
# 2.再写入内容

# 追加写(a,ab)
# 追加写一直都是在文件的末尾添加

# +操作
# r+ 读写
# 先读后写-追加的方式
# 先写后读-覆盖之前的内容

# w+清空写读
# 1.清空文件
# 2.写
# 3.移动光标再读取

# a+ 追加写，读
# 先写后读
# 需要移动光标

# a,w都具有创建文件的功能

# 光标
# seek(0,0) 移动到文件头部seek(0)
# seek(0,1) 移动到光标当前位置
# seek(0,2) 移动到文件末尾
# seek(3)  按照字节移动，具体字节根据编码决定大小

# tell()  查看光标，返回字节

# with open()  --上下文管理（面向对象）
# 1.自动关闭文件
# 2.同时操作多个文件
# 3.as取别名

# 文件修改