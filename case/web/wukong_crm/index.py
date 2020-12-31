# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/17 19:43

# Unittest_demo\case\web\wukong_crm\index.py
# 悟空CRM系统 首页相关的测试用例

from selenium import webdriver
import unittest
import os
import time

from public.wukong_crm.login import Login


class TestIndex(unittest.TestCase):
    def setUp(self):
        """ setUp方法，初始化 最先执行，每次都会打开页面 """
        self.driver = webdriver.Chrome()
        # 打开悟空CRM系统
        self.driver.get("http://101.133.169.100:8088/")
        self.driver.maximize_window()
        time.sleep(3)

        # 打印用例开始执行的时间
        print("start_time:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))

    def tearDown(self):
        """  最后执行，每次执行完成都会截图 """
        file_dir = "D:/Desktop/Testman_Study/图库/screen/"
        # 如果找不到文件夹，则新建一个文件夹
        if not os.path.exists(file_dir):
            os.makedirs(os.path.join("D:/", "Desktop", "Testman_Study", "图库", "screen"))
        # 打印执行完成的时间
        print("end_time:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))
        # 截图命名以时间戳命名
        screen_name = file_dir + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"
        self.driver.get_screenshot_as_file(screen_name)
        self.driver.quit()

    def testIndex01_01(self):
        """WKCRM_001. 验证导航文案是否显示正常"""

        # 调用login方法，登录悟空CRM系统
        Login(self.driver).login()

        # 获取导航栏各个控件的文本信息
        # 办公
        text_bg = self.driver.find_element_by_xpath('//a[@class="nav-item router-link-active"]/div').text
        # 客户管理
        text_khgl = self.driver.find_element_by_xpath('//*[@id="app"]/section/header/div/div/div/a[2]/div').text
        # 商业智能
        text_syzn = self.driver.find_element_by_xpath('//*[@id="app"]/section/header/div/div/div/a[3]/div').text
        # 项目管理
        text_xmgl = self.driver.find_element_by_xpath('//*[@id="app"]/section/header/div/div/div/a[4]/div').text
        # 开通授权
        text_ktsq = self.driver.find_element_by_xpath('//*[@id="app"]/section/header/div/span[1]/button').text
        # 带有用户名的头像
        text_tx = self.driver.find_element_by_xpath(
            '//*[@id="app"]/section/header/div/span[2]/div[2]/div/div/div/div').text

        # 断言结果，进行文本信息的比对

        # 断言方法一：assertEqual、assertNotEqual
        self.assertEqual('办公', text_bg)
        self.assertEqual('客户管理', text_khgl)
        self.assertEqual('商业智能', text_syzn)
        self.assertEqual('项目管理', text_xmgl)
        self.assertEqual('开通授权', text_ktsq)
        self.assertEqual('hs', text_tx)
        # self.assertNotEqual("办公管理", text_bg)

        # 断言方法二：
        # assertIn
        # 表示包含，类似于模糊查询
        # self.assertIn("开通", text_ktsq)

        # 断言方法三：assertTrue、assertFalse
        # self.assertTrue(
        #     self.driver.find_element_by_xpath('//a[@class="nav-item router-link-active"]/div').is_displayed())
        # self.assertFalse(
        #     self.driver.find_element_by_xpath('//a[@class="nav-item router-link-active"]/div').is_displayed())

        # 断言方法四：
        # if username.text == "":
        #     print("不等于")
        # else:
        #     print("不等于")
        #     self.driver.find_element_by_id("蔡坨坨")


# 单独执行index.py
if __name__ == "__main__":
    unittest.main()
