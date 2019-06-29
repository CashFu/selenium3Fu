# coding=utf-8
import ddt
import unittest
import os


from business.register_business import RedisterBusiness
from selenium_lfj.register_function import RegisterFunction
from selenium import webdriver
import unittest
# from util import HTMLTestReportCN
from util.HTMLTestReportCN import *
from log.user_log import *
from util.excel_util import ExcelUtil


ex =ExcelUtil()
ex_data =ex.get_data()

@ddt.ddt
class FrstDdtCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.login = RedisterBusiness(self.driver)
        time.sleep(2)

        print('——————————————这是前置——————————————')


    def tearDown(self):
        time.sleep(5)
        self.driver.close()


        print('****************************这是后置*****************************')

    # @ddt.data(
    #     ['12 ', '123465', '1234554', 'code', 'email_error', '请输入有效的电子邮件地址']
    # )
    # @ddt.unpack
    @ddt.data(*ex_data)
    def test_register_case(self,ex_data):
        print(ex_data)

        email, name, password, file_name, assertCode, assertText=ex_data
        print(file_name)
        self.login.user_base(email, name, password, file_name)
        print(1)
        print(file_name)
        # error_text = self.login.register_function(email, name, password, file_name, assertCode, assertText)
        # print(error_text)
        # self.assertFalse(error_text, '注册成功，输入错误')





if __name__ == '__main__':
    unittest.main()
    # path_cwd = os.getcwd()
    # path_file = os.path.abspath(os.path.dirname(path_cwd) + '/report' + '/first_case.html')
    # f = open(path_file, 'wb')
    # # 不是一条条的添加了，是一下都添加
    # suite = unittest.TestLoader().loadTestsFromTestCase(FrstDdtCase)
    # runner = HTMLTestRunner(stream=f, title='This is  first report1 ', description=u'这是第一测试1',verbosity=1)
    #
    # runner.run(suite)