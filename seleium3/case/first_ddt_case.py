# coding=uff-8
import ddt
import unittest
import os

from business.register_business import RedisterBusiness
from selenium_lfj.register_function import RegisterFunction
from selenium import webdriver
import unittest
import HTMLTestReportCN


@ddt.ddt
class DttData(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.login = RedisterBusiness(self.driver)
        print('——————————————这是前置——————————————')

    def tearDown(self):
        self.driver.close()

        print('****************************这是后置*****************************')

    @ddt.data(
        [' ', '123465', '1234554', 'code', 'email_error', '请输入有效的电子邮件地址'],
        ['1211231241@126.com', ' ', '1212342345', 'code', 'nickname_error', '字符长度必须大于等于4，一个中文字算2个字符'],
        ['1211231241@126.com', '12121122222222222222222222222222', '1212342345', 'code', 'nickname_error',
         '字符长度必须小于等于18，一个中文字算2个字符'],
        ['12232413@126.com', '124322334', ' ', 'code', 'password_error', '最少需要输入 5 个字符'],
        ['12232413@126.com', '124322334', '2122121112212121212121212112 ', 'code', 'password_error', '最多只能输入 20 个字符'],
        ['12342@126.com', '1223434', '12323445', '', '最少需要输入 5 个字符'],
    )
    @ddt.unpack
    def test_login_email_error(self, email, username, password, code, assertCode, assertText):
        error_text = self.login.register_function(email, username, password, code, assertCode, assertText)
        self.assertFalse(error_text, '注册成功，输入错误')


if __name__ == '__main__':
    unittest.main()
