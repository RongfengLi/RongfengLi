# print("hello world!") #字符串
# print(23321)   #整数
# print(1.21021)  #小数
# print(True)   #布尔值   true false
# print(())  #元组
# print([])  #数组
# print({})  #字典
# print("哈 哈",1515,1.24)
# print("哈哈"+"嘻嘻") # 字符串的拼接  只能同类型的进行拼接  
# print("哈哈"*5)    # 输出5遍
# print(1+2*5-10+(55.5))
# print(2>3)
# a = "张绍"   #变量必须是小写字母
# print(a)
# a = input("请输入a的值")  #只要是通过input获取的都是字符串
# b = input("请输入b的值")  #只要是通过input获取的都是字符串
# print("a+b=",a+b)
# 数据格式的转换
# print(type(2333))
# print(type(2.33))
# print(type("哈哈"))
# print(type(True))
# print(type(()))
# print(type([]))
# print(type({}))
# a = str(2333)
# print(type(a))  #数据转换的规律 任何数据都可以转换为字符串
# #数据转换的规律 任何数据都可以转换为字符串除了None
# #整数和小数可以互相转换
# #字符串转换为其它类型的数据 需要满足一个规律 "长得像"  

# a = float(input("请输入a的值"))  #只要是通过input获取的都是字符串
# b = float(input("请输入b的值"))  #只要是通过input获取的都是字符串
# print("a+b=",a+b)

#len() 计算 字符串 元组 数组 字典的长度
# a = input("请输入a的值")
# b = input("请输入b的值")
# print("字符串a+b=",len(a)+len(b))
# print("修改了代码")

#元组
a = () #空元组
b = (1,2,3,"哈哈",True,False,"哈哈")
# print(b) #输出所有元组的内容
# #元组的下标(从0开始编号的)
# print(b[3])  #输出元组b中下标为3的值
# print(b[-1]) #输出倒数第一个值
# print(b.index("哈哈")) #查找元组b中哈哈的下标值 并打印出来  如果出现重复值 输出的是从左往右第一个值的下标 只能操作一维元组
# print(b.count(True)) #查找元组中一共有几个1 并输出     Ture = 0    False=1   只能操作一维元组
#二维元组   元组里面有元组
c = (b,"嘻嘻",4,5,6)  
print(c[0][3])  #取数组c中数组b的第3个值  取二维元组的值方式就是[值的位置][值的位置]