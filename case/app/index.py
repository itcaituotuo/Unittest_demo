# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/23 13:55

import os
import unittest
import time
from public.zuiyou_app.public_login import AppLogin
from appium import webdriver

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class AndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['noReset'] = 'False'
        # desired_caps['app'] = PATH('D:\Desktop\Testman_Study\apk\zuiyou518.apk')
        # desired_caps['app'] = r'D:\Desktop\Testman_Study\apk\zuiyou518.apk'
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboard'] = 'True'
        desired_caps['appPackage'] = 'cn.xiaochuankeji.tieba'
        desired_caps['appActivity'] = '.ui.base.SplashActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_index_01(self):
        """ZY005_验证首页导航栏文案显示是否正常"""
        time.sleep(8)
        # 青少年提示->点击我知道了
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tvConfirmWithBg").click()
        # 点击最右按钮，切换至首页
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
        time.sleep(6)
        ele = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/title")
        for i in range(0, len(ele)):
            print(ele[i].text, end=" ")  # 关注 推荐 视频 图文
        self.assertEqual(ele[0].text, "关注")
        self.assertEqual(ele[1].text, "推荐")
        self.assertEqual(ele[2].text, "视频")
        self.assertEqual(ele[3].text, "图文")

    def test_index_02(self):
        """ZY006_验证帖子列表内容跳转"""
        time.sleep(8)
        self.driver.implicitly_wait(60)
        # 青少年提示->点击我知道了
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tvConfirmWithBg").click()
        # 定位还没跳转至详情页面时的帖子信息
        a = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/expand_content_view")
        # 将帖子信息内容赋值给b
        b = a.text
        # 点击跳转到帖子详情页面
        a.click()
        time.sleep(3)
        # 详情页面的标题
        detail_text = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tvTitle")
        c = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tvPostContent")
        self.assertEqual("帖子详情", detail_text.text)
        # b的值与详情页面的帖子内容比较是否一致
        self.assertEqual(b, c.text)

    def test_index_03(self):
        """ZY007_验证评论帖子功能"""
        AppLogin(self.driver).login("15127409611", "a123456")
        time.sleep(3)
        # 点击最右，进入首页
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/iconTabItem").click()
        time.sleep(6)
        # 定位第一条帖子
        self.driver.find_element_by_id('cn.xiaochuankeji.tieba:id/expand_content_view').click()
        time.sleep(3)
        self.driver.find_element_by_id('cn.xiaochuankeji.tieba:id/etInput').send_keys("123456")
        # 点击发送
        self.driver.find_element_by_id('cn.xiaochuankeji.tieba:id/send').click()
        time.sleep(3)

        # 断言结果
        # 获取所有评论，通过循环，放入列表，再转换成字符串
        sendContent = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/expandTextView")
        sendContentRawList = []
        for i in range(0, len(sendContent)):
            sendContentRawList.append(sendContent[i].text)
        sendContentList = "".join(sendContentRawList)
        self.assertIn("123456", sendContentList)


if __name__ == "__main__":
    unittest.main()
