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

age = int(input("请输入你的年龄:"))
if age >= 18 and age <= 30:
    print("你已经成年了")
elif age > 30 and age <= 60:
    print("你已经要成家了")
elif age > 60:
    print("你已经老了")
else:
    print("好好学习天天向上")

