# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/17 21:34

# Unittest_demo\case\web\wukong_crm\approval.py
# 新建审批相关的测试用例

import os
import time
import unittest
from selenium import webdriver

from public.wukong_crm.approval import Approval
from public.wukong_crm.login import Login


class TestApproval(unittest.TestCase):
    def setUp(self):
        """ setUp方法，初始化，最先执行，比如：每次都会打开页面 """

        self.driver = webdriver.Chrome()
        # 打开悟空CRM系统
        self.driver.get("http://101.133.169.100:8088/")
        self.driver.maximize_window()
        time.sleep(3)

        # 打印用例开始执行的时间
        print("start_time:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))

    def tearDown(self):
        """  tearDown()方法，最后执行，比如：每次执行完成都会截图 """
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

    def testApproval_01(self):
        """WKCRM_002. 新建请假审批，必填项正常输入"""

        # 调用login()方法，登录悟空CRM系统
        Login(self.driver).login()

        # 调用approval()方法，打开新建审批页面
        Approval(self.driver).approval()

        # 调用select_type_other()，请假类型选择其他
        Approval(self.driver).select_type_other()

        # 调用approval_all()方法
        # 审批内容输入：请假审批；
        # 开始时间选择：动态获取当前时间
        # 结束时间选择：动态获取；
        # 时长输入24；
        date1 = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        time1 = time.strftime('%H-%M-%S', time.localtime(time.time()))

        date2 = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        time2 = time.strftime('%H-%M-%S', time.localtime(time.time()))
        Approval(self.driver).approval_all("请假审批", date1, time1, date2, time2, 24)

        # 调用scroll_end()方法，将div中内嵌的滚动条滚动条移动到底部
        Approval(self.driver).scroll_end()

        # 调用select_admin()方法，审核人选择admin
        Approval(self.driver).select_admin()

        # 调用save()方法，点击保存
        Approval(self.driver).save()

        # 调用save_info()方法，判断是否保存成功
        Approval(self.driver).save_info()

    def testApproval_02(self):
        """WKCRM_003. 审批内容不输入，其他必填项正常输入"""

        # 调用login()方法，登录悟空CRM系统
        Login(self.driver).login()

        # 调用approval()方法，打开新建审批页面
        Approval(self.driver).approval()

        # 调用select_type_other()方法，请假类型选择其他
        Approval(self.driver).select_type_other()

        # 审批内容不填写

        # 调用send_star_end_time()方法，输入开始时间和结束时间
        # 开始时间选择：2021-12-25 17:59:58；结束时间选择：2021-12-26 17:59:58；
        Approval(self.driver).send_star_end_time("2021-12-25", "17:59:58", "2021-12-26", "17:59:58")

        # 输入时长24
        ele_time = self.driver.find_element_by_xpath('//form/div[5]/div/div[1]/input')
        ele_time.click()
        self.driver.implicitly_wait(20)
        ele_time.send_keys(24)
        self.driver.implicitly_wait(20)

        # 调用scroll_end()方法，将div中内嵌的滚动条滚动条移动到底部
        Approval(self.driver).scroll_end()

        # 调用select_admin()方法，审核人选择admin
        Approval(self.driver).select_admin()

        # 调用save()方法，点击保存
        Approval(self.driver).save()

        # 断言结果
        waring_text = self.driver.find_element_by_xpath('//form/div[2]/div/div[2]').text
        self.assertEqual("审批内容不能为空", waring_text)

    def testApproval_03(self):
        """WKCRM_004. 审批内容输入字母、数字、中文、特殊字符、空格组合，其他必填项正常输入"""

        # 调用login()方法，登录悟空CRM系统
        Login(self.driver).login()
        # 调用approval()方法，打开新建审批页面
        Approval(self.driver).approval()
        # 请假类型选择其他
        self.driver.find_element_by_xpath('//ul/li[8]/span').click()
        self.driver.implicitly_wait(20)
        # 调用approval_all()方法
        # 审批内容输入：qingjia123￥ %……你好；
        # 开始时间选择：2021-12-25 17:59:58；
        # 结束时间选择：2021-12-26 17:59:58；
        # 时长输入24；
        Approval(self.driver).approval_all("qingjia123￥ %……你好", "2020-12-25", "17:59:58", "2020-12-26", "17:59:58", 24)
        # 调用scroll_end()方法，将div中内嵌的滚动条滚动条移动到底部
        Approval(self.driver).scroll_end()
        # 调用select_admin()方法，审核人选择admin
        Approval(self.driver).select_admin()
        # 点击 保存
        Approval(self.driver).save()
        # 调用save_info()方法，判断是否保存成功
        Approval(self.driver).save_info()

    def testApproval_04(self):
        """WKCRM_005. 时长不输入，其他必填项正常输入"""

        # 调用login()方法，登录悟空CRM系统
        Login(self.driver).login()
        # 调用approval()方法，打开新建审批页面
        Approval(self.driver).approval()
        # 调用select_type_other()方法，请假类型选择其他
        Approval(self.driver).select_type_other()
        # 调用send_content()方法，输入审批内容
        Approval(self.driver).send_content("请假审批")
        # 调用send_star_end_time()方法，输入开始时间和结束时间
        # 开始时间选择：2021-12-25 17:59:58；结束时间选择：2021-12-26 17:59:58；
        Approval(self.driver).send_star_end_time("2021-12-25", "17:59:58", "2021-12-26", "17:59:58")

        # 时长不输入

        # 调用select_admin()方法，审核人选择员工
        Approval(self.driver).select_admin()
        # 调用save()方法，点击保存
        Approval(self.driver).save()
        # 断言结果
        # 提示时长不能为空
        waring_text = self.driver.find_element_by_xpath('//form/div[5]/div/div[2]').text
        self.assertEqual('时长不能为空', waring_text)

    def testApproval_05(self):
        """WKCRM_006. 时长输入含有字母，其他必填项正常输入"""

        # 调用check_time()方法，对时长输入框进行等价类验证
        Approval(self.driver).check_time("aa")

    def testApproval_06(self):
        """WKCRM_007. 时长输入0，其他必填项正常输入"""

        # 调用login()方法，登录悟空CRM系统
        Login(self.driver).login()
        # 调用approval()方法，打开新建审批页面
        Approval(self.driver).approval()
        # 调用select_type_other()方法，请假类型选择其他
        Approval(self.driver).select_type_other()

        # 调用approval_all()方法
        # 审批内容输入：请假审批；
        # 开始时间选择：2021-12-25 17:59:58；
        # 结束时间选择：2021-12-26 17:59:58；
        # 时长输入0；
        Approval(self.driver).approval_all("请假审批", "2021-12-25", "17:59:58", "2021-12-26", "17:59:58", 0)

        # 调用scroll_end()方法，将div中内嵌的滚动条滚动条移动到底部
        Approval(self.driver).scroll_end()
        # 调用select_admin()方法，审核人选择admin
        Approval(self.driver).select_admin()
        # 点击保存
        Approval(self.driver).save()

        # 断言结果
        # 提示时长不能为零
        error_text = self.driver.find_element_by_xpath('//form/div[5]/div/div[2]').text
        self.assertEqual('时长不能为零', error_text)  # NoSuchElementException 找不到元素，说明没有给出提示

    def testApproval_07(self):
        """WKCRM_008. 时长输入含有特殊符号，其他必填项正常输入"""

        # 调用check_time()方法，对时长输入框进行等价类验证
        Approval(self.driver).check_time("#￥")

    def testApproval_08(self):
        """WKCRM_009. 时长输入含有汉字，其他必填项正常输入"""

        # 调用check_time()方法，对时长输入框进行等价类验证
        Approval(self.driver).check_time("你好")

    def testApproval_09(self):
        """WKCRM_010. 时长输入负数，其他必填项正常输入"""

        # 调用check_time()方法，对时长输入框进行等价类验证
        Approval(self.driver).check_time(-1)

        # 返回结果：NoSuchElementException，说明没有给出相应的提示

    def testApproval_10(self):
        """WKCRM_011. 开始时间为空，其他必填项正常输入"""

        # 调用login()方法，登录悟空CRM系统
        Login(self.driver).login()
        # 调用approval()方法，打开新建审批页面
        Approval(self.driver).approval()
        # 调用select_type_other()，请假类型选择其他
        Approval(self.driver).select_type_other()
        # 调用send_content()方法，审批内容填写：请假审批
        Approval(self.driver).send_content("请假审批")

        # 开始时间不输入

        # 结束时间选择：2021-12-26 17:59:58
        # 点击结束时间的选择日期框
        self.driver.find_element_by_xpath('//form/div[4]/div/div[1]/input').click()
        self.driver.implicitly_wait(20)
        # 点击选择日期框
        ele_end_date = self.driver.find_element_by_css_selector(
            'body>div.el-picker-panel.el-date-picker.el-popper.has-time>div.el-picker-panel__body-wrapper>div>div.el-date-picker__time-header>span:nth-child(1)>div>input')
        ele_end_date.click()
        self.driver.implicitly_wait(20)
        # 输入结束日期
        ele_end_date.send_keys("2021-12-26")
        self.driver.implicitly_wait(20)
        # 点击选择时间框
        ele_end_time = self.driver.find_element_by_css_selector(
            'div.el-picker-panel__body-wrapper > div > div.el-date-picker__time-header > span:nth-child(2) > div.el-input.el-input--small > input')
        ele_end_time.click()
        self.driver.implicitly_wait(20)
        # 清空时间框
        ele_end_time.clear()
        self.driver.implicitly_wait(20)
        # 输入结束时间
        ele_end_time.send_keys("17:59:58")
        # 点击确认
        self.driver.find_element_by_css_selector('.el-button--mini.is-plain > span').click()
        self.driver.implicitly_wait(20)

        # 输入时长24
        self.driver.find_element_by_xpath('//form/div[5]/div/div[1]/input').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//form/div[5]/div/div[1]/input').send_keys(24)
        self.driver.implicitly_wait(20)

        # 调用select_admin()方法，审核人选择admin
        Approval(self.driver).select_admin()

        # 调用save()方法，点击保存
        Approval(self.driver).save()

        # 断言结果
        # 提示开始时间不能为空
        waring_text = self.driver.find_element_by_xpath('//form/div[3]/div/div[2]').text
        self.assertEqual('开始时间不能为空', waring_text)

    def testApproval_11(self):
        """WKCRM_012. 结束时间为空，其他必填项正常输入"""

        # 调用login()方法，登录悟空CRM系统
        Login(self.driver).login()
        # 调用approval()方法，打开新建审批页面
        Approval(self.driver).approval()
        # 调用select_type_other()，请假类型选择其他
        Approval(self.driver).select_type_other()
        # 调用send_content()方法，审批内容填写：请假审批
        Approval(self.driver).send_content("请假审批")

        # 开始时间选择：2021-12-25 17:59:58；
        # 点击开始时间的选择日期框
        self.driver.find_element_by_xpath('//form/div[3]/div/div[1]/input').click()
        self.driver.implicitly_wait(20)
        # 点击选择日期框
        ele_start_date = self.driver.find_element_by_css_selector(
            'body>div.el-picker-panel.el-date-picker.el-popper.has-time>div.el-picker-panel__body-wrapper>div>div.el-date-picker__time-header>span:nth-child(1)>div>input')
        ele_start_date.click()
        self.driver.implicitly_wait(20)
        # 输入开始日期
        ele_start_date.send_keys("2021-12-25")
        self.driver.implicitly_wait(20)
        # 点击选择时间框
        ele_start_time = self.driver.find_element_by_css_selector(
            'body>div.el-picker-panel.el-date-picker.el-popper.has-time>div.el-picker-panel__body-wrapper>div>div.el-date-picker__time-header>span:nth-child(2)>div.el-input.el-input--small>input')
        ele_start_time.click()
        self.driver.implicitly_wait(20)
        # 清空时间框
        ele_start_time.clear()
        self.driver.implicitly_wait(20)
        # 输入时间
        ele_start_time.send_keys("17:59:58")
        # 点击确认
        self.driver.find_element_by_css_selector(
            'body > div.el-picker-panel.el-date-picker.el-popper.has-time > div.el-picker-panel__footer > button.el-button.el-picker-panel__link-btn.el-button--default.el-button--mini.is-plain').click()
        self.driver.implicitly_wait(20)

        # 结束时间不填写

        # 输入时长24
        self.driver.find_element_by_xpath('//form/div[5]/div/div[1]/input').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//form/div[5]/div/div[1]/input').send_keys(24)
        self.driver.implicitly_wait(20)

        # 调用select_admin()方法，审核人选择admin
        Approval(self.driver).select_admin()

        # 调用save()方法，点击保存
        Approval(self.driver).save()

        # 断言结果
        # 提示结束时间不能为空
        waring_text = self.driver.find_element_by_css_selector('div.el-form-item__error').text
        self.assertEqual('结束时间不能为空', waring_text)

    def testApproval_12(self):
        """WKCRM_013. 开始时间等于结束时间"""

        # 调用login()方法，登录悟空CRM系统
        Login(self.driver).login()
        # 调用approval()方法，打开新建审批页面
        Approval(self.driver).approval()
        # 调用select_type_other()，请假类型选择其他
        Approval(self.driver).select_type_other()

        # 调用approval_all()方法
        # 审批内容输入：请假审批；
        # 开始时间选择：2021-12-25 17:59:58；
        # 结束时间选择：2021-12-25 17:59:58；
        # 时长输入24；
        Approval(self.driver).approval_all("请假审批", "2021-12-25", "17:59:58", "2021-12-25", "17:59:58", 24)

        # 调用select_admin()方法，审核人选择admin
        Approval(self.driver).select_admin()
        # 调用save()方法，点击保存
        Approval(self.driver).save()  # 调用select_admin()方法，审核人选择admin
        Approval(self.driver).select_admin()
        # 调用save()方法，点击保存
        Approval(self.driver).save()

        # 断言结果
        # 提示开始时间不能等于结束时间
        # NoSuchElementException，找不到错误提示，说明没有给出提示
        self.assertTrue(self.driver.find_element_by_xpath('/html/body/div[8]/p').is_displayed())

    def testApproval_13(self):
        """WKCRM_014. 开始时间大于结束时间"""

        # 调用login()方法，登录悟空CRM系统
        Login(self.driver).login()
        # 调用approval()方法，打开新建审批页面
        Approval(self.driver).approval()
        # 调用select_type_other()，请假类型选择其他
        Approval(self.driver).select_type_other()

        # 调用approval_all()方法
        # 审批内容输入：请假审批；
        # 开始时间选择：2021-12-27 17:59:58；
        # 结束时间选择：2021-12-26 17:59:58；
        # 时长输入24；
        Approval(self.driver).approval_all("请假审批", "2021-12-27", "17:59:58", "2021-12-26", "17:59:58", 24)

        # 调用scroll_end()方法，将div中内嵌的滚动条滚动条移动到底部
        Approval(self.driver).scroll_end()
        # 调用select_admin()方法，审核人选择admin
        Approval(self.driver).select_admin()
        # 点击保存
        self.driver.find_element_by_xpath('//div[3]/div/div[1]/div/div[3]/button[2]/span').click()
        self.driver.implicitly_wait(10)

        # 获取提示信息
        error_text = self.driver.find_element_by_css_selector(
            'body>div.el-message.el-message--error.el-message-fade-leave-active.el-message-fade-leave-to>p')

        # 断言结果：
        # 提示审批结束时间早于开始时间
        self.assertEqual('审批结束时间早于开始时间', error_text.text)

    def testApproval_14(self):
        """WKCRM_015. 开始时间小于结束时间"""

        # 调用login()方法，登录悟空CRM系统
        Login(self.driver).login()
        # 调用approval()方法，打开新建审批页面
        Approval(self.driver).approval()
        # 调用select_type_other()，请假类型选择其他
        Approval(self.driver).select_type_other()

        # 调用approval_all()方法
        # 审批内容输入：请假审批；
        # 开始时间选择：2021-12-25 17:59:58；
        # 结束时间选择：2021-12-26 17:59:58；
        # 时长输入24；
        Approval(self.driver).approval_all("请假审批", "2021-12-25", "17:59:58", "2021-12-26", "17:59:58", 24)

        # 调用scroll_end()方法
        # 将div中内嵌的滚动条滚动条移动到底部
        Approval(self.driver).scroll_end()
        # 调用select_admin()方法，审核人选择admin
        Approval(self.driver).select_admin()
        # 调用save()方法，点击保存
        Approval(self.driver).save()
        # 调用save_info()方法，判断是否保存成功
        Approval(self.driver).save_info()

    def testApproval_15(self):
        """WKCRM_016. 审核人不选择"""

        # 调用login()方法，登录悟空CRM系统
        Login(self.driver).login()
        # 调用approval()方法，打开新建审批页面
        Approval(self.driver).approval()
        # 调用select_type_other()，请假类型选择其他
        Approval(self.driver).select_type_other()

        # 调用approval_all()方法
        # 审批内容输入：请假审批；
        # 开始时间选择：2021-12-25 17:59:58；
        # 结束时间选择：2021-12-26 17:59:58；
        # 时长输入24；
        Approval(self.driver).approval_all("请假审批", "2021-12-25", "17:59:58", "2021-12-26", "17:59:58", 24)

        # 调用scroll_end()方法
        # 将div中内嵌的滚动条滚动条移动到底部
        Approval(self.driver).scroll_end()

        # 审核人不选择

        # 调用save()方法，点击保存
        Approval(self.driver).save()

        # 断言结果
        # 提示审批人不能为空
        waring_text = self.driver.find_element_by_xpath('//div[4]/div[2]/div/form/div/div/div').text
        self.assertEqual('审批人不能为空', waring_text)

    def testApproval_16(self):
        """WKCRM_017. 备注栏输入字母、数字、中文汉字、特殊字符、空格组合，其他必填项正常输入"""

        # 调用login()方法，登录悟空CRM系统
        Login(self.driver).login()
        # 调用approval()方法，打开新建审批页面
        Approval(self.driver).approval()
        # 调用select_type_other()，请假类型选择其他
        Approval(self.driver).select_type_other()

        # 备注栏输入字母、数字、特殊字符、空格组合：abc123！@ #中
        self.driver.find_element_by_css_selector('form>div:nth-child(6)>div>div>textarea').send_keys("abc123！@ #中")

        # 调用approval_all()方法
        # 审批内容输入：请假审批；
        # 开始时间选择：2021-12-25 17:59:58；
        # 结束时间选择：2021-12-26 17:59:58；
        # 时长输入24；
        Approval(self.driver).approval_all("请假审批", "2021-12-25", "17:59:58", "2021-12-26", "17:59:58", 24)

        # 调用scroll_end()方法
        # 将div中内嵌的滚动条滚动条移动到底部
        Approval(self.driver).scroll_end()
        # 调用select_admin()方法，审核人选择admin
        Approval(self.driver).select_admin()
        # 调用save()方法，点击保存
        Approval(self.driver).save()

        # 调用save_info()方法，判断是否保存成功
        Approval(self.driver).save_info()

    def testApproval_17(self):
        """WKCRM_018. 备注栏不输入，其他必填项正常输入"""

        # 调用login()方法，登录悟空CRM系统
        Login(self.driver).login()
        # 调用approval()方法，打开新建审批页面
        Approval(self.driver).approval()
        # 调用select_type_other()，请假类型选择其他
        Approval(self.driver).select_type_other()

        # 调用approval_all()方法
        # 审批内容输入：请假审批；
        # 开始时间选择：2021-12-25 17:59:58；
        # 结束时间选择：2021-12-26 17:59:58；
        # 时长输入24；
        Approval(self.driver).approval_all("请假审批", "2021-12-25", "17:59:58", "2021-12-26", "17:59:58", 24)

        # 调用scroll_end()方法
        # 将div中内嵌的滚动条滚动条移动到底部
        Approval(self.driver).scroll_end()

        # 调用select_admin()方法，审核人选择admin
        Approval(self.driver).select_admin()
        # 调用save()方法，点击保存
        Approval(self.driver).save()
        # 调用save_info()方法，判断是否保存成功
        Approval(self.driver).save_info()

    def testApproval_18(self):
        """WKCRM_019. 请假类型选择中间一个，其他必填项正常输入"""

        # 调用login()方法，登录悟空CRM系统
        Login(self.driver).login()
        # 调用approval()方法，打开新建审批页面
        Approval(self.driver).approval()
        # 请假类型选择调休
        self.driver.find_element_by_xpath('//ul/li[5]').click()
        self.driver.implicitly_wait(20)

        # 调用approval_all()方法
        # 审批内容输入：请假审批；
        # 开始时间选择：2021-12-25 17:59:58；
        # 结束时间选择：2021-12-26 17:59:58；
        # 时长输入24；
        Approval(self.driver).approval_all("请假审批", "2021-12-25", "17:59:58", "2021-12-26", "17:59:58", 24)

        # 调用scroll_end()方法
        # 将div中内嵌的滚动条滚动条移动到底部
        Approval(self.driver).scroll_end()
        # 调用select_admin()方法，审核人选择admin
        Approval(self.driver).select_admin()
        # 调用save()方法，点击保存
        Approval(self.driver).save()

        # 调用save_info()方法，判断是否保存成功
        Approval(self.driver).save_info()

    def testApproval_19(self):
        """WKCRM_020. 请假类型选择第一个，其他必填项正常输入"""

        # 调用login()方法，登录悟空CRM系统
        Login(self.driver).login()
        # 调用approval()方法，打开新建审批页面
        Approval(self.driver).approval()
        # 请假类型选择默认：年假

        # 调用approval_all()方法
        # 审批内容输入：请假审批；
        # 开始时间选择：2021-12-25 17:59:58；
        # 结束时间选择：2021-12-26 17:59:58；
        # 时长输入24；
        Approval(self.driver).approval_all("请假审批", "2021-12-25", "17:59:58", "2021-12-26", "17:59:58", 24)

        # 调用scroll_end()方法
        # 将div中内嵌的滚动条滚动条移动到底部
        Approval(self.driver).scroll_end()
        # 调用select_admin()方法，审核人选择admin
        Approval(self.driver).select_admin()
        # 调用save()方法，点击保存
        Approval(self.driver).save()

        # 调用save_info()方法，判断是否保存成功
        Approval(self.driver).save_info()


# 单独执行index.py
if __name__ == "__main__":
    unittest.main()
