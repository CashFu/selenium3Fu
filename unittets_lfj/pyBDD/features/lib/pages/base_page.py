# coding=utf-8
# 运行顺序： environment-->>register_user-->>register_page-->>base_page
from selenium.webdriver.common.by import By


# 页面有什么元素，需要的东西都在这写，方面后面的继承
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # 打开网页
    def get_url(self, url):
        self.driver.get(url)

    # 获取title
    def get_title(self):
        return self.driver.title

    # 查找元素 需要driver *loc 位置局部
    def find_element(self, *loc):
        return self.driver.find_element(*loc)
