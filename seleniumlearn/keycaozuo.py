from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys  #导入键盘操作的包



driver = webdriver.Chrome(executable_path="./chromedriver.exe")
url = "https://demo.10x1000.org/"    

#进入10x1000首页
driver.get(url)
driver.maximize_window()        
driver.implicitly_wait(2)


#跳转到注册页
driver.find_elements_by_class_name('mobile-move')[1].click()   

#输入用户名密码进行登入
driver.find_element_by_css_selector('[placeholder="Please enter your email."]').send_keys("ym771221560@163.com")
driver.find_elements_by_class_name('el-input__inner')[1].send_keys("q12345678")
driver.find_elements_by_class_name('el-input__inner')[1].send_keys(Keys.CONTROL,"a")
driver.find_elements_by_class_name('el-input__inner')[1].send_keys(Keys.CONTROL,"c")
driver.find_elements_by_class_name('el-input__inner')[2].send_keys(Keys.CONTROL,"v")
time.sleep(3)
driver.quit()