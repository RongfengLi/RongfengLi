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


#--------------------------------


#元组
# a = () #空元组
# b = (1,2,3,"哈哈",True,False,"哈哈")
# print(b) #输出所有元组的内容
# #元组的下标(从0开始编号的)
# print(b[3])  #输出元组b中下标为3的值
# print(b[-1]) #输出倒数第一个值
# print(b.index("哈哈")) #查找元组b中哈哈的下标值 并打印出来  如果出现重复值 输出的是从左往右第一个值的下标 只能操作一维元组
# print(b.count(True)) #查找元组中一共有几个1 并输出     Ture = 1    False=0   只能操作一维元组
#二维元组   元组里面有元组
# c = (b,"嘻嘻",4,5,6)  
# print(c[0][3])  #取数组c中数组b的第3个值  取二维元组的值方式就是[值的位置][值的位置]
# print(c[0][2],c[1])

#切片
# print(b[0:4]) #取 元组b下标0到下标3的值    左闭右开
# print(c[0:2])
# print(b[3:])   #取3到最后
# print(b[:3])   #取开始到2 


#--------------------------------

#数组          
# a = [1,2,3,"哈哈",True,False,"哈哈"] #套娃、下标取值和元组一致  
#元组一旦写好后不可以修改，而数组是可以修改的
# a.append("添加1")   # append 往数组里添加新数据 默认添加在最后  只能装一个
# a.append("添加2")
# a.insert(3,4)       # insert 在对应下标3的值的前面插入新的数据4
# print(a)
# a.pop(2)               # pop 剪切  把数组的值拿到别的地方去用
# print(a)               # 取完之后打印数组a 下标为2的数据就不见了 
# b = a.pop(2)           # 剪切最新的元组a中下标为2的数据并赋值给变量b
# c = a.pop(1)
# print(a)
# d = a[0]
# print(b+c+d)
#a.clear()              #清空数组
# i = ["extend01","extend02"]   
# a.extend(i)            # extend是合并数组的作用 用的也比较少  通过 + 也可以合并数组
# print(a)
# j = a
# print(j+i)             # 打印出数组 j + i 一起的值   
# o = i+a                # 变量o 等于数组 i + a  也成了一个数组是数组i+a的合集
# print(o)
# a.remove("哈哈")       # remove 是移除数组中的数据
# print(a)
#在操作数组和元组时下标不要超出范围  否则视为越界 
#所有的方法都是小括号结尾
#元组数组字典的取值都是用中括号比如 a[0]

#--------------------------------

#字典
'''字典的特点
1.字典中的值没有顺序
2.字典的结构必须是 键值对    key:value
3.字段的取值是通过Key去取value
'''
# a = {"name":"张三"}  #key是name valve是张三
# b = {"name":"李四","sex":"男","age":"23"}
# print(a,b)          #字典不能相加
# print(b["name"])    #字典的取值不是输入下标 是通过Key取valve 
#新增
# b["high"] = "178cm"  #新增值使用中括号
# print([b])
#修改
# b["name"] = "赵云"   #输入已有的key 赋予新的Value
# print([b])
#get 取值  pop剪切走
# d = b.get("name")    #变量d 取字典b中的name的value值
# print(d)
# e = b.pop("name")
# print(b)
# print(e)
#修改 update  添加  和上面新增的效果一致  如果Key存在那就修改如果不存在那就新增
# b.update(age=26)
# b.update(name="司马懿")  #这里的name相当于变量 所以不需要加引号
# print(b)
#删除   数字和字段才可以删除  del是通用的删除方法
# del b["name"]     #删除字典中key是name的值
# print(b)
# f = [1,2,3,4,5,6]
# del f[2]           #删除数组中下标为2的值
# print(f,f.index(2))

#联系 获取用户的个人信息 姓名 性别 年龄并存储到字典中 

方法一 
# a = input("请输入你的姓名:")
# b = input("请输入你的性别:")
# c = int(input("请输入你的年龄:"))
# d = {}
# d.update(name=a,sex=b,age=c)
# print(d)

方法二
# d = {"name":input("请输入你的姓名:"),"sex":input("请输入你的性别:"),"age":input("请输入你的年龄:")}
# print(d)
