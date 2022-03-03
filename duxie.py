#Python常用的方法——文件的读写



#写——————————————————————————
#from email.utils import localtime    #导入localtime
# a = localtime()  #获取当前时间  格式固定
# print(a)

import time   #导入时间包

now = time.strftime("%y-%m-%d %H:%M:%S") #获取当前时间    "%y-%m-%d %h:%m:%s" 设置日期格式 年月日小写 时分秒大写
print(now)
name = input("输入姓名:")
sex = input("输入性别:")         
with open ("D:\workhome\Test\用户信息.txt","a",encoding="utf8") as f:   #存放路径+"用户信息.txt"文件名 "w"写入 "a"追加 encoding="utf8"设置文件的编码方式
    f.write(now+"\n")
    f.write(name+"\t")    #字符串拼接用 +   /n 实现换行
    f.write(sex+"\n")          #字符串拼接用 +   /n 实现换行
    f.write("------------------------\n")
    #Python存放的文件夹名称不要t n开头  不然路径显示的时候变成\n \t就会报错
# Python的制表符  \t    \n 换行
# 把Python文件直接放在 Python文件夹环境变量中  即可在cmd命令中 输入文件名直接运行



#读——————————————————————————
with open ("D:\workhome\Test\用户信息.txt","r",encoding="utf8") as f:  #"r"读
    text = f.readlines()              # readlines() 这个方法是读取全部
    print(text)  #直接打印出来显示的是数组 
for i in text:
    print(i)       #所以需要遍历一下循环逐个打印数组的内容