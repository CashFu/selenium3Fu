# coding=utf-8
from selenium.webdriver.common.by import By

from features.lib.pages.base_page import BasePage


# 运行顺序： environment(环境)-->>register_user(登录用户)
# -->>register_page(登录页)-->>base_page()

class RegisterPage(BasePage):
    def __init__(self, context):
        # 这的driver，需要传进来
        super(RegisterPage, self).__init__(context.driver)

    # 注册页面有发送功能
    def send_useremail(self, useremail):
        self.find_element(By.ID, 'register_email').send_keys(useremail)

        # def register_get_title(self):
        # self.get_title()

    # 注册页面有发送功能
    def send_username(self, username):
        self.find_element(By.ID, 'register_nickname').send_keys(username)

    def send_password(self, password):
        self.find_element(By.ID, 'register_password').send_keys(password)

    def send_code(self, code):
        self.find_element(By.ID, 'captcha_code').send_keys(code)

    def click_register_button(self):
        self.find_element(By.ID, 'register-btn').click()

    def get_code_text(self):
        return self.find_element(By.ID, 'captcha_code-error').text
