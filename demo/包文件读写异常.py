"""
模块其实就是一个python文件
想要使用模块的内容就要导入
两种导入方式：1. import 模块名    2.from 模块名 import 成员名
把a2的文件导入a1，a1可以使用a2所有的类，方法，属性

"""

# 包是⼀个包含多个模块的特殊⽬录，目录里有文件或目录组成 。
# ⽬录下有⼀个 特殊的⽂件 __init__.py
# 包名的 命名⽅式 和变量名⼀致， ⼩写字⺟加_导入包和导入模块的方式是一样的
# 常见的系统包 os datetime sys
# import os
# print(os.listdir()) #返回当前路径下所有的文件和文件夹
# print(os.getcwd()) #返回当前的工作目录
# print(os.path.exists("E:\python\python基础"))
# import datetime
# print(datetime.datetime.now())
# import sys
# print(sys.path)
"""
下载命令 pip install 包名
操作文件  f = open('a.test','r')
result = f.read()
print(result)
f.close()

read write close
open 函数负责打开⽂件， 并且返回⽂件对象
read / write / close 三个⽅法都需要通过 ⽂件对象 来调⽤

r   以只读⽅式打开⽂件。 ⽂件的指针将会放在⽂件的开头， 这是默认模式。 如果⽂件不
存在， 抛出异常
w   以只写⽅式打开⽂件。 如果⽂件存在会被覆盖。 如果⽂件不存在， 创建新⽂件
a   以追加⽅式打开⽂件。 如果该⽂件已存在， ⽂件指针将会放在⽂件的结尾。 如果⽂件
不存在， 创建新 ⽂件进⾏写⼊
r+  以读写⽅式打开⽂件。 ⽂件的指针将会放在⽂件的开头。 如果⽂件不存在， 抛出异常
w+  以读写⽅式打开⽂件。 如果⽂件存在会被覆盖。 如果⽂件不存在， 创建新⽂件
a+  以读写⽅式打开⽂件。 如果该⽂件已存在， ⽂件指针将会放在⽂件的结尾。 如果⽂件
不存在， 创建新⽂件进⾏写⼊
"""
# try....except语句
#语法格式：
# try:可能出现异常的代码块
# except Exception as e:
# print(e)
# #实例：
# try:print(10 * 2 / 0)
# except Exception as e:
# print(e)
# print("======")



