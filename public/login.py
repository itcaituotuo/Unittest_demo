# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/16 21:38

from selenium import webdriver
import time


class Login:
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        """ 封装云商登录"""
        self.driver.find_element_by_xpath('//div[@class="login"]/a[1]').click()
        time.sleep(2)
        self.driver.find_element_by_id("text").send_keys("15059224492")
        time.sleep(1)
        self.driver.find_element_by_id("password").send_keys("123456")
        time.sleep(1)
        self.driver.find_element_by_class_name("submit_login").click()
        time.sleep(3)
