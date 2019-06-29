# coding=utf-8
import os
import random

import time
from PIL import Image
from selenium import webdriver

from selenium_lfj.ShowapiRequest import ShowapiRequest
from selenium_lfj.find_element import FindElement

from page.register_page import RegisterPage

# 登录
class RegisterFunction():
    def __init__(self, url,driver):
        self.driver = self.send_driver(url,driver)


    # 获取deiver
    def send_driver(self, url, more_brower):
        if more_brower == 0:
            driver = webdriver.Chrome()
        elif more_brower == 1:
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Edge()
        driver.get(url=url)
        driver.maximize_window()
        return driver

    # 获取用户信息--data是指输入的用户信息
    def send_user_info(self, key, data):
        self.get_user_element(key).send_keys(data)

    # 获取用户信息,先定位element
    def get_user_element(self, key):
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(key)
        return user_element

    # 获取随机数
    def get_range_user(self):
        user_info = ''.join(random.sample('1234567890qwertyuiopasdfghjklzxcvbnm', 5))
        return user_info

    # 保存图片
    def get_code_image(self, file_path):
        self.driver.save_screenshot(file_path)
        # code_element = self.get_user_element('code_image')

        code_element =self.driver.find_element_by_id('getcode_num')
        left = code_element.location["x"]
        top = code_element.location["y"]
        rigth = code_element.size['width'] + left
        height = code_element.size['height'] + top
        im = Image.open(file_path)
        img = im.crop((left, top, rigth, height))

        img.save(file_path)

    # 解析图片
    def code_online(self, file_path):
        self.get_code_image(file_path)
        r = ShowapiRequest("http://route.showapi.com/184-4", "95852", "11b2e667952d400596286de04efc4e03")
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addBodyPara("needMorePrecise", "0")
        r.addFilePara("image", file_path)  # 文件上传时设置
        res = r.post()
        text = res.json()["showapi_res_body"]["Result"]
        return text


    def main(self):
        user_nickname = self.get_range_user()
        user_email = user_nickname + '@126.com'
        path_file = os.getcwd()
        file_path = os.path.abspath(os.path.dirname(path_file) + '/Image' + '/c.png')
        text = self.code_online(file_path)
        self.send_user_info('user_email', user_email)
        self.send_user_info('user_name', user_nickname)
        self.send_user_info('password', user_nickname)
        self.send_user_info('code_text', text)
        self.get_user_element('register_button').click()
        code_error = self.get_user_element('captcha_code-error')
        if code_error == None:
            print('注册成功')
        else:
            path_file = os.getcwd()
            file_path = os.path.abspath(os.path.dirname(path_file) + '/Image' + '/code.png')
            print(file_path)
            self.driver.save_screenshot(file_path)
        time.sleep(2)
        self.driver.close()


if __name__ == '__main__':
    pass

    for more_brower in range(1):
        print(more_brower)
        register_function = RegisterFunction('http://www.5itest.cn/register',more_brower)
        register_function.main()
