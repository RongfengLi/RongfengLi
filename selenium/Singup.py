from selenium import webdriver
import time


#创建Webdriver对象
#如果把游览器的驱动放置到了环境变量中则可不带参数
#driver = webdriver.Chrome()

#如果没放到环境变量中则要参数指定   设置环境变量的目的就是任意时候都可以直接使用文件
driver = webdriver.Chrome(executable_path="./chromedriver.exe")
url = "https://demo.10x1000.org/"    #把测试地址放到一个变量中  直接get这个变量   

#使用游览器打开指定页面
driver.get(url)                 #如果上面没设置变量也可以这么写  driver.get("https://demo.10x1000.org/")
driver.maximize_window()        #游览器全屏
time.sleep(1)                   

#模拟新用户注册路径的操作
#查找 元素  跳转到登入页
#driver.find_element_by_xpath('//body//div//div[@class="person-logo"]//a[text()="Sign In"]').click()   #通过xpath定位元素

driver.find_elements_by_class_name('mobile-move')[1].click()  # 当Class name重复了 根据顺序位置定位
time.sleep(1)                   


#查找 元素  跳转到注册页   
driver.implicitly_wait(5)                               #隐示等待5秒
driver.find_element_by_class_name('sign-up').click()    #通过Class_name定位元素  这里发现name是唯一的所以没有用elements
              


#注册 账号 密码  确认密码  
driver.find_element_by_css_selector('[placeholder="Please enter your email."]').send_keys("jiaoben@163.com")
driver.find_elements_by_class_name('el-input__inner')[1].send_keys("q12345678")
driver.find_elements_by_class_name('el-input__inner')[2].send_keys("q12345678")
time.sleep(2)


#点击注册信息提交
driver.find_element_by_class_name('submit').click()

#断言是否注册成功



#关闭游览器  回收资源
#driver.quit() 


