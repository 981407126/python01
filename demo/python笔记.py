# # a = int(input("请输入第一个数:"))
# # b = int(input("请输入第二个数:"))
# # c = int(input("请输入第三个数:"))
# # d = int(input("请输入第四个数:"))
# # print( a+b-c**d )
# #-------------------------------------------------------
# # a = 0
# # sum = 0
# # while a < 100 :
# #     a += 3
# #     sum += a
# # print(sum)
# #------------------------------------------------------
# #
# # for x in range(1,101,1) :
# #     if x % 3 != 0 :
# #         continue
# #     print(x)
# # list = [] 列表
# # qq_usr = [11,25,'list',None]
# # for x in qq_usr :
# #     print("QQ列表",x)
# # ----------------------------------------------
# # 列表，clst = ['red','green','blue']
# # clst.append('black')
# # print("使用append在列表最后添加元素",clst)
# # alst = ['white','pink']
# # clst.extend(alst)
# # print("使用extend在列表最后中添加其他列表的元素",clst)
# # clst.reverse()
# # print("使用reverse反转列表中的元素",clst)
# # clst.sort()
# # print("使用sort对列表进行排序",clst)
# # print("使用count统计列表元素出现的次数",clst.count('blue'))
# # print("使用index找出某个元素的位置",clst.index('black'))
# # clst.insert(1,'hello')
# # print("使用insert在指定的位置插入某个元素",clst)
# # ----------------------------------------------------------
# # 元组与列表相同，但元组是不能修改的
# # tp1 = ()
# # tp2 = (1,2,3,'hello',None)
# # print(tp1)
# # print(tp2)
# # for x in tp2 :
# #     print(x)
# # -----------------------------------------------------------
# # 字典{} ，是一种无序的，可变的序列，每组元素都要有对应的键对值，用冒号进行相连，多组元素用逗号隔开
# # d = {key1:obj1,key2:obj2}
# dict1 = {'a':1,'b':2,'c':3}
# print("使用[]来获取字典中键名为b对应的值",dict1['b'])
# dict1['c'] = 4
# print("使用[] = 来更新键名c所对应的值",dict1)
# dict2 = {'d':3,'e':5}
# dict1.update(dict2) #使用update来将字典2更新进字典1中
# print(dict1)
# print('e' in dict1) # 使用in判断键名e是否存在与字典1中
# # 获取字典中所有的键名： dict.keys（）
# print("获取字典中所有的键名",dict1.keys())
# # 只用使用dict.keys()输出迭代器，才能将字典进行循环,迭代器中的值是字典内所有的键名，而不是键名对应的值
# for x in dict1.keys() :
#     print(x)
# print(dict1.values()) # dict.values 才是字典中所有的值
# for x in dict1.values() :
#     print(x)
# print(dict1.items()) #使用items返回所有的键对值，进行循环的时候要for x，y 两个值
# for x,y in dict1.items() :
#     print(x,y)
# ----------------------------------------------------------
# 字符串格式化  可以将字符串单独分离出来 %s 格式化字符串 "%d" % 格式化整数   "%f" % 格式化浮点数
# my_str = "my name is %s" % ('lisi')
# print(my_str)
# my_str1 = "my name is %d" % (123)
# print(my_str1)
# my_str2 = "my name is % 6.2f" % (123.256)
# print(my_str2)
# print("保留3位数字->'%.3f'" % 659) print("返回的数字宽度是8位，小数后两位，默认右对齐->'%8.2f'" % 659)
# 数字宽度8位，数字占了6位，剩余的两位被空格占用
# print("返回的数字宽度是8位，小数后两位，设置左对齐->'%-8.2f'" % 659)
# print("数字前显示+号->'%+8.2f'" % 659)
# print("数字前显示-号->'%+8.2f'" % -659)
# print("总宽度是8位，小数后两位，剩余空位用0补齐->'%08.2f'" % 659)
# #运行结果： 返回的数字宽度是8位，小数后两位，默认右对齐->' 659.00'
# 返回的数字宽度是8位，小数后两位，设置左对齐->'659.00 '
# 数字前显示+号->' +659.00' 数字前显示-号->' -659.00'
# 总宽度是8位，小数后两位，剩余空位用0补齐->'00659.00'
# mystr_3 = "张三今年{}岁".format("25")
# print(mystr_3)
# --------------------------------------------------------
# format格式化两个参数
# mystr_4 = "今天星期{}，张三买了两斤{}".format("三","苹果")
# print(mystr_4)
# mystr_5 = "今天星期{1}，张三买了两斤{0}".format("三","苹果") # 使用位置参数可以将格式化的参数进行排序
# print(mystr_5)
# mystr_6 = "今天星期{a}，张三买了两斤{b}".format(a="三",b="苹果") # 或者添加关键字参数与位置参数结合使用
# print(mystr_6)  # 但位置参数必须在关键字参数前面      "{0}{x}".format("三",x="四")
# ------------------------------------------------------------
# 序列的通用操作
"""
1.索引 seq[index] index代表下标- 列表，序列，字符串
lst = ['red','hello',2,3,5]
print(lst[0])
tp = ('red','hello',2,3,5,)
print(tp[1])
2.切片 lst[start:end:step]
start 包括该位置 end不包括该位置
lst5 = ['red','green','blue','black','gold','orange']
print("获取第2-5个元素:",lst5[1:5])
#有start,end，没有step,默认为1
print("获取第2,4,6个元素:",lst5[1:6:2])
#从第2个元素到第7个元素，遵循左臂右开原则，不包 括第7个
print("获取第1,3,5个元素:",lst5[::2])
#步长为2
print("获取第3个及后面的元素:",lst5[2:])
print("将列表翻转：",lst5[::-1])
"""
# lst1 = ['ada',5,'ccc',564,2,31,'?',1,'sad',41]
# print(lst1[::2])
# print(lst1[1::2])
"""
序列的相加和相乘+，*
#列表相加，相乘 a_list = ['abc'] 
b_list = ['xyz'] 
c_list = a_list + b_list 
print("两个列表相加后产生的新列表:",c_list) 
print("列表a_list乘3后产生的新列表:",a_list*3) 
#运行结果 两个列表相加后产生的新列表: ['abc', 'xyz'] 
两个列表相乘后产生的新列表: ['abc', 'abc', 'abc']
"""
# 多用到for循环的参数 enumerate 可以将序列的索引和值都循环出来
# lst8 = ['red', 'yellow', 'cream', 'blue', 'gunmetal']
# for index,values in enumerate(lst8) :
#     print(index,"====",values)
"""
列表推导式 : [表达式2 循环体 表达式1 ]
生成一个1-10的列表
lst = []
for x in range(1,11):
    lst.append(x)
print(lst)
============================
[ x for x in range(1,11) ]
==================================
for x in iterable : 循环的是一个序列，包括字典，元组，字符串以及range()方法。for循环体是最
先被执行的。
expA：主要是由if语句或for语句构成，如果是if语句，一般是将x进行条件筛选，符合条件的传给
expB参与运算，如果是for循环，那就是双层嵌套循环，这里需要注意的是，后面的for是内层循
环 。当然该表达式也可以不写 。
expB:主要是对for循环中的x进行的最后的运算，可以是+，-，*，%，|，条件判断以及各种方法
等 。
lst1 = [x for x in range(0,10) ] 
#1.for循环后无表达式 
lst2 = [x for x in range(0,10) if x % 2 == 0] 
#2.for循环后if条件表达式 
lst3 = [x*2+1 for x in range(0,10) if x % 2 == 0] 
#3.返回的值参与计算 
lst4 = [y+str(x) for x in range(1,3) for y in ['x','y','z']] 
#4.嵌套循环 
print("生成0~9的列表：",lst1) 
print("对0~9的数对2取余返回新列表：",lst2) 
print("对0~9的数对2取余后再参与计算:",lst3) 
print("嵌套循环生成的数相连接：",lst4) 
#运行结果： 生成0~9的列表： 
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
对0~9的数对2取余返回新列表： 
[0, 2, 4, 6, 8] 
对0~9的数对2取余后再参与计算: 
[1, 5, 9, 13, 17] 
嵌套循环生成的数相连接：
 ['x1', 'y1', 'z1', 'x2', 'y2', 'z2']
"""

