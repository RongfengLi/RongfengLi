from selenium import webdriver
import time


#创建Webdriver对象
#如果把游览器的驱动放置到了环境变量中则可不带参数
#driver = webdriver.Chrome()

#如果没放到环境变量中则要参数指定   设置环境变量的目的就是任意时候都可以直接使用文件
driver = webdriver.Chrome(executable_path="./chromedriver.exe")
url = "https://www.huya.com/l"


driver.get(url)
driver.maximize_window()       
time.sleep(3)


driver.execute_script("window.scrollTo(0,10000)")
time.sleep(3)


driver.find_element_by_xpath('//a[@class="laypage_next"]').click()
