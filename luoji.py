# 判断

# a = 1
# b = 2
# if a > b:   #先if  if背后根条件  条件背后一定要冒号结束 并换行 换行后缩进 缩进后代表代码块
#     print("a大于b") #这是一个代码块  
# else:
#     print("a小于b") #这是一个代码块

# if a == 1:
#     print("a等于1")

# if b != 1:
#     print("b不等于1")

#多个条件的判断  elif  否则如果  从上往下判断 满足判断后不在往下执行

# age = int(input("请输入你的年龄:"))
# if age > 60:
#     print("你已经老了")
# elif age > 30:
#     print("你已经要成家了")
# elif age > 18:
#     print("你已经成年了")
# else:
#     print("好好学习天天向上")

# age = int(input("请输入你的年龄:"))
# if age >= 18 and age <= 30:    #if 的判断条件有 == !=  <   >   <=  >=  in  is  not in  not is  条件之间可以用and  or  
#     print("你已经成年了")
# elif age > 30 and age <= 60:
#     print("你已经要成家了")
# elif age > 60:
#     print("你已经老了")
# else:
#     print("好好学习天天向上")

#in 的写法
# a = "我"
# b = ["你","我","他"]
# if a in "你是谁":   #如果 我 在  "你是谁"里面那就符合条件 
#     print("我")
# elif a in b:        #判断数组b中有没有a的内容
#     print("我")
#-------------------------------
# a = input("请输入数字:")
# if a == "":
#     print("不能为空!")  #加了一个不能为空的判断
#     exit()
# if a in "0123456789":
#     a = int(a)
#     print(a)
# else:
#     a = input("请重新输入数字")
#     exit()
# if a > 5:
#     print("大")
# else:
#     print("小")



#is 的用法   可用用来判断某个变量的类型
# a = 10
# if type(a) is int:
#     print("a是整数")
# elif type(a) is str:
#     print("a是字符串")
# else:
#    print("其它")

#if的写法只有
'''if
   if else
   if  elif else '''


#--------------------------


#循环

#while  循环用法
# a = 1
# while a < 10:
#     print("a小于10",a)  #直接这个写是一个死循环 因为a 永远小于10   Ctrl + C  可跳出死循环
#     a = a + 1        # a的数值在累计增加 就不会陷入死循环

'''
练习：
现在有10个学生的成绩需要录入到系统中
这10个人分别是 张一 张二 张三 张四 张五 张六 张七 张八 张九 张十
并且名字和成绩的需要对应上
而且大于等于60 和小于60的要分开存放
'''
student = ("张一","张二","张三","张四","张五","张六","张七","张八","张九","张十") #先把所有人放元组中
pa = {}   #用来放成绩大于等于60的人  人名+成绩 当然用字典啦
fi = {}   #用来放成绩小于60的人
a = 0
while a < len(student):  #用len()方法获取元组的长度 也就是人数  从而控制输入成绩的循环次数 
    i = student[a]
    f = float(input("请输入"+i+"的成绩:"))    #输入每个人的成绩    字符串拼接用 + 
    if f >= 60:          #判断分数
        pa[i] = f          #满足条件就新增到字典中
    else:
        fi[i] = f
    a = a + 1
print("成绩大于等于60的人",pa)
print("成绩小于60的人",fi)



