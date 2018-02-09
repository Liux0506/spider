# -*- coding: utf-8 -*-
# @Time    : 2018/2/5 16:59
# @Author  : Liunux
# @Email   : 103996977@qq.com
# @File    : test.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
start_urls=["http://www.qichacha.com/user_login"]
driver = webdriver.Chrome(executable_path="D:/_Liunux/study/python/chromedriver.exe")
driver.get(start_urls[0])
time.sleep(3)
loginText = driver.find_element_by_id("nameNormal")
loginText.clear()
loginText.send_keys("13302330150")
pwdText = driver.find_element_by_id("pwdNormal")
pwdText.clear()
pwdText.send_keys("mima=520124")
verifyElement = driver.find_element_by_id("nc_1_n1z")
ActionChains(driver).drag_and_drop_by_offset(verifyElement, 348,30).perform()
time.sleep(5)   ##一定要等待，否则点击动作识别手动验证码的提交
loginBtn = driver.find_element_by_xpath('//*[@id="user_login_normal"]/button')
loginBtn.click()
cookie=driver.get_cookies()
print (cookie)
time.sleep(10)
driver.quit()