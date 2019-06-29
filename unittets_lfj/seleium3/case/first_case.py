# coding=utf-8
import time

from business.register_business import RedisterBusiness
from selenium_lfj.register_function import RegisterFunction
from selenium import webdriver
import unittest
# from util import HTMLTestReportCN
from util.HTMLTestReportCN import *
from log.user_log import *

# 写所有的case层
class FirstCase(unittest.TestCase):
    # 若是放到函数外面，只能执行一遍log：因为第一次实例化了，创建了对象然后销毁了，第二次没有可用的了
    # 放发函数setup里面也可以
    @classmethod
    def setUpClass(cls):
        # 调用日志的地方
        cls.log = UserLog()
        cls.user_log = cls.log.get_log()

        # 传给放的路径信息--code码保存路径
        path_file = os.getcwd()
        file_name = os.path.abspath(os.path.dirname(path_file) + '/Image' + '/code.png')
        cls.file_name = file_name

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.user_log.info('this is chrome')

        self.login = RedisterBusiness(self.driver)
        print('——————————————这是前置——————————————')

    def tearDown(self):
        time.sleep(3)
        # outcome: 捕捉函数运作之后的结果
        for method_name, error in self._outcome.errors:
            if error:
                cae_name = self._testMethodName
                path_cwd = os.getcwd()
                file_path = os.path.abspath(os.path.dirname(path_cwd) + '/report' + '/' + cae_name + '.png')
                self.driver.save_screenshot(file_path)

        self.driver.close()

        print('****************************这是后置*****************************')

    @classmethod
    def tearDownClass(cls):
        # 还是报错：TypeError: 'FileHandler' object is not callable
        # cls.log = UserLog()
        cls.log.file_handle()

    # 验证邮箱
    def test_login_email_error(self):
        email_error_text = self.login.login_email_error('0', '1234265', '12342554', self.file_name)
        # if email_error_text == True:
        #     print('注册成功，---email输入错误')
        self.assertFalse(email_error_text, '注册成功，---email输入错误')

    # 验证用户名
    def test_login_username_error(self):
        username_error_text = self.login.login_name_error('121122341@126.com', '1', '123422345', self.file_name)
        # if username_error_text == True:
        #     print('注册成功，---name输入错误')
        self.assertFalse(username_error_text, '注册成功，---name输入错误')

    # 验证密码
    def test_login_password_error(self):
        password_error_text = self.login.login_password_error('122321413@126.com', '1214322334', '2', self.file_name)
        # if password_error_text == True:
        #     print('注册成功，---password输入错误')
        self.assertFalse(password_error_text, '注册成功，---password输入错误')


    # 验证成功
    def test_login_succeed(self):
        self.login.user_base('61224@126.com', '1122214', '11114', self.file_name)
        # if self.login.register_succes() == True:
        #     print('注册成功')
        self.assertFalse(self.login.register_succeed(), '注册成功')
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

    # suite.addTest(FirstCase('test_login_email_error'))
    # suite.addTest(FirstCase('test_login_username_error'))
    # suite.addTest(FirstCase('test_login_password_error'))
    suite.addTest(FirstCase('test_login_succeed'))

    # unittest.TextTestRunner().run(suite)
    runner = HTMLTestRunner(stream=f, title='This is  first report ', description=u'这是第一测试',
                                             verbosity=2)
    runner.run(suite)
