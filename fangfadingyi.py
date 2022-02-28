#方法/函数的定义

#自动判断账号的长度未5~8位 并且账号是小写开头

# def checkcount(username):  
#     '''自动判断账号的长度未5~8位 并且账号是小写开头'''   #方法的备注说明 鼠标悬浮方法后会限制该备注 
#     if len(username) >= 5 and len(username)<= 8:  #def方法的声明 checkname方法的名字 username方法的参数
#         if username [0] in "qwertyuiopasdfghjklzxcvbnm":    #里面的是方法的逻辑代码
#             print("账号格式正确")
#         else:
#             print("账号必须小写字母开头")        
#     else:
#         print("用户名长度不对")  

#——————————————————————————
#输入方法名称+参数调用方法
# a = input("输入账号名称:")
# checkcount(a)

#写个2个数据相加的方法

# def qiuhe(a,b,c):   #括号里面放参数
#     '''
#     这个方法的作用是实现3个数字相加
#     '''
#     if type(a) is int and type(b) is int and type(c) is int: #判断类型
#         return a+b+c          #return返回的值可以做其它操作  print不行
#     else:
#         return "输入的数据类型不正确"  

# # c = []
# # print(c.append("哈哈"))  #输出结果返回值为None  是因为append 方法无返回值

# print(qiuhe(3,5,7))   #返回值返回后我们可以对这个值做其它操作

# 把之前登入判断的作业写成方法

# def signin(username,password):
#     file = {}
#     if len(username) >= 5 and len(username)<= 8:
#         if username [0] in "qwertyuiopasdfghjklzxcvbnm":   #判断首字符是否再26个小写字母里面
#             if len(password) >=8 and len(password) <= 12:
#                 file["username"] = username
#                 file["password"] = password
#                 print("注册成功")
#                 return True
#             else:
#                 print("密码长度不对")
#         else:
#             print("账号必须小写字母开头")        
#     else:
#         print("用户名长度不对")

# username = input("请输入你的姓名:")
# password = input("请输入你的密码:")
# signin(username,password)





#try + except 异常捕获   可用于自动化脚本断言
try:
    print("a"+y)
except:
    print("上面的代码写错了")

try:
    print(a*b)
except Exception as e:   #Exception 就是把报错信息赋值给变量e并打印出来
    print("上面的代码写错了",e)

#报错信息就是从异常类来的
# 包》类》方法》变量


