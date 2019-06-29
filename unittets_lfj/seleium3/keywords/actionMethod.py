# # coding=utf-8
#
# # 所有的方法都在这从keyword.excl
# # 基本仿照webdriver原理写的，再次封装，后期可以加容错处理
# 类中的函数名字，都是Excel中的--执行方法
import time
from selenium import webdriver
from selenium_lfj.find_element import FindElement


class ActionMethod:

    def open_browser(self, browser):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Edge()

    # 输入地址
    def get_url(self, url):
        self.driver.get(url)

    # 定位元素-->>输入元素--->>点击元素
    def get_element(self, key):
        find_element = FindElement(self.driver)
        element = find_element.get_element(key)
        return element

    # 输入元素
    def element_send_keys(self, key, value):
        element = self.get_element(value)
        element.send_keys(key)

    # 点击元素
    def click_element(self, key):
        self.get_element(key).click()

    # 等待功能
    def sleep_time(self,*args):
        time.sleep(3)

    # 关闭浏览器
    def close_browser(self,*args):
        self.driver.close()

    # 获取title
    def get_title(self):
        return self.driver.title