# coding=utf-8
# 中间
# 所有的case与句柄之间的桥梁--操作层-操作handle层
from handle.register_handle import RegisterHandele


class RedisterBusiness():
    # 执行操作--
    def __init__(self, driver):
        self.register_h = RegisterHandele(driver)

    def user_base(self, email, name, password, code):
        self.register_h.send_user_email(email)
        self.register_h.send_user_name(name)
        self.register_h.send_user_password(password)
        self.register_h.send_user_code(code)
        self.register_h.click_register_button()
        # 这个case成功返回None
        self.register_h.get_register_text()
    def register_succes(self):
        if self.register_h.get_register_text() == None:
            print("注册是点击按钮不成功")
            return True
        else:
            return False


    # 单个检查错误信息-case直接调用
    def login_email_error(self, email, name, password, code):
        self.user_base(email, name, password, code)
        # 返回的是text；有好几种text，分别获取。获取不到则为空
        if self.register_h.get_text_info('email_error', "请输入有效的电子邮件地址") == None:
            print('检查邮箱不成功')
            return True
        else:
            # 成功就是False
            return False
    def login_name_error(self, email, name, password, code):
        print(2)
        self.user_base(email, name, password, code)
        # 返回的是text；有好几种text，分别获取。获取不到则为空
        if self.register_h.get_text_info('nickname_error', '字符长度必须大于等于4，一个中文字算2个字符') == None:
            print('检查用户名不成功')
            return True
        else:
            return False

    def login_password_error(self, email, name, password, code):
        self.user_base(email, name, password, code)
        # 返回的是text；有好几种text，分别获取。获取不到则为空
        if self.register_h.get_text_info('password_error', '最少需要输入 5 个字符') == None:
            print('密码长度不成功')
            return True
        else:
            return False
    def login_code_error(self, email, name, password, code):
        self.user_base(email, name, password, code)
        # 返回的是text；有好几种text，分别获取。获取不到则为空
        if self.register_h.get_text_info('code_error', '最少需要输入 5 个字符') == None:
            print('密码长度不成功')
            return True
        else:
            return False