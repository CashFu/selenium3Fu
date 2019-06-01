from selenium_lfj.find_element import FindElement

# 后勤
class RegisterPage():
    def __init__(self, driver):
        self.fd = FindElement(driver)

    # 获取邮箱
    def get_email_element(self):
        return self.fd.get_element('user_email')

    # 获取用户名字
    def get_user_name_element(self):
        return self.fd.get_element('user_name')

    # 获取用户密码
    def get_password_element(self):
        return self.fd.get_element('password')

    # 获取验证码文本
    def get_code_text_element(self):
        return self.fd.get_element('code_text')

    # 获取点击按钮
    def get_register_butto_element(self):
        return self.fd.get_element('register_butto')

    # 获取错误的信息
    def get_email_error_element(self):
        return self.fd.get_element('email_error')

    def get_nickname_error_element(self):
        return self.fd.get_element('nickname_error')

    def get_password_error_element(self):
        return self.fd.get_element('password_error')

    def get_code_error_element(self):
        return self.fd.get_element('code_error')
