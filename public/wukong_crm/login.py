# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/17 19:40

import time


class Login:
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        """ 封装悟空CRM登录"""
        # 输入用户名15059224492
        self.driver.find_element_by_name("username").send_keys("15059224492")
        # 输入密码123456
        self.driver.find_element_by_name("password").send_keys("123456")
        self.driver.implicitly_wait(10)
        # 点击登录
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[4]/div/button').click()
        time.sleep(5)
