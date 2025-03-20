# print("hello world")
# print("h")
# print("he")
# print("hee")
# print("hello")
# print("hello w")
# print("hello wo")
# print("hello wor")
# print("hello","world","你好",sep="oo")
# print("hello",end="*")
# print("world","你好")
# num1=1     #商品1号的单价
# num2=3     #商品2号的单价
# total=num1+num2
# print(total)
# a=666
# print(a)
# a=999
# print(a)
# 转义符：
# 1. %s 字符串(占位符）
# name="a"
# print("my name is %s" % name)

# 2. %d 整数
# name="a"
# age=18
# print("my name is %s,age is %d" %(name,age))

# 3. %f 浮点型
# num=1.23456
# print("num=%4f" %num)

# 4. %4d 占位符，占据了多少个位置，默认以空格代替
# num=123
# print("num=%06d" % num)

# 5. %.4f
# num=1.23456
# print("num=%.4f" % num)

# 运算符
# 1. +-*/
# print(2/1)
# a=1/1
# print(type(a))

# 2. // 取整除
# a=5
# b=2
# print(a//b)

# 3. %取余数
# a=5
# b=2
# print(a%b)  #5%2=2...1

# 4. ** 幂（次方）
# a=4
# b=2
# print(a**b)

# 5.计算顺序： 幂>* />+ -
# print(4**2+5*5+10/5-3)

# 6. 运算符 +=
# a=5
# a+=1
# print(a)

# 7. -=
# a=5
# a-=1
# print(a)

# n1=55
# n2=33
# total=n1+n2
# print(total)

# n1=55
# n2=33
# n1+=n2
# print(n1)

# 赋值变量
# n1=55
# n2=11
# n3=n1
# n4=n3+n2
# print(n4)

# 输入
# name=input("请输入您的名字：")
# print(name)

# 转移字符
# 1. \t  制表符， 通常空4个空格，简称：缩进
# print("super\tstar")
# print("age\tname\tschool")

# # 2. \n 换行符
# print("haha\nxixi")
#
# #3. \r 回车
# print("have a good \rday!")

# 4. \\反斜杠
# print(r"have a \\nice day!")  #添加r，默认取消转义

# 判断语句
# 1. if
# score=input("请输入您的成绩：")
# print(type(score))   #检验score类型，发现输出为字符串，需转整形，所以需加int（）在input外面
# if 100 >= score >=90 :
#     print("优秀")
# elif 90 > score >=75 :
#     print("良好")
# elif 75 >  score >=60 :
#     print("及格")
# elif score > 100 :
#     print("无效成绩")
# else:
#     print("不合格")

# 2. ==
# score=input("请输入你的成绩：")
# if score== '100' :   # 数值添加“”，字符串判断是否相等
#     print("very Good!")
# if score== '60' :
#     print("加油")

# 3. ><
# a=6666
# b=999
# if a > b :
#     print("a>b")
# else:
#     print("a<b")

# 4.and 全部为真则为真
# a=111
# b=777
# if a==111 and b==777 :
#     print("a=b")

# 5. or  一个为真则为真
# a=11
# b=77
# if a==111 or b==777 :
#     print("a=b")

# 6. 比较运算符
# a=4
# b=6
# # if a<=b :
# #     print("a小于等于b")
# # else:
# #     print("a大于b")
# print("a小于等于b") if a <= b else print("a大于b")  #三目运算 格式：真结果  if 判断条件  假结果


# while 循环语句
# 输出100遍“好好学习，天天向上”
# i =1
# while i <= 5 :
#     print("好好学习，天天向上")
#     i+=1

# 计算1+2+3+...+100 的总和
# i=1
# s=0
# while i <= 100:
#     s += i
#     i += 1
# print("计算总和为：",s)

# 循环格式
# while 条件1：
#     循环体1
#     while 条件2 ：
#         循环体2
#         改变变量2
#       改变变量1

# i =1       # 定义一个变量记录外循环的次数
# while i <= 3:  #外循环
#     print(f"这是第{i}次外循环")
#     j = 1   #定义一个变量记录内循环的次数
#     while j <= 5 :  #内循环
#         print(f"{j}次内循环")
#         j += 1
#     i += 1


# for 循环
# 基本格式：  for 临时变量  in 可迭代变量：
#                 循环体
#  输出“hellopython”逐个字符
# str = "hellopython"    #定义一个字符串变量，字符串为可迭代变量。 可迭代变量就是遍历去取值的整体
# for i in str :
#     print(i)

# 2. range()  用来记录循环次数，相当于一个计数器
# for i in range (1,6):  # 相当于[x,y）,包前不包后
#     print(i)


# s = 0
# for i in range(1,101):
#     s += i
# print("计算总和为：",s)


# # 输出99乘法表(while 循环写法
# i = 1      #行
# while i <= 9:    #一共有9行      --外循环
#     j = 1  # 列
#     # print(f'{j}*{i}={j*i}'end="\t")
#     while j <= i:              # 有多少行就有多少列  --内循环
#         print(f'{j}*{i}={j*i}', end="\t")
#         j += 1
#     print() #执行完内循环后需要换行，再换一行执行外循环
#     i += 1


# for i in range(1,10):
#     for j in range(1,i+1):
#      print(f'{j}*{i}={j * i}',end = "\t")
#     print()  # 执行完内循环后需要换行，再换一行执行外循环

#  break 跳出循环
#  一共有5个苹果，a吃到第3个时吃饱了，不吃了
# i = 1
# while i <=5:
#     print(f"吃第{i}个苹果")
#     if i == 3:
#         print(f"饱了")
#         break
#     i += 1

# #  break 跳出循环 for
# for i in range(1,6):
#     print(f"吃第{i}个苹果")
#     if i == 3:
#         print(f"饱了")
#         break

# continue  跳过当前循环，进入下一段循环
# 一共有5个苹果，a吃到第3个时有个虫子，换一个吃
# i =1
# while i <=5:
#     print(f"吃第{i}个苹果")
#     if i == 3 :
#         print(f"吃第{i}个时吃到虫子，不吃了")
#         i += 1
#         continue
#     i += 1

# # for 写法
# for i in range(1,6):
#     print(f"吃第{i}个苹果")
#     if i == 3:
#         print(f"吃第{i}个时吃到虫子，不吃了")
#         continue

# for i in  range(5):
#     if i == 3:
#         continue    #可切换 break 尝试结束循环
#     print(i)

# 字符串编码转换
# 转换bytes类型
# a = "hello"
# print(a,type(a))
# a1 =a.encode()
# print("编码后：",a1)
# print(type(a1))
# a2 = a1.decode()
# print(a2,type(a2))

# st = "这就是哈"
# st1 = st.encode("utf-8")
# print(st1,type(st1))
# st2 = st1.decode("utf-8")
# print(st2,type(st2))

# 成员运算符
# in 如果包含则返回 Ture  不包含返回 False
# not in 如果不包含则返回 Ture  包含返回 False
# name ="dingding"
# # print("ing" in name)
# print("c" not in name)

# + 字符串拼接
# print(10+10)
# print("10"+"10")
# n1 = "哈哈"
# n2 = "嘿嘿"
# print(n1 + n2)

# 下标  格式： 字符串名[下标值]
# name="abcde"
# print(name[0])
# print(name[1])
# print(name[-1])

# 切片 语法：[开始位置：结束位置：步长]
# st="abcdefg"
# print(st[0:2])   #ab
# print(st[4:6])   #ef
# print(st[-1:-5:-1])  #gfed  反方向取值，一定要加步长
# print(st[-1::-2])  #geca

# find 查找  格式：find(子字符串，开始位置下标，结束位置下标)  开始/结束位置可以省略
# name="dingding"
# print(name.find("d"))        # 0
# print(name.find("n",3))      #6
# print(name.find("d",3,6))    #4

# count() 返回某个子字符串出现的次数 格式：count（子字符串，开始位置下标，结束位置下标）
# name="dingding"
# print(name.count("d"))      #2
# print(name.count("a"))      #0
# print(name.count("d",1))    #1
# print(name.count("d",1,6))  #1

# startswith(): 判断是否以某个子字符串开头，是则返回ture
# 格式： startswith(子字符串，开始位置下标，结束位置下标)
# str="thisislife"
# print(str.startswith("this"))
# print(str.startswith("is"))
# print(str.startswith("i",2,6))

# endswith(): 判断是否以某个子字符串结尾，是则返回ture
# 格式： endswith(子字符串，开始位置下标，结束位置下标)
# st="thisislife"
# print(st.endswith("e"))

# isupper():检测字符串中所有的字母是否是大写
# st="this is life"
# print(st.isupper())
# print("THIS".isupper())

# while True:
#  st = input("请输入字符(大写字母）：")
#  if st.isupper()==0:
#      print("输入失败，请重新输入！")
#  else:
#       print("输入成功！")
#       break

# 修改元素
# 1. replace（）：替换  格式：replace(旧内容，新内容，替换次数) 替换次数可省略，默认全部替换
# st = "好好学习，天天向上"
# print(st.replace("天","day"))    #好好学习，dayday向上
# print(st.replace("天","day",1))  #好好学习，day天向上

# 2. split():指定分隔符来切字符串
# st = "hello,python"
# print(st.split(","))  #['hello', 'python']
# print(st.split("a"))   #['hello,python']
# print(st.split("o"))   #['hell', ',pyth', 'n']
# print(st.split("o",1))  #['hell', ',python']

# 3. capitalize(): 第一个字符大写，其它字符小写
# st = "dingding"
# print(st.capitalize())     #Dingding

# 4. lower():大写字母转为小写
# st = "dingDing"
# print(st.lower())   #dingding

# 5. upper():小写字母转为大写字母
# st = "DinGdInG"
# print(st.upper())     #DINGDING


# 列表   列表名=[元素1，元素2，元素3...]   元素之间的数据类型可以不相同  可迭代对象
# li = [1,2,"a","c",6]
# # print(type(li))
# # print(li[0:3])
# # 用for进行遍历取值
# for i in li:
#     print(i)

# 添加元素
# append()   extend()  insert()
# li = ["one","two","three"]
# # li.append("four")     # 整体添加
# # li.extend("four")       #['one', 'two', 'three', 'f', 'o', 'u', 'r'] 分散添加
# li.insert(2,"four")       # 在指定位置添加字符，无指定下标会报错
# print(li)

# li = [1,2,3]
# # li.append(4)
# # li.extend(0.4)     #报错，不支持整形
# li.insert(3,4)
# print(li)

# # 修改元素   指定下标，修改该下标的值
# li = [1,2,3]
# li[0] = 'a'
# print(li)


# 查找元素
# in 判断指定元素是否在列表中，是则返回ture
# not in 判断指定元素是否在列表中，不是则返回ture
# li = ["a","b","c","d"]
# print("e" not in li)

# 用户输入名称，名称重复则不能使用，未重复则插入列表
# while True :
#   li = ["MM", "GG", "CC", "DD"]
#   name = input("请输入您的名字：")
#   if name in li:
#     print("名称已被占用，请重新输入")
#   else:
#     li.append(name)
#     print("创建成功！")
#     print(li)
#     break


# index():返回指定数据所在位置的下标，查找不到就报错
# count():统计数据在当前列表出现的次数
# li = ["a","b","c","c"]
# # print(li.index("d"))
# print(li.count("c"))

# del 删除列表
# li = [1,2,3,"a","b","c"]
# # del li                    #删除列表
# del li[3]                   #删除指定下标的元素
# print(li)

# pop：  删除指定下标的数据   默认删除最后一个
# li = [1,2,3,"a","b","c"]
# # li.pop()
# li.pop(3)
# print(li)


# remove: 根据元素的值进行删除  若有相同值，默认删除第一个
# li = [1,2,3,"a","b","c","b"]
# li.remove("b")
# print(li)

# 排序
# sort：将列表按特定顺序重新排列，默认从小到大
# reverse：倒叙，将列表反过来
# li = [8,5,9,7,2,1,6,4,3]
# # li.sort()                #默认从小到大
# li.sort(reverse=True)      #值为True时，从大到小排序。 为False时，从小到大排序
# # li.reverse()
# print(li)


# 列表推导式
# 格式一： [表达式 for 变量 in 列表]

# li = [1,2,3,4,5,6]
# [print(i*5) for i in li]
# [print(i) for i in li]
# li =[]
# # for i in range(1,6):
# #     # print(i)
# #     li.append(i)
# # print(li)
# [li.append(i) for i in range(1,6)]
# print(li)

# 格式二： [表达式 for 变量 in 列表 if 条件]
# 把奇数放进列表里
# li = []
# for i in range(1,10):
#     if i%2 == 1 :
#        # print(i)
#        li.append(i)
# print(li)
# [li.append(i) for i in range(11) if i % 2 ==1]
# print(li)

# li = [i for i in range(11) if i % 2 ==1]
# print(li)


# 列表嵌套
# li = [1,2,3,[4,5,6]]
# print(li[3])    #取出下标为3的数值
# print(li[3][2]) #取出嵌套里的下标为2的数值

# 元祖  格式： 元祖名=（元素1，元素2，元素3....）
# tua = (1,2,3,"a","b","v")
# print(type(tua))
# tua=()
# print(type(tua))
# tua=(1,)
# print(type(tua))

# name = "dingding"
# age = 18
# # print("%s的年龄是%s"%(name,age))
# info = (name,age)
# print(type(info))
# print("%s的年龄是%s" % info)

# 字典
# 格式： 字典名 ={键1：值1，键2：值2，键3：值3...}
# dic = {"name": "dingding","age" : 18}
# print(type(dic))
# dic = {"name":"dingding","name":"cc"}    #重复的值会被后的值覆盖
# dic2 = {"name":"dingding","name2":"cc"}
# print(dic2)

# dic = {"name":"dingding","age":18}
# # print(dic[1])     # 不能通过下标搜索值
# print(dic["name"])

# dic = {"name":"dingding","age":18}
# print(dic.get("name"))
# print(dic.get("age"))
# print(dic.get("tep"))     #不存在则返回none

# 修改元素
# dic = {"name":"dingding","age":18}
# dic["age"] = 20       #字典通过键名修改
# print(dic)

# 添加元素
# 变量名[键名] = 值
# dic = {"name":"dingding","age":18}
# # dic["tel"] = 123456
# dic["tel"] = 12345
# print(dic)


# 删除元素 格式：del 字典名
# dic = {"name":"dingding","age":18}
# # dic["tel"] = 123456
# # del dic["tel"]
# print(dic)

# # 清空字典  clear():清空字典里的元素，保留字典
# dic = {"name":"dingding","age":18}
# dic.clear()
# print(dic)

# pop()  删除指定键值对
# dic = {"name":"dingding","age":18,"tel":123456}
# # dic.pop("age")
# # dic.pop("tel")
# dic.popitem()      # 默认删除最后一个键值对
# print(dic)


# len（）求长度
# dic = {"name":"dingding","age": 18,"tel":123456}
# print(len(dic))              #输出3，字典中有3个键值对
# li = [1,2,3,4]
# print(len(li))
# st = "hello"
# print(len(st))


# .keys()   返回字典里包含的所有键名
# dic = {"name":"dingding","age": 18,"tel":123456}
# print(dic.keys())    #dict_keys(['name', 'age', 'tel'])
#
# #for循环取出键名
# for i in dic:
#     print(i)


# values(): 返回字典中包含的所有值
# dic = {"name":"dingding","age": 18,"tel":123456}
# print(dic.values())           #dict_values(['dingding', 18, 123456])
#
# #for循环取出值
# for i in dic.values():
#     print(i)


# item(): 返回字典里面包含所有键值对，以元祖形式
# dic = {"name":"dingding","age": 18,"tel":123456}
# print(dic.items())   #dict_items([('name', 'dingding'), ('age', 18), ('tel', 123456)])
# #for循环取出值
# for i in dic.items():
#     print(i)


#  set 集合
#  格式： 集合名 ={元素1，元素2，元素3...}
# s1 = {1,2,3}
# s1 = {}              # 空字典
# s1 = set()             #空集合
# print(type(s1))

# 集合具有无序性
# s1 = {8,5,1,9,3,4,6,2}        #数字为有序性
# s2 = {"a","c","f","d","e"}      #字符串，每次运行结果都不一样
# print(s2)

# 集合无序的实现方式涉及 hash表
# print(hash("a"))   #每次运行结果都不同，hash值不同，hash表中位置也不同
# print(hash(1))        #int整形的hash值就是它的本身

# 集合： 添加元素
# add  整体添加
# s1 = {1,2,3}
# print("原集合为：",s1)
# # s1.add((4,5,6))          #一次只能添加一个元素
# # s1.add(4)
# print("现集合为：",s1)      #现集合为： {1, 2, 3, (4, 5, 6)}

# update  把传入的元素拆分，一个个添加
# s1 = {1,2,3,4}
# print("原集合为：",s1)
# # s1.update((5,6,7))
# s1.update("456")          #{1, 2, 3, 4, '4', '6', '5'}
# print("现集合为：",s1)

# 删除元素
# remove:  选择删除的元素， 有则删除，没有就报错
# s1 = {1,2,3,4,5}
# s1.remove(5)
# print(s1)


# pop: 对集合进行无序排序，删除左边第一个元素
# s1 = {5,2,1,3,4}
# s1 = {"c","a","d","b"}
# s1.pop()
# print(s1)

#  discard: 选择要删除的元素，有就删除，没有就不发生改变
# s1 = {"c","a","d","b"}
# s1.discard("a")
# s2 ={1,2,3,4,5}
# s2.discard(3)
# print("删除后：",s2)

# 交集和并集
# 交集 &
# a = {"a","b","c"}
# b = {"c","d","e"}
# a = {1,2,3,4}
# b = {3,4,5,6}
# print(a&b)

# 并集 |
# a = {"a","b","c"}
# b = {"c","d","e"}
# a = {1,2,3}
# b = {4,5,6}
# print(a|b)


# 类型转换
# int（）： 转换为整数，只能由纯数字转换的字符
# float --> int
# a = 1.2
# print(type(a))
# b = int(a)
# print(type(b),b)
# print(int(1.8))

# str-->int
# a = int("123")
# print(a,type(a))
# print(int("bing"))  #报错
# print(int("-10"))

# 通过年龄，判断是否成年
# age = int(input("请输入您的年龄："))
# # print(age,type(age))
# if age >=18:
#     print("成年了")
# else:
#     print("未成年")

# float(): 转换为一个小数
# print(float(11))    #11.0  整形转换为浮点型
# print(float(-11))
# print(float(11.35))

# str(): 转换为字符串类型，任何类型都能转换
# n = 110
# print(type(n))
# n2 = str(n)
# print(n2,type(n2))
# st = str(1.8)
# print(st,type(st))
# li = [1,2,3]
# st = str(li)
# print(st,type(st))

# eval(): 用来执行一个字符串表达式，并返回表达式的值
# print(10+10)
# print(eval("10+10"))
# print(eval("'10+'10"))

# eval() 可以实现list、dict、tuple 和 str之间的转换
# str-->list
# st1 = "[[1,2],[3,4],[5,6]]"
# print(type(st1))
# li = eval(st1)
# print(li,type(li))

# str-->dict
# st2 ="{'name':'dingding','age':18}"
# dic =eval(st2)
# print(dic,type(dic))

# lisr(): 将可迭代的对象转换为列表
# 支持转换为list类型： str、tuple、dict、set
# str ---> list
# print(list('abvdas'))   #['a', 'b', 'v', 'd', 'a', 's']
# print(list("12345"))

# tuple--list
# print(list((1,2,3,4)))   #[1, 2, 3, 4]

# dict ---list
# print(list({'name':'ding','age':18}))    # 字典转换为列表，将键名作为列表的值

# set -->list
# print(list({'a','b','v','v'}))    # 基本转换为列表，会先去重，再转换

# 赋值： 会随着源对象一起
# li = [1,2,3,4]
# # print(li)
# li2 =li      # li赋值给li2
# print('li',li)
# print('li2',li2)
# li.append(5)
# print('添加后的li：',li)
# print('添加后的li2：',li2)
# 赋值： 等于完全共享资源，一个值改变，另外一个值也会被共享


# 浅拷贝（数据半共享）
#  会创建新的对象，拷贝第一层的数据，嵌套层会指向原来的地址
# import  copy   #导入copy模块
# li = [1,2,3,[4,5,6]]    # 定义一个嵌套列表
# li2 = copy.copy(li)     # 浅拷贝
# print("li:",li)
# print("li2:",li2)
# 查看内存地址  id（）
# print('li内存地址：',id(li))
# print('li2内容地址：',id(li2))
# id 不一致，所以不是同个对象
# li.append(8)
# print('li',li)
# print('li2',li2)
# 往嵌套列表添加元素
# li[3].append(7)
# print('li',li)
# print('li2',li2)
# print('li[3]内存地址：',id(li[3]))
# print('li2[3]内容地址：',id(li2[3]))
# # 外层内存地址不同，但内层的内存地址相同


# 深拷贝（数据完全不共享）
# 外层的对象和内部的元素都拷贝了一个遍
# import copy   #导入copy模块
# li = [1,2,3,[4,5,6]]
# li2 = copy.deepcopy(li)
# # print('li:',li,id(li))
# # print('li2:',li2,id(li2))
# li.append(8)
# print(li)
# print(li2)
# # 在嵌套里添加元素
# li[3].append(7)
# print(li)
# print(li2)
# print('li[3]内存地址：',id(li[3]))
# print('li2[3]内容地址：',id(li2[3]))


# 可变类型   变量的值可更改，但内存地址不会变
# li = [1,2,3,4]
# print("li的原内存地址：",li,id(li))
# li.append(5)
# print("li的现内存地址：",li,id(li))

# dic = {'name':'dingding','age':18}
# print(dic,id(dic))
# dic['name'] = 'susu'  #修改元素
# print(dic,id(dic))

# set = {1,2,3,4}
# print(set,id(set))
# set.remove(3)
# print(set,id(set))

# 不可变对象   对应的值不可修改，修改则会生成一个新的值从而匹配一个新的空间
# n = 10                     #整形
# print("现地址：",n,id(n))
# n = 15
# print("修改后",n,id(n))


# st = 'hello'             # 字符串
# print('现地址：',st,id(st))
# st = 'dingdingd'
# print('修改后',st,id(st))


# tua = (1,2,3)            #元祖
# print(tua,id(tua))
# # 不支持新增删除修改操作
# tua = ('a','b','c')
# print(tua,id(tua))


# 函数
# def 函数名（）：
#       函数体
#  调用函数
#   函数名（）
# def login():
#     print("登录函数")
# login()


# 编写一个打招呼的函数 并调用
# def hello():
#     print("你好")
# hello()


# return 返回值
# return 会给函数的执行者返回值
# def buy():
#     # print("珍珠奶茶")
#     return '珍珠奶茶'
#     # return 20
# buy()
# print(buy())
# 程序中遇到return，表示此函数结束

# return 是返回计算值，print是打印值
# def add():
#     a = 1
#     b = 3
#     return a+b
#     print(a+b)
# add()
# # print(add())

# 定义格式：
# def 函数名（形参a，形参b）
#        函数体
#        ....（如a=1，b=2）
#        调用格式:
#         函数名（实参1，实参2）

# def  add(a,b):
#      return a+b
# print(add(2,5))

# 函数参数
# 1.位置参数    传递和定义参数的顺序及个数必须一致
# 格式： def func（a，b）   func为自定义参数名
# def func(name,age,tel):
#     print(name)
#     print(age)
#     print(tel)
# func('dingd',18,123456)


# 2. 默认参数   为参数提供默认值，调用函数时，可不传递该默认参数的值
# 格式： def func(a=12):
# def funb(a=8):
#     print(a)
# funb(100)


# 可变参数 传入的值的数量可以改变，可以传多个，也可以不传
# 格式： def func（*args）
# def funb(*args):
#     print(args)
#     print(type(args))
# funb('派大星')

# 关键字参数
# 格式： def func（**kwargs）
# def func(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
# func()           #空字典
# func(name='bingbing',age=18)    # 传值时，需要采用=值形式
# # 可扩展函数功能


# 函数嵌套
# 嵌套调用 ： 在一个函数里面调用另一个函数
# def stduy():
#     print("好好学习")
# def course():
#     stduy()
#     print("python语言")
# # stduy()
# # course()

# 嵌套定义  在一个函数中定义另外一个函数
# def stduy():
#     print('好好学习')
#     def course():
#         print('python')
#     course()    #注意缩进，定义和调用是同级
# stduy()


# 作用域    ： 指变量生效时的范围
# 全局变量 ： 函数外部定义的变量，在整个文件中都是有效的
# n = 100  #全局变量
# def test1():
#     print("test1的值：",n)
# def test2():
#     n = 20            #局部变量
#     print("test2的值：",n)
# test1()
# test2()

# 局部变量
# def funa():
#     num = 10
#     print("funa中的值：",num)
# funa()
# def funb():
#     num = 2
#     print("funb中的值：",num)
# funb()


# 变量声明为全局变量  global
# a = 100
# def funa():
#     print("funa的值：",a)
# def funb():
#     global a          # 声明
#     # a = 20
#     print("funb的值",a)
# print("调用函数前的值：",a)
# funa()
# funb()

# def study():
#     global name
#     name = 'python'
#     print(f'在学习{name}')
# study()
# # print(name)

# nonlocal  : 声明外层的局部变量，只能在嵌套函数中使用，在外部函数先声明，内部函数nonlocal声明
# a = 10            #全局变量
# def outer():       #外函数
#     a = 5
#     def inner():    #内函数
#         # nonlocal a
#         a = 20
#         # print("inner函数a的值：",a)
#     # print("outer中a的值",a)
#         def inner2():
#              nonlocal a
#              a = 30
#              print("inner2的值：", a)
#         inner2()
#         print("inner函数a的值：", a)
#     inner()
#     print("outter的值：",a)
# outer()


# 匿名函数     函数名 = lambda  形参 ： 返回值（表达式）
#            调用： 结果 = 函数名（实参）

# 普通函数
# def add(a,b):
#     return a+b
# print((add(1,3)))

# 匿名函数
# add = lambda a,b:a+b
# print(add(1,5))

# lambda 参数形式
# func = lambda name,age:(name,age)
# func = lambda name,age=18:(name,age)
# print(func('bing'))
# print(func('dingding',20))
# print(func(18))


# 默认参数
# func = lambda name,age =18:(name,age)
# print(func('bing'))
# print(func('bing',17))

# fune = lambda a,b,c = 12:a+b+c
# print(fune(1,2,4))
# print(fune(1,2))
# 默认参数必须写在非默认参数后面


# 关键字参数
# fund = lambda **kwargs:kwargs
# print(fund(name='bin',age=18))

# # lambada结合if判断
# a = 8
# b = 5
# #格式： 为真结果  if 条件 else 为假结果
# # print('a比b大') if a>b else print('a比b小')
# comp = lambda a,b :'a比b大' if a>b else 'a比b小'
# print(comp(8,5))

# 内置函数
# 查看所有的内置函数
# import builtins
# print(dir(builtins))   # 字母大写一般为内置常亮名，小写字母为内置函数名
# abs（）：返回绝对值
# print(abs(-1))
# print(abs(10))

# sum() 求和
# print(sum([1,2]))
# print(sum({1,3}))

# min():最小值
# max()：最大值
# print(max(1,2,3))
# print(min(1,2,3))
# print(min(-8,5,key=abs))

# # zip():将可迭代对象作为参数，将对象中的元素打包成一个个元祖
# li = [1,2,3]
# li2 = ['a','b','c']
# print(zip(li,li2))
# # 第一种方式： 通过for循环
# for i in zip(li,li2):
#     print(i)
#     print(type(i))
# # 如果元素个数不一致，按照长度最短的返回
# # 第二种： 转换成列表打印
# print(list(zip(li,li2)))
# print(list(zip(li)))

# map():可以对可迭代对象中的每一个元素进行映射，再分别去执行
# map(func,iterl)   func为自定义函数    iterl为可迭代对象
# li = [1,2,3]
# def func(x):
#     return x*5
# mp = map(func,li)
# print(mp)
# # 第一种方式： 通过for循环
# # for i in mp :
# #     print(i)
# # 第二种： 转换成列表打印
# print(list(mp))

# reduce()   先把对象中的两个元素取出，计算出值后保存，再将这值与后面的值计算
# 需要导包
# from functools import reduce
# # reduce(function,sequence) function-函数，必须是2个参数的函数，  sequence-序列，可迭代对象
# li1 = [1,2,3,4]
# def add(x,y):
#     return x+y*2
# res = reduce(add,li1)
# print(res)

# 拆包： 对于函数中的多个返回数据，去掉元祖，列表，字典，直接获取里面的数据
# tua = (1,2,3,4)
# # print(tua)
# # print(tua[0])
# # 方法一：
# a,b,c =tua
# print('a=',a,'b=','b','c=',c)
# 一般获取元素组值的时候使用
# 方法二：
# a,*b = tua
# print(a,b)
# c,*d =b
# print(c,d)
# 一般调用函数的时候使用

# def func(a,b,*args):
#     print(a,b)
#     print(args,type(args))
# func(1,2,3,4,5)
# arg = (1,2,3,4,5)
# func(*arg)

# raise 抛出异常
# raise Exception("狗抛出了个爪")  # 创建一个exception（“xx”）对象  xx--异常信息
# def func():
#     raise Exception("狗抛出了个爪")  # raise抛出这个对象（异常对象）
#     print('我伸手接住了')  # 执行了raise语法，程序不会继续往下运行
# func()
#


# 需求： 密码长度不足，报异常
# def login():
#     pwd=input("请设置你的用户名：")
#     if len(pwd) >= 6:
#         return "设置成功"
#     # else:
#     raise Exception("用户名不足6位")
# # # login()
# # print(login())
#
# try:
#     print(login())
# except Exception as e:
#     print(e)
# print(1234)

# 模块  ： 一个py文件就是一个模块
#  内置模块：random、time、os、loggin，直接导入即可使用
# 第三方模块： 自己在项目中定义的模块（命名遵从规范性，不能与内置模块起冲突，否则无法使用）
# 导入模块：
# import 模块名
# 调用功能：
# 模块名.功能名
# import excp    #导入模块名
# print(excp.name)    # 调用excp模块中的name变量
# excp.funa()         #调用excp模块中的funa（）

# 方法二： form...import
# 语法： 从模块中导入指定的部分
#  form 模块名 import 功能1，功能2...
# 调用功能
# 直接输入功能即可，不需要添加模块名
# from excp import funa
# funa()
# from excp import name
# print(name)

# 方法三： from ...import  *    # 不建议使用过多声明，容易命名起冲突
# 语法： from 模块名 import *
# from excp import *        #把模块中的内容全面导入
# funa()
# funb()
# print(excp.name)


# as 起别名  ： 给模块起别名
# 语法： import 模块名 as 别名
# import excp as py
# py.funb()
# print(py.name)

# as 给功能名起别名
# 语法： from 模块名 import 功能 as 别名
# from excp import funa as a,funb as b,name as c
# a()
# b()
# print(c)

# 内置全局变量  _name_   用来控制不同的应用场景执行不同的逻辑
# 语法：   if  __name__  =="__mian__":
#  __name__
# 1.文件在当前程序执行（自己执行自己）：__name__  =="__mian__":
# 2. 文件被当作模块杯其它文件导入： __name__  ==模块名:
# import exp2
# exp2.test()    # 被当做模块导入时，__name__  =="__mian__":下面的代码不会显示

# 包  ：  项目结构中的文件夹/目录
#  与普通文件夹的区别： 包是含有—__init__.py的文件夹
# 新建包： 右键项目名->new->python Package
# 导入包是，先执行__init__.py的文件代码
# 导入包方式一：
# import pack_01
# 导包方式二：
# from pack_01 import register
# register.reg()

# # _all_:本质上是一个列表，列表里面的元素代表要导入的模块
# from pack_01 import *
# register.reg()
# login.log()

# 递归函数： 一个函数在内部不调用其他函数，而是调用本身的函数，这个函数就是递归函数
# 1. 必须有一个明确的结束条件 ---递归出口
# 2. 没进行更深一层的递归，问题规模相比上次递归都要有所减少
# 3. 相邻两次重复之间有紧密的联系
# 普通函数实现1-100累计和
# def add():
#     s = 0
#     for i in range(1,101):
#         s += i
#     print(s)
# add()

# 递归函数
# def add2(n):    #累计到N项
#     if n==1:       #如果是1，则返回1
#         return 1
#     return n + add2(n-1)    #如果不是1，重复执行累加并返回结果   5+add(4)--add(3) add(2)+1
# print(add2(5))

# # 斐波那契数列
# # 1,1,2,3,5,8,13...
# def funa(n):     #n 代表第N项
#     if n <= 1:
#         return n
#     return funa(n-1)+funa(n-2)
# # print(funa(7))
#
# for i in range(1,8):
#     print(funa(i))

# 闭包
# 条件：
# 1. 函数嵌套（函数里面再定义函数）
# 2. 内层函数使用外层函数的局部变量
# 3. 外层函数的返回值是内层函数的函数名

# def outer():        #定义一个外层函数
#     n = 10          # 外层函数的局部变量
#     def inner():    #定义一个内层函数
#         print(n)    # 调用外层函数的局部变量
#     return inner    # 返回内层函数名
#     # print(outer())
# # outer()()          #  第一种调用写法
#
# ot = outer()         #调用第二总写法
# ot()


# def outer(m):             #外函数，m是形参，外函数的局部变量
#     n = 10
#     def inner():          #内函数
#         print('计算结果：',m+n)
#     return inner          #返回函数名，而不是inner（）
# ot = outer(20)            # 调用函数
# ot()                      #调用内函数

# 函数引用
# def funa():
#     print(123)
# print(funa)            # 函数名里保存了函数所在的位置引用
# # id():  判断两个变量是否是同一个值的引用
# a = 1
# print(a)
# print(id(a))
# a = 2          # 修改a，生成了新的值，重新赋值给a
# print(id(a))
# print(id(2))
# # 内存地址发生变化，因为值夜发生了变量

# def test1():           #test1是一个函数名，存了这个函数的位置引用
#     print('这里是test函数')
# test1()
# print(test1)        #内存地址（引用）
# te = test1
# te()      #通过引用调用函数

# 每次开启内函数都在使用同一份闭包变量
# def outer(m):
#     print("outer中的函数值：",m)
#     def inner(n):
#         print("inner中的函数值：",n)
#         return m+n            #在inner函数中返回m+n的值
#     return inner
# ot = outer(10)                # 调用外函数，给outer（）传值
# ot(20)                        # 调用内函数，给inner（）传值
# print(ot(50))                 #第二次调用

# 装饰器
# def test2():
#     print('发送消息给dd')
# def test(fn):
#     print('开始注册')
#     print('登录')
#     fn()
# test(test2)
# # 作用： 在不改变原有代码情况下添加新的功能
# # 条件： 1. 不修改源程序或函数的代码
# #       2. 不改变函数或程序的调用方法

# def test(fn):          #fn是普通形参
#     print('登录')
#     print('注册')
#     fn()
# def test2():
#     print('发送消息')
# test(test2)

#  装饰器： 装饰器就是闭包函数，不修改原本代码基础上新增其它功能
# 标准装饰器：
# def send():
#     print("发送消息")
# send()

# 闭包条件：
# 1. 函数嵌套
# 2. 内函数要使用外函数的局部变量
# 3. 外函数的返回值是内函数的函数名
# def outer(fn):            #外层函数，fn为形参，往里传入被装饰的函数send（）
#     def inner():          #内函数
#         print("登录..")
#         # 执行被装饰的函数
#         fn()         #这里fn（）为send（）
#     return inner
# print(outer(send))
# ot = outer(send)          #调用外函数
# ot()                      #调用内函数

# 装饰器： 将原有的函数名重新定义为以原函数为参数的闭包

# 语法糖
# 格式：@装饰器名称
# 方式一：
# 函数装饰器的语法：
# def 装饰器函数名（参数）：
#     语句块
#     return 函数对象
# 方式二：
#  @装饰器函数名<换行>
# def 函数名（参数列表）：
#        语句块
#
# def outer(fn):
#     def inner():
#         print("登录微信")
#         fn()
#     return inner
# @outer
# def send():
#     print('发送消息给小白:出来玩吗')
# send()
# @outer
# def send2():
#     print('我们去狗咖吧')
# send2()

# def outer(fn):
#     def inner(name):         #内函数，name是内函数的参数
#         print(f'{name}是inner函数中的参数')
#         print('嘿嘿')
#         fn(name)
#     return inner
# # @outer
# def func(name):
#     print('这是被装饰的函数')
# # func('dd')
# ot = outer(func)
# ot('dd')

# 被装饰的函数有可变参数*args，**kwargs
# 被装饰的函数
# def func(*args,**kwargs):
#     print(args)
#     print(kwargs)
# # func(name='dd')
# # 装饰器函数
# def outer(fn):
#     def inner(*args,**kwargs):
#         print("登录..")
#         fn(*args,**kwargs)
#     return inner
# # print(outer('test'))
# # outer('test')()
# # outer('test')-->inner
# # print(outer(func))
# ot = outer(func)
# ot('dd',name='aa')

# 1.6 多个装饰器
# 第一个装饰器
# def decol(fn):
#     def inner():
#         return '嘿嘿'+fn()+'哈哈'
#     return inner
# # 第二个装饰器
# def decol2(fn):
#     def inner():
#         return '哈喽'+fn()+'你好'
#     return inner
# # 被装饰的函数一：
# @decol
# @decol2
# def test1():
#     return '努力学习'
# print(test1())


# 类与对象
# 类的三要素：
# 1. 类名
# 2. 属性：对象的特征描述，用来说明是什么样子的
# 3. 方法： 对象具有的功能，用来说明能够做什么
# 定义类
# class 类名：
#       代码块
# class login:
#     username = 'DD'
# # 查看类属性：类名.属性名
# print(login.username)
# # 新增类属性：类名.属性名=值
# login.password = 123456
# print(login.password)

# 创建对象：创建对象的过程也叫实例化对象
# 实例化对象的格式：  对象名=类名（）
# 实例化一个登录
# class login:
#     username = 'DD'
# lg = login()
# print(lg)              #显示的对象在内存中的地址
# # 第二次实例化
# lg2 = login()
# print(lg2)
#  内存地址不一样，说明是不同的对象，可以实例化多个对象

# 实例方法：
#  由对象调用，至少有一个self参数，执行实例方法时，自动调用该方法赋值给self
# class login:
#     username = 123    #类属性
#     def lgn(self):
#         print("正在登录中...")
# # 实例化对象
# lg = login()
# # 对象调用类中方法
# lg.lgn()
# lg2 =login()
# print('lg2:',lg)
# lg2.lgn()
# # self代表对象本身，当对象调用实例化方法时，Python会自动将对象本身的引用作为参数，传递到实例方法第一个self参数

# 定义类
# class Person:
#     name = 'dd'
#     def run(self):
#         print('run方法中的self：',self)
#         print('跑步')
# # 实例化对象： 对象名=类名（）
# pe = Person()
# print(pe)
# pe.run()

# 实例属性
# 格式： self.属性名
# class Person:
#     name = 'dd'     #类属性
#     def introduce(self):          #实例方法
#         print("我是实例方法")
#         print(f'{Person.name}的年龄：{self.age},性别为:{self.sex}')   #self.age为实例化属性
# pe = Person()
# pe.age = 18
# pe.sex = '女'
# # print(pe.sex)           # 根据对象名访问实例属性
# # print(Person.sex)     #报错，实例属性只能由对象名访问
# # pe.introduce()
# # 类属性属于类，是公共的，大家都能访问的；实例属性是属于对象的，是私有的
# # 只能由对象名访问，不能由类名访问
# print(Person.name)
# print(pe.name)
# pe2 = Person()
# pe2.sex = '男'
# print(pe2.sex)
# # print(pe2.sex)    #报错，是给pe对象新增实例属性，其他对象不能调用

# 构造函数   __init__()
# 通常用来做属性初始化或者赋值操作
# 注意： 在类实例化对象的时候，会被自动调用
# class Test:
#     def __init__(self):     #self实例方法
#         print('这是__init__()函数')
# te = Test()

class Person:     #类名为 人类
    # def __init__(self):
    #     self.name = 'DD'
    #     self.age = 18
    #     self.hight = 175
    # def play(self):
    #     print(f'{self.name}在打双影奇境')
    # def introduce(self):
    #     print(f'{self.name}的年龄是{self.age},身高为{self.hight}cm')
    def __init__(self,name,age,hight):
        self.name = name
        self.age = age
        self.hight = hight

    def play(self):
        print(f'{self.name}在打双影奇境')

    def introduce(self):
        print(f'{self.name}的年龄是{self.age},身高为{self.hight}cm')

# 实例化对象
# pe = Person()
pe = Person('cc',28,183)
pe.play()
pe.introduce()
# 实例化第二个对象
pe2 = Person('mm',22,165)
pe2.play()
pe2.introduce()
# 实例化第三个对象
pe3 = Person(77,21,165)
pe3.play()
pe3.introduce()

