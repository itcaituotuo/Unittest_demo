# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2021/1/5 13:47

from selenium import webdriver
import unittest
import time
import warnings


class BlogIndex(unittest.TestCase):
    def setUp(self):
        # 忽略警告，Enable tracemalloc to get the object allocation traceback
        warnings.simplefilter("ignore", ResourceWarning)
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.cnblogs.com/caituotuo/p/14226452.html")
        self.driver.maximize_window()
        time.sleep(3)
        js = "var bottom = document.documentElement.scrollTop = 10000"
        self.driver.execute_script(js)
        time.sleep(120)

    def tearDown(self):
        self.driver.quit()

    def test001(self):
        pass

    def test002(self):
        pass

    def test003(self):
        pass

    def test004(self):
        pass

    def test005(self):
        pass

    def test006(self):
        pass

    def test007(self):
        pass

    def test008(self):
        pass

    def test009(self):
        pass

    def test010(self):
        pass

    def test011(self):
        pass

    def test012(self):
        pass

    def test013(self):
        pass

    def test014(self):
        pass

    def test015(self):
        pass

    def test016(self):
        pass

    def test017(self):
        pass

    def test018(self):
        pass

    def test019(self):
        pass

    def test020(self):
        pass

    def test021(self):
        pass

    def test022(self):
        pass

    def test023(self):
        pass

    def test024(self):
        pass

    def test025(self):
        pass

    def test026(self):
        pass

    def test027(self):
        pass

    def test028(self):
        pass

    def test029(self):
        pass

    def test030(self):
        pass

    def test031(self):
        pass

    def test032(self):
        pass

    def test033(self):
        pass

    def test034(self):
        pass

    def test035(self):
        pass

    def test036(self):
        pass

    def test037(self):
        pass

    def test038(self):
        pass

    def test039(self):
        pass

    def test040(self):
        pass

    def test041(self):
        pass

    def test042(self):
        pass

    def test043(self):
        pass

    def test044(self):
        pass

    def test045(self):
        pass

    def test046(self):
        pass

    def test047(self):
        pass

    def test048(self):
        pass

    def test049(self):
        pass

    def test050(self):
        pass


if __name__ == "__main__":
    unittest.main()
