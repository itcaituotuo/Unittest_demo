# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/23 13:55

import os
import unittest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
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
        self.driver.implicitly_wait(60)

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

    def test_login_01(self):
        """ZY001_验证正常登录功能"""

        # 调用login()方法，登录
        AppLogin(self.driver).login("15127409611", "a123456")

        # 断言结果
        # 登录成功，跳转到我的页面，显示该账号的用户名
        member_name = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/member_name").text
        print(member_name)
        self.assertEqual("ad涅", member_name)

    def test_login_out_02(self):
        """ZY002_验证是否能正常退出当前账号"""

        # 调用login()方法，先进行登录
        AppLogin(self.driver).login("15127409611", "a123456")
        # 再调用login_out()，退出当前账号
        AppLogin(self.driver).login_out()

        # 断言结果
        text = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tv_notLogin_goLogin").text
        print(text)
        self.assertEqual("立即登录/注册", text)

    def test_login_password_error_03(self):
        """ZY003_验证异常登录，密码错误"""

        # 调用login()方法，输入错误的密码
        AppLogin(self.driver).login("15127409611", "a12345")

        # 断言结果，提示账号或密码错误
        ele = WebDriverWait(self.driver, 20, 0.1).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@text='账号或密码错误']")))
        print(ele.text)
        self.assertEqual('账号或密码错误', ele.text)

    def test_login_phone_error_04(self):
        """ZY004_验证异常登录，手机号未注册"""

        # 调用login()方法，输入错误的密码
        AppLogin(self.driver).login("15127409613", "a123456")

        # 断言结果，提示手机号还没有注册
        ele = WebDriverWait(self.driver, 20, 0.1).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@text='手机号还没有注册']")))
        print(ele.text)
        self.assertEqual('手机号还没有注册', ele.text)

    def test_sign_08(self):
        """ZY008_验证修改签名功能"""

        # 调用sign()方法，修改个性签名
        AppLogin(self.driver).sign("编测编学")
        # 断言结果，提示签名修改成功
        ele = WebDriverWait(self.driver, 20, 0.1).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@text='签名修改成功']")))
        print(ele.text)
        self.assertEqual('签名修改成功', ele.text)

    def test_sign_09(self):
        """ZY009_签名内容含有字母，数字，字符串，空格，汉字"""

        # 调用sign()方法，修改个性签名
        AppLogin(self.driver).sign("abc12 3*/@签名")
        # 断言结果，提示签名修改成功
        ele = WebDriverWait(self.driver, 20, 0.1).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@text='签名修改成功']")))
        print(ele.text)
        self.assertEqual('签名修改成功', ele.text)

    def test_sign_10(self):
        """ZY010_验证签名内容为空时点击保存是否有提示"""

        # 调用sign()方法，修改个性签名
        AppLogin(self.driver).sign("")
        # 断言结果，提示签名不能为空
        ele = WebDriverWait(self.driver, 20, 0.1).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@text='签名不能为空']")))
        print(ele.text)
        self.assertEqual('签名不能为空', ele.text)

    def test_search_11(self):
        """ZY011_验证搜索功能"""

        # 调用login()方法，登录
        AppLogin(self.driver).login("15127409611", "a123456")

        # 调用search()方法
        AppLogin(self.driver).search("迪丽热巴")

        # 断言结果
        text = self.driver.find_elements_by_id('cn.xiaochuankeji.tieba:id/title')
        ls = []
        for i in range(0, len(text)):
            ls.append(text[i].text)
        ls2 = ''.join(ls)
        self.assertIn('迪丽热巴', ls2)

    def test_search_12(self):
        """ZY012_验证搜索不到内容时是否有提示"""

        # 调用login()方法，登录
        AppLogin(self.driver).login("15127409611", "a123456")

        # 调用search()方法
        AppLogin(self.driver).search("123")

        # 断言结果
        text = self.driver.find_element_by_id('cn.xiaochuankeji.tieba:id/tvTip').text
        print(text)
        self.assertEqual('打开方式不对，换个关键词试试~', text)

    def test_attention_013(self):
        """ZY013_验证关注用户功能"""

        # 调用login()方法，登录
        AppLogin(self.driver).login("15127409611", "a123456")
        # 点击最右按钮，切换至首页
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
        time.sleep(3)
        # 切换至关注页面
        ele = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/title")
        ele.click()
        time.sleep(3)
        # 点击关注
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tv_subscribe_name_unselected").click()
        time.sleep(3)
        # 断言结果
        text = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tv_subscribe_name_selected").text
        print(text)
        self.assertEqual("已关注", text)

    def test_attention_014(self):
        """ZY014_验证取消关注用户功能"""

        # 调用login()方法，登录
        AppLogin(self.driver).login("15127409611", "a123456")
        # 点击最右按钮，切换至首页
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
        time.sleep(3)
        # 切换至关注页面
        ele = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/title")
        ele.click()
        time.sleep(3)
        # 点击关注
        unselected = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tv_subscribe_name_unselected")
        unselected.click()
        time.sleep(3)
        # 点击取消关注
        selected = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tv_subscribe_name_selected")
        selected.click()
        # 断言结果
        self.assertEqual("关注", unselected.text)

    def test_attention_015(self):
        """ZY015_验证我关注的人是否正确"""
        # 调用login()方法，登录
        AppLogin(self.driver).login("15127409611", "a123456")
        # 点击最右按钮，切换至首页
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
        time.sleep(3)
        # 切换至关注页面
        ele = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/title")
        ele.click()
        time.sleep(3)
        # 点击关注
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tv_subscribe_name_unselected").click()
        time.sleep(3)
        # 获取用户昵称
        nick = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/nickname").text
        # 点击我的，进入我的模块
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/me_item").click()
        time.sleep(2)
        # 点击关注，进入到我的关注页面
        self.driver.find_element_by_xpath("//android.widget.TextView[@text=\"关注\"]").click()
        time.sleep(2)

        # 断言结果
        # 获取有所用户的昵称，通过循环，放入列表，再转换成字符串，与前面获取的nick对比
        text = self.driver.find_elements_by_id('cn.xiaochuankeji.tieba:id/tv_name')
        ls = []
        for i in range(0, len(text)):
            ls.append(text[i].text)
        ls2 = ''.join(ls)
        self.assertIn(nick, ls2)


if __name__ == "__main__":
    unittest.main()
