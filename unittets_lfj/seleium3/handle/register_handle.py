# coding=utf-8
import os

from page.register_page import RegisterPage
from util.get_code import GetCode
#前台
# case所执行需要的句柄--输入层根源--页面
class RegisterHandele():
    def __init__(self, driver):
        self.driver =driver
        self.register_p = RegisterPage(self.driver)

    # 输入邮箱
    def send_user_email(self, email):
        self.register_p.get_email_element().send_keys(email)

    # 输入用户名
    def send_user_name(self, name):
        self.register_p.get_user_name_element().send_keys(name)

    # 输入密码
    def send_user_password(self, password):
        self.register_p.get_password_element().send_keys(password)

    # 输入验证码
    def send_user_code(self, file_name):
        # get_code_text =GetCode(self.driver)
        # print(8.1)
        # print(get_code_text)
        # code =get_code_text.code_online(file_name)
        # print(8.2)
        # print(code)
        self.register_p.get_code_text_element().send_keys(file_name)

    # 获取文字信息  info 是判断是属于哪个信息
    def get_text_info(self, info, user_info):
        try:
            if info == 'email_error':
                # 获取文本信息的函数get_attribute
                text = self.register_p.get_email_error_element().get_attribute('value')
                # text = self.register_p.get_email_error_element().text
            elif info == 'nickname_error':
                text = self.register_p.get_nickname_error_element().get_attribute('value')
            elif info == 'password_error':
                text = self.register_p.get_password_error_element().get_attribute('value')
            elif info == 'code_error':
                text = self.register_p.get_code_error_element().get_attribute('value')
        except:
            text=None
        return text

    # 点击注册
    def click_register_button(self):
        self.register_p.get_register_button_element().click()

#     获取注册按钮文字信息
    def get_register_text(self):
        return self.register_p.get_register_button_element().get_attribute('value')
