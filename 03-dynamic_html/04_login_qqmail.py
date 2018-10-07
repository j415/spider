# author:aspiring

import time
from selenium import webdriver

# 实例化一个浏览器
driver = webdriver.Chrome()
driver.get("http://mail.qq.com/")

# 切换到iframe
driver.switch_to.frame("login_frame")

driver.find_element_by_id("u").send_keys("123123123")

time.sleep(5)

driver.quit()