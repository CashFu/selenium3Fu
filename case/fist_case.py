# coding=utf-8
import os

from business.register_business import RedisterBusiness
from selenium_lfj.register_function import RegisterFunction
from selenium import webdriver
import unittest
import HTMLTestReportCN


# 写所有的case层
class FirstCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.login = RedisterBusiness(self.driver)
        print('——————————————这是前置——————————————')

    def tearDown(self):
        self.driver.close()

        print('****************************这是后置*****************************')

    def test_login_email_error(self):
        email_error_text = self.login.login_email_error(' ', '123465', '1234554', 'code')
        # if email_error_text == True:
        #     print('注册成功，---email输入错误')
        self.assertFalse(email_error_text,'注册成功，---email输入错误')

            # def test_login_username_error(self):
            #     username_error_text = self.login.login_name_error('12112341@126.com', ' ', '12342345', 'code')
            #     if username_error_text == True:
            #         print('注册成功，---name输入错误')
            #     # self.assertFalse(username_error_text,'注册成功，---name输入错误')
            #
            # def test_login_password_error(self):
            #     password_error_text = self.login.login_password_error('12232413@126.com', '124322334', ' ', 'code')
            #     # if password_error_text == True:
            #     #     print('注册成功，---password输入错误')
            #     self.assertFalse(password_error_text,'注册成功，---password输入错误')
            #
            # def test_login_code_error(self):
            #     code_error = self.login.login_code_error('12342@126.com', '1223434', '12323445', '')
            #     # if code_error == True:
            #     #     print('注册成功,---code输入错误')
            #     self.assertFalse(code_error,'注册成功,---code输入错误')
            #
            # def test_login_succeed(self):
            #     self.login.user_base('1233424@126.com', '1233244', '12345324', 'p23p2342')
            #     # if self.login.register_succes() == True:
            #     #     print('注册成功')
            #     self.assertFalse(self.login.register_succes(),'注册成功')
            # def main():
            # first = FirstCase()
            # first.test_login_email_error()
            # first.test_login_password_error()
            # first.test_login_username_error()
            # first.test_login_code_error()
            # first.test_login_succeed()


if __name__ == '__main__':
    # main()
    # unittest.main()
    path_cwd = os.getcwd()
    path_file = os.path.abspath(os.path.dirname(path_cwd) + '/report' + '/first_case.html')
    f = open(path_file, 'wb')

    suite = unittest.TestSuite()
    suite.addTest(FirstCase('test_login_email_error'))
    # unittest.TextTestRunner().run(suite)
    runner= HTMLTestReportCN.HTMLTestRunner(stream=f, title='This is  first report ',description=u'这是第一测试',verbosity=1)
    runner.run(suite)
