# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2021/1/5 13:47

from selenium import webdriver
import unittest
import time
import warnings


class BlogIndex(unittest.TestCase):
    def setUp(self):
        for i in range(0, 10000):
            # 忽略警告，Enable tracemalloc to get the object allocation traceback
            warnings.simplefilter("ignore", ResourceWarning)

            # 实例化driver
            self.driver = webdriver.Chrome()

            # HTTP和HTTPS
            self.driver.get("https://www.cnblogs.com/caituotuo/p/14253800.html")
            # 窗口最大化
            self.driver.maximize_window()
            time.sleep(60)

            # 软件测试基础知识
            self.driver.get("https://www.cnblogs.com/caituotuo/p/14226452.html")
            # 窗口最大化
            self.driver.maximize_window()
            time.sleep(60)

            # 接口自动化测试
            self.driver.get("https://www.cnblogs.com/caituotuo/p/14260258.html")
            # 窗口最大化
            self.driver.maximize_window()
            time.sleep(60)
            self.driver.quit()

    def tearDown(self):
        pass

    def test_001(self):
        pass


if __name__ == "__main__":
    unittest.main()
