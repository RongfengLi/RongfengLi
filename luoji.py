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
# student = ("张一","张二","张三","张四","张五","张六","张七","张八","张九","张十") #先把所有人放元组中
# pa = {}   #用来放成绩大于等于60的人  人名+成绩 当然用字典啦
# fi = {}   #用来放成绩小于60的人
# a = 0
# while a < len(student):  #用len()方法获取元组的长度 也就是人数  从而控制输入成绩的循环次数 
#     i = student[a]
#     f = float(input("请输入"+i+"的成绩:"))    #输入每个人的成绩    字符串拼接用 + 
#     if f >= 60:          #判断分数
#         pa[i] = f          #满足条件就新增到字典中
#     else:
#         fi[i] = f
#     a = a + 1
# print("成绩大于等于60的人",pa)
# print("成绩小于60的人",fi)


#for  循环用法   原理是：通过编历来实现的 

#编历
# a = "你好,你真的爱我么?"
# for i in a:
#     print(i)   #把a中的所有字符串都打印了一遍
#同原理可取所有元组 数组 字典里的值

# student = ("张一","张二","张三","张四","张五","张六","张七","张八","张九","张十")
# for i in student:
#     print(i)     #把student 元组中的所有的数据都打印了一遍

#range 数列生成器
#b = range(0,10) #自动生成了一个数列 
# b = list(range(0,10)) #自动生成了一个数列   并转换成数组  左闭右开 生成的0~9  可缩写为range(10)
# print(b)

# for i in range(5):  #相当与直接设置了训练的次数为5
#     print(i)

#range 可设置步长
# b = list(range(0,10,2)) #自动生成了一个数列 步长为2
# print(b)

# for i in range(10):
#     print(i) 

#用for循环来实现while的习题
# student = ("张一","张二","张三","张四","张五","张六","张七","张八","张九","张十") #先把所有人放元组中
# pa = {}   #用来放成绩大于等于60的人  人名+成绩 当然用字典啦
# fi = {}   #用来放成绩小于60的人
# for i in student:  #元组 student 有几个值就循环几次
#     f = float(input("请输入"+i+"的成绩:"))    #输入每个人的成绩    字符串拼接用 + 
#     if f >= 60:          #判断分数
#         pa[i] = f          #满足条件就新增到字典中
#     else:
#         fi[i] = f
# print("成绩大于等于60的人",pa)
# print("成绩小于60的人",fi)

#python 99乘法表

# for i in range(1,10):            #从1到就9 总共循环9次  
#     for j in range(1,i+1):       #控制每次大循环时小循环的次数 例如当I循环到3时 对应I就要循环3次(1,4)就是三次  
#         print(i,"x",j,"=",i*j,end="  ")   #这里end主要是用来控制不换行,并且结果之之间可以设置内容  
#     print()                              #这个空的print里面没有end 这样第一个for循环结束之后就会换行了
#
#反过来
# for i in range(9,0,-1):
#     for j in range(1,i+1):
#         print(i,"x",j,"=",i*j,end="  ") 
#     print()

#练习1：
#模拟一个红绿灯功能 注意:红灯30次 黄灯3次 绿灯35次  

# light = {"红灯":30,"绿灯":35,"黄灯":3}
# while True:                                   #搞个死循环一直倒计时
#     for i in light:
#         for j in range(light[i]):
#             print(i+"倒计时还有",light[i]-j,"秒")

# #练习2:
# #实现一个注册功能  用户名  密码    用户名必须5~8位  密码必须6~12位  并且账号必须小写开头

username = input("请输入5~8位首字母小写的用户名:")
password = input("请输入6~12位的密码:")
file = {}
if len(username) >= 5 and len(username)<= 8:
    if username [0] in "qwertyuiopasdfghjklzxcvbnm":
        if len(password) >=8 and len(password) <= 12:
            file["username"] = username
            file["password"] = password
            print("注册成功")
        else:
            print("密码长度不对")
    else:
        print("账号必须小写字母开头")        
else:
    print("用户名长度不对")

