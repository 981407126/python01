# 1、请输入abcd四个数，计算a+b-c*d的值
# a = int(input("请输入第一个值"))
# b = int(input("请输入第二个值"))
# c = int(input("请输入第三个值"))
# d = int(input("请输入第四个值"))
# print(a+b-c*d)
# -------------------------------------
# 2、打印1-100内被3整除的所有数的和
# 第一种sum = 0
# for x in range(1,101,1) :
#     if x % 3 == 0 :
#         sum += x
# print(sum)
# 第二种sum = 0
# for x in range(3,101,3):
#     sum += x
# print(sum)
# 第三种a = 0
# sum = 0
# while a < 100:
#     if a % 3 == 0:
#        sum += a
#     a += 1
# print(sum)
# ---------------------------
# 3、使用range()函数打印1-10内所有奇数
# for x in range(1,11,1) :
#     if x % 2 != 0 :
#         print(x)
# ----------------------------
# 4、打印1-100所有偶数的和减去所有奇数的和的值
# 第一种sum1 = 0
# sum2 = 0
# for x in range(1,101,1):
#     if x % 2 == 0 :
#         sum1 += x
# for y in range(1,101,1):
#     if y % 2 != 0 :
#         sum2 += y
# print(sum1-sum2)
# 第二种sum1 = 0
# sum2 = 0
# for x in range(1,101,1):
#     if x % 2 == 0:
#         sum1 += x
#     else:
#         sum2 += x
# print(sum1-sum2)
# --------------------------------
# 5、求1+2+3+...+100的和
# sum = 0
# for x in range(1,101,1):
#     sum += x
# print(sum)
# ----------------------------------
# 6、判断一个数n能同时被3 和 5 整除
# a = int(input("请输入一个数:"))
# if a % 3 == 0 and a % 5 ==0 :
#     print("正确")
# else:
#     print("错误")
#  -------------------------------
# 7、定义一个整数变量，判断该变量值是否是1-100内的某个数
# a = int(input("输入一个整数"))
# if a in range(1,101,1):
#     print("正确")
# else:
#     print("错误")
# -------------------------------
# 8、输入三个整数x，y，z，请把这三个数由大到小输出
# x = int(input())
# y = int(input())
# z = int(input())
# list1 = [x,y,z]
# list1.sort()# 排序之后在打印，不能直接print（list1.sort（） ）
# print(list1)
# ------------------------------
# 9、利用条件运算符来嵌套完成此题：学习成绩>=90分的同学用A表示，60-89分 的同学用B表示，60分以下的同学用C表示
# a = int(input())
# if 90<= a <= 120 :
#     print('A')
# elif 60 <= a <=89 :
#     print('B')
# elif  0 <= a < 60 :
#     print('C')
# else:print("输入的成绩错误")
# ---------------------------------
# 10、将一个列表的数据复制到另一个列表中
# a = [1,2,3,4,5,6,7]
# b = [8,9,10]
# a.extend(b)
# a.sort()
# print(a)
# --------------------------------------
#  11、打印9*9乘法表
# x = 1
# y = 1
# for x in range(1,10,1):
#     for y in range(1,x+1,1):
#         print(x,'*',y,'=',x*y,end=' ')
# end代表在输出最后加上某个东西，print默认添加的是end='\n'换行符，我们在end后加个空格可以阻止换行
#     print()
# ------------------------------------
# 12、输入一行字符串，分别统计出其中的英文字母、空格、数字和其他字符的个数
# astr = str(input("请输入字符串:"))
# zm = 0
# kg = 0
# sz = 0
# other = 0
# for x in astr :
#     if x.isalpha():
#         zm += 1
#     elif x.isspace():
#         kg +=1
#     elif x.isdigit():
#         sz +=1
#     else:
#         other +=1
# print("英文字母:",zm)
# print("空格:",kg)
# print("数字:",sz)
# print("其他字符:",other)
# -----------------------------------------
# 13、打印出如下图型 菱形
# 第一种num = 5
# x = num - 1
# for n in range(1,num):
#     space = " " * (x-n)
#     star = "*" * (2*n-1)
#     print(space + star + space)
# for n in range(1,4):
#     space = " " * n
#     star = (5 - (n - 1) * 2) * "*"
#     print(space + star + space)

















