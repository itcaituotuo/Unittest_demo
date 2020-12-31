# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/23 14:13

import time


class AppLogin(object):
    def __init__(self, driver):
        self.driver = driver

    def login(self, phone, password):
        """
        封装账号密码登录方法
        @param phone: 手机号
        @param password: 密码
        """
        time.sleep(8)
        self.driver.implicitly_wait(60)  # 添加隐式等待时间60s
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tvConfirmWithBg").click()  # 青少年提示->点击我知道了
        time.sleep(2)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/me_item").click()  # 点击我的，进入我的模块
        time.sleep(2)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tv_notLogin_goLogin").click()  # 点击立即登录
        time.sleep(2)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/login_mode").click()  # 选择密码登录
        time.sleep(2)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/phone_num_edit").send_keys(phone)  # 输入账号
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/code_edit").send_keys(password)  # 输入密码
        time.sleep(1)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/login").click()  # 点击登录
        time.sleep(3)

    def login_out(self):
        """退出当前账号"""
        # 点击我的，进入我的模块
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/me_item").click()
        time.sleep(2)
        # 点击设置按钮
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/setting").click()
        time.sleep(2)
        # 手势上滑，至页面最底部
        self.driver.swipe(400, 700, 400, 400)
        time.sleep(2)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tvLogout").click()
        # 点击确认
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/bt_positive").click()
        time.sleep(2)

    def sign(self, content):
        """
        修改个性签名
        @param content: 签名内容
        @return:
        """
        # 调用login()方法，登录
        AppLogin(self.driver).login("15127409611", "a123456")
        # 点击用户名，跳转至空间页面
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/member_name").click()
        self.driver.implicitly_wait(30)
        # 点击编辑资料
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/btn_edit_info").click()
        self.driver.implicitly_wait(30)
        # 点击个性签名框
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tvSignOrLoginTips").click()
        time.sleep(2)
        # 定位编辑框
        ele_edit = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/etInput")
        ele_edit.click()
        ele_edit.clear()
        time.sleep(2)
        ele_edit.send_keys(content)
        time.sleep(2)
        # 点击保存
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/bnNext").click()

    def search(self, content):
        """
        搜索功能
        @param content: 搜索内容
        @return:
        """
        # 点击最右按钮，切换至首页
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
        time.sleep(3)

        # 点击搜索按钮，进入搜索页面
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/ic_search_b").click()
        time.sleep(2)
        ele_input = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/search_input")
        ele_input.click()
        ele_input.send_keys(content)
        time.sleep(5)
