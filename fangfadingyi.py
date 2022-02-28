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

def qiuhe(a,b,c):
    '''
    这个方法的作用是实现3个数字相加
    '''
    if type(a) is int and type(b) is int and type(c) is int: #判断类型
        return a+b+c
    else:
        return "输入的数据类型不正确"

# c = []
# print(c.append("哈哈"))  #输出结果返回值为None  是因为append 方法无返回值

print(qiuhe(3,5,7))   #返回值返回后我们可以对这个值做其它操作


