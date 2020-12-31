# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/17 20:15

from selenium.webdriver.common.action_chains import ActionChains
import unittest
import time
from public.wukong_crm.login import Login


class Approval(unittest.TestCase):
    def __init__(self, driver):
        self.driver = driver

    def approval(self):
        """将打开新建请假审批的页面封装成approval方法"""
        # 将鼠标移动到 快速创建
        ele = self.driver.find_element_by_css_selector('.create-button-container>span>div>div.button-name')
        ActionChains(self.driver).move_to_element(ele).perform()
        self.driver.implicitly_wait(20)
        # 点击审批
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/p[2]').click()
        self.driver.implicitly_wait(20)
        # 选择请假审批
        self.driver.find_element_by_css_selector('.vux-flexbox.vux-flex-row > div:nth-child(2)').click()
        self.driver.implicitly_wait(20)
        #
        self.driver.find_element_by_xpath('//form/div[1]/div/div/div[1]/input').click()
        time.sleep(3)

    def approval_all(self,
                     approval_content,  # 审批内容
                     star_date,  # 开始日期
                     start_time,  # 开始时间
                     end_date,  # 结束日期
                     end_time,  # 结束时间
                     long  # 时长
                     ):
        """输入审批内容的方法"""
        self.approval_content = approval_content
        self.star_date = star_date
        self.start_time = start_time
        self.end_date = end_date
        self.end_time = end_time
        self.long = long

        # 输入审批内容
        self.driver.find_element_by_xpath('//form/div[2]/div/div[1]/input').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//form/div[2]/div/div[1]/input').send_keys(approval_content)
        self.driver.implicitly_wait(20)

        # 开始时间
        # 点击开始时间的选择日期框
        self.driver.find_element_by_xpath('//form/div[3]/div/div[1]/input').click()
        self.driver.implicitly_wait(20)
        # 点击选择日期框
        self.driver.find_element_by_xpath('//div[5]/div[1]/div/div[1]/span[1]/div/input').click()
        self.driver.implicitly_wait(20)
        # 输入开始日期
        self.driver.find_element_by_xpath('//div[5]/div[1]/div/div[1]/span[1]/div/input').send_keys(star_date)
        self.driver.implicitly_wait(20)
        # 点击选择时间框
        self.driver.find_element_by_xpath('//div[5]/div[1]/div/div[1]/span[2]/div[1]/input').click()
        self.driver.implicitly_wait(20)
        # 清空时间框
        self.driver.find_element_by_xpath('//div[5]/div[1]/div/div[1]/span[2]/div[1]/input').clear()
        self.driver.implicitly_wait(20)
        # 输入开始时间
        self.driver.find_element_by_xpath('//div[5]/div[1]/div/div[1]/span[2]/div[1]/input').send_keys(start_time)
        self.driver.find_element_by_xpath('//div[5]/div[2]/button[2]/span').click()
        self.driver.implicitly_wait(20)

        # 结束时间
        # 点击结束时间的选择日期框
        self.driver.find_element_by_xpath('//form/div[4]/div/div[1]/input').click()
        self.driver.implicitly_wait(20)
        # 点击选择日期框
        self.driver.find_element_by_xpath('//div[6]/div[1]/div/div[1]/span[1]/div/input').click()
        self.driver.implicitly_wait(20)
        # 输入结束日期
        self.driver.find_element_by_xpath('//div[6]/div[1]/div/div[1]/span[1]/div/input').send_keys(end_date)
        self.driver.implicitly_wait(20)
        # 点击选择时间框
        self.driver.find_element_by_xpath('//div[6]/div[1]/div/div[1]/span[2]/div[1]/input').click()
        self.driver.implicitly_wait(20)
        # 清空时间框
        self.driver.find_element_by_xpath('//div[6]/div[1]/div/div[1]/span[2]/div[1]/input').clear()
        self.driver.implicitly_wait(20)
        # 输入结束时间
        self.driver.find_element_by_xpath('//div[6]/div[1]/div/div[1]/span[2]/div[1]/input').send_keys(end_time)
        self.driver.find_element_by_xpath('//div[6]/div[2]/button[2]/span').click()
        self.driver.implicitly_wait(20)

        # 输入时长
        self.driver.find_element_by_xpath('//form/div[5]/div/div[1]/input').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//form/div[5]/div/div[1]/input').send_keys(long)
        self.driver.implicitly_wait(20)

    def scroll_top(self):
        """将div内嵌的滚动条拉到最顶部"""
        js = 'document.querySelector("body>div.c-view>div>div.el-card__body>div>div.crm-create-flex").scrollTop=0'
        self.driver.execute_script(js)
        time.sleep(3)

    def scroll_end(self):
        """将div内嵌的滚动条拉到最底部"""
        js = 'document.querySelector("body>div.c-view>div>div.el-card__body>div>div.crm-create-flex").scrollTop=10000'
        self.driver.execute_script(js)
        time.sleep(3)

    def save(self):
        """点击保存"""
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div[3]/button[2]/span').click()
        # 使用强制等待，确保获取到提示信息
        time.sleep(5)

    def save_info(self):
        """保存成功的标志"""
        # 保存成功会跳转到首页，获取首页的一个按钮 如果那个按钮出现，说明保存成功
        element_all = self.driver.find_element_by_xpath('//div[@class="el-tabs__nav is-top"]/div[2]')
        self.assertTrue(element_all.is_displayed())

    def send_star_end_time(self, start_date, start_time, end_date, end_time):
        """输入开始时间和结束时间"""
        self.start_date = start_date
        self.start_time = start_time
        self.end_date = end_date
        self.end_time = end_time

        # 开始时间
        # 点击开始时间的选择日期框
        self.driver.find_element_by_xpath('//form/div[3]/div/div[1]/input').click()
        self.driver.implicitly_wait(20)
        # 点击选择日期框
        ele_start_date = self.driver.find_element_by_xpath('//div[5]/div[1]/div/div[1]/span[1]/div/input')
        ele_start_date.click()
        self.driver.implicitly_wait(20)
        # 输入开始日期
        ele_start_date.send_keys(start_date)
        self.driver.implicitly_wait(20)
        # 点击选择时间框
        ele_start_time = self.driver.find_element_by_xpath('//div[5]/div[1]/div/div[1]/span[2]/div[1]/input')
        ele_start_time.click()
        self.driver.implicitly_wait(20)
        # 清空时间框
        ele_start_time.clear()
        self.driver.implicitly_wait(20)
        # 输入时间
        ele_start_time.send_keys(start_time)
        # 点击确认
        self.driver.find_element_by_xpath('//div[5]/div[2]/button[2]/span').click()
        self.driver.implicitly_wait(20)

        # 结束时间
        # 点击结束时间的选择日期框
        self.driver.find_element_by_xpath('//form/div[4]/div/div[1]/input').click()
        self.driver.implicitly_wait(20)
        # 点击选择日期框
        ele_end_date = self.driver.find_element_by_xpath('//div[6]/div[1]/div/div[1]/span[1]/div/input')
        ele_end_date.click()
        self.driver.implicitly_wait(20)
        # 输入结束日期
        ele_end_date.send_keys(end_date)
        self.driver.implicitly_wait(20)
        # 点击选择时间框
        ele_end_time = self.driver.find_element_by_xpath('//div[6]/div[1]/div/div[1]/span[2]/div[1]/input')
        ele_end_time.click()
        self.driver.implicitly_wait(20)
        # 清空时间框
        ele_end_time.clear()
        self.driver.implicitly_wait(20)
        # 输入结束时间
        ele_end_time.send_keys(end_time)
        # 点击确认
        self.driver.find_element_by_xpath('//div[6]/div[2]/button[2]/span').click()
        self.driver.implicitly_wait(20)

    def send_content(self, content):
        """输入审批内容"""
        self.content = content

        ele = self.driver.find_element_by_xpath('//form/div[2]/div/div[1]/input')
        ele.click()
        self.driver.implicitly_wait(20)
        ele.send_keys(content)
        self.driver.implicitly_wait(20)

    def select_admin(self):
        """审核人选择员工admin"""

        # 点击添员工
        self.driver.find_element_by_xpath('//form/div/div/span/div[2]/div/div').click()
        time.sleep(3)
        # 选择admin
        self.driver.find_element_by_css_selector(
            'div.el-checkbox-group>label:nth-child(1)>span.el-checkbox__label>span').click()
        self.driver.implicitly_wait(20)

    def select_type_other(self):
        """请假类型选择其他"""
        self.driver.find_element_by_xpath('//ul/li[8]/span').click()
        self.driver.implicitly_wait(20)

    def check_time(self, time_long):
        """验证时长输入框"""

        self.time_long = time_long
        self._type_equality_funcs = {}  # 消除报错 AttributeError: 'Approval' object has no attribute '_type_equality_funcs'

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
        # 时长输入aa；
        Approval(self.driver).approval_all("请假审批", "2021-12-25", "17:59:58", "2021-12-26", "17:59:58", time_long)

        # 调用scroll_end()方法，将div中内嵌的滚动条滚动条移动到底部
        Approval(self.driver).scroll_end()
        # 调用select_admin()方法，审核人选择admin
        Approval(self.driver).select_admin()
        # 点击保存
        Approval(self.driver).save()

        # 断言结果
        # 提示时长必须为数字类型，整数部分须少于10位，小数部分须少于2位，且不能为负数，默认单位为时
        error_text = self.driver.find_element_by_xpath('//form/div[5]/div/div[2]').text
        self.assertEqual('时长必须为数字类型，整数部分须少于10位，小数部分须少于2位，且不能为负数，默认单位为时', error_text)
