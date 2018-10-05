# author:aspiring


from selenium import webdriver
import time

chromedriver_path = "C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe"
driver = webdriver.Chrome(chromedriver_path)

driver.get("https://www.bilibili.com/v/kichiku/mad/#/all/stow")


print(driver.find_element_by_xpath("//ul[@class='vd-list mod-2']/li//a[@class='title']").text)

for i in range(10):
    # 翻页
    driver.find_element_by_xpath("//button[@class='nav-btn iconfont icon-arrowdown3']").click()

    time.sleep(1)

    print(driver.find_element_by_xpath("//ul[@class='vd-list mod-2']/li//a[@class='title']").text)



driver.quit()