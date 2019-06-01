# coding=utf-8
from business.register_business import RedisterBusiness
from selenium_lfj.register_function import RegisterFunction
from selenium import webdriver

# 写所有的case层
class FirstCase():
    def __init__(self):
        driver = webdriver.Chrome()
        driver.get('http://www.5itest.cn/register')
        self.login = RedisterBusiness(driver)

    def test_login_email_error(self):
        email_error_text = self.login.login_email_error('12', '1234', '12345', 'code')
        if email_error_text == True:
            print('注册成功，---email输入错误')

    def test_login_username_error(self):
        username_error_text = self.login.login_name_error('12111@126.com', 'ss', '12345', 'code')
        if username_error_text == True:
            print('注册成功，---name输入错误')

    def test_login_password_error(self):
        password_error_text = self.login.login_password_error('12213@126.com', '1234', '1', 'code')
        if password_error_text == True:
            print('注册成功，---password输入错误')

    def test_login_code_error(self):
        code_error = self.login.login_code_error('12@126.com', '1234', '12345', '')
        if code_error == True:
            print('注册成功,---code输入错误')

    def test_login_succeed(self):
        self.login.user_base('1234@126.com', '1234', '12345', 'p23p2')
        if self.login.register_succes() == True:
            print('注册成功')
def main():
    first = FirstCase()
    first.test_login_email_error()
    first.test_login_password_error()
    first.test_login_username_error()
    first.test_login_code_error()
    first.test_login_succeed()
if __name__ == '__main__':
    main()