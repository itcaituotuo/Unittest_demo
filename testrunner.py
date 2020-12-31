# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/16 22:41

import unittest
import time
import os
import sys
from report import HTMLTestRunner

# 获取当前.py文件的绝对路径，并进行路径分割
# dir_name：目录路径
# file_name：文件名称
dir_name, file_name = os.path.split(os.path.abspath(sys.argv[0]))
print(dir_name, file_name)
# 测试用例路径
case_path = ".\\case\\web\\wukong_crm\\"
# case_path = ".\\case\\app\\"
# 测试报告路径
result = dir_name + "\\report\\"


def create_suite():
    """  定义单元测试容器 """
    test_unit = unittest.TestSuite()  # TestSuite() 测试套件

    # 定义搜索用例文件的方法
    # 比如：web/yunshang下的所有.py文件
    discover = unittest.defaultTestLoader.discover(case_path, pattern="*.py", top_level_dir=None)

    # 将测试用例加入测试容器中
    for test_suite in discover:
        for case_name in test_suite:
            test_unit.addTest(case_name)
    return test_unit


# 调用create_suite()方法
test_case = create_suite()

# 获取系统当前时间
now_time = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
day = time.strftime('%Y-%m-%d', time.localtime(time.time()))

# 定义测试报告路径
result_dir = result + day


def report():
    """定义一个测试报告生成方法"""
    file_name = result_dir + "\\" + now_time + "_result.html"
    fp = open(file_name, 'wb')
    # 定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="测试报告", description="执行情况")
    # 执行测试用例
    runner.run(test_case)
    # 关闭报告文件
    fp.close()


# 检验文件夹路径是否存在
if os.path.exists(result_dir):
    # 调用report()方法
    report()
else:
    # 创建测试报告文件夹
    os.mkdir(result_dir)
    report()
