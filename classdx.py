#类的实现
'''
class 声明类的名字  类的名字首字母必须大写
面向对象编程
类里面所有的方法必须传一个参数  
类的特点 继承  重写/多态  
'''

# class Airdengfahuan():
#     def __init__(self,Level,sex,hong,lan,lv):  #里面所有的方法必须传一个参数 self    __init__基本属性
#        self.Level = Level   #对应方法参数里的值
#        self.sex = sex           
#        self.hong = hong
#        self.lan = lan
#        self.lv = lv
    
#     def zhiye(self,num):   #类里面方法的第一个参数必须固定写self    职业
#         print("你的等级为:"+self.Level+"血量:"+self.hong+"蓝量:"+self.lan+"体力值:"+self.lv+"选择了:")
#         if num == 1:
#             print("魔剑士")
#         elif num == 2:
#             print("法爷")
#         else:
#             print("猎龙骑士")
    
#     def zhuangbei(self,wuqi):  # 装备
#         print(wuqi)
    
#     def work(self):     #工作目标
#         print("获得艾尔登法环登上王座")


#类的实例化
# Shanks = Airdengfahuan()  #类的实例化将类赋值给一个变量
# Lufei = Airdengfahuan()
# Shanks.zhiye(1)           #赋值后通过变量.方法名 可以调用类里面的方法
# Shanks.work()             #赋值后通过变量.方法名 可以调用类里面的方法
# print(Shanks.Level)       #可通过变量.属性 说去类的基本属性
# Shanks.zhiye(1)

# baihuzi = Airdengfahuan("54","女","520","120","20")  #给类里面__init__这个方法下变量赋值
# baihuzi.zhiye(2)
# baihuzi.zhuangbei("月影刀")   #给实例化后用变量名+类里面方法的名称+参数 实现方法的调用

# class Car():  #看似什么也没继承实际继承了 object 这个类是默认存在的最大的一个类
#     def __init__(self,pingpai,yanse,neishi,chexing):
#         self.pingpai = pingpai
#         self.yanse = yanse
#         self.neishi = neishi
#         self.chexing = chexing

#     def gongneng(self):
#         print("百米加速4.3s")
    
#     def youhao(self):
#         print("5.8L/100KM")

# Mycar = Car("奔驰","碳黑","豪华","G500")
# Mycar.gongneng()


#类的继承   子类继承父类 同时继承父类的所有方法

# class Newcar(Car):   #Newcar（子类） 继承 Car(父类)
    
#     def gongneng(self):    #重写父类Car里面的方法 即为重写
#         print("3.2s")

# Mynewcar = Newcar("宝马","碳黑","豪华","780")
# Mynewcar.gongneng()
