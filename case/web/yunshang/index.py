# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/16 22:40

from selenium import webdriver
import unittest
import os
import time
from public.login import Login


class TestIndex(unittest.TestCase):
    def setUp(self):
        """ setUp方法，初始化 最先执行，每次都会打开页面 """
        self.driver = webdriver.Chrome()  # self：类的一个实例化对象
        self.driver.get("http://101.133.169.100/yuns/index.php/")
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
        """测试首页导航文案显示是否正常"""
        # 调用封装好的登录方法
        Login(self.driver).login()
        # 定位欢迎语、用户名、退出按钮
        welcome_text = self.driver.find_element_by_xpath("//body/div[1]/div/span")
        login_name = self.driver.find_element_by_xpath("//body/div[1]/div/div[1]/a[1]")
        logout_text = self.driver.find_element_by_xpath("//div[@class='login']/a[2]")

        # 断言方法一：
        # assertEqual，预期结果与实际结果比对
        self.assertEqual("亲，欢迎您来到云商系统商城！", welcome_text.text)
        self.assertEqual("150****4499", login_name.text)
        self.assertEqual("退出", logout_text.text)

        # self.assertNotEqual("150****4492", login_name.text)
        #
        # self.assertIn("", )
        #
        # self.assertTrue(self.driver.find_element_by_xpath("").is_displayed())
        #
        # self.assertFalse()
        #
        # if username.text == "":
        #     print("不等于")
        # else:
        #     self.driver.find_element_by_id("蔡坨坨")

    def testIndex01_02(self):
        '''点击“秒杀”，查看控件是否成功跳转'''

        self.driver.find_element_by_link_text('秒杀').click()

        time.sleep(5)
        print(self.driver.window_handles)
        print(self.driver.current_window_handle)

        if self.driver.current_window_handle == self.driver.window_handles[0]:
            self.driver.switch_to.window(self.driver.window_handles[1])
            print(self.driver.current_window_handle)
        else:
            pass
        jieguo = self.driver.find_element_by_link_text('限时抢购').text
        self.assertEqual('限时抢购', jieguo)


# 单独执行index.py
if __name__ == "__main__":
    unittest.main()
