from argparse import Action
from threading import activeCount
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time


driver = webdriver.Chrome(executable_path="./chromedriver.exe")
url = "https://demo.10x1000.org/"    

#进入10x1000首页
driver.get(url)
driver.maximize_window()        
driver.implicitly_wait(2)


#跳转到登入页
driver.find_elements_by_class_name('mobile-move')[0].click()   

#输入用户名密码进行登入
driver.find_element_by_css_selector('[placeholder="Please enter your email."]').send_keys("ym771221560@163.com")
driver.find_element_by_css_selector('[placeholder="Please enter your password."]').send_keys("q12345678")
driver.find_element_by_xpath('*//main//div[4]//input').click()
driver.implicitly_wait(5)


#鼠标悬停头像
action = ActionChains(driver)
action.move_to_element(driver.find_element_by_xpath('//img[@class=" el-dropdown-selfdefine"]'))
#事件的操作必须要执行
action.perform()

#选择退出按钮
driver.find_element_by_xpath('//li[@class="el-dropdown-menu__item"]').click()
time.sleep(5)

#关闭游览器
driver.quit()




