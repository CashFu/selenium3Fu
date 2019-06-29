# coding=utf-8
from selenium import webdriver


# context超级全局变量
def before_all(context):
    context.driver = webdriver.Chrome()


def after_all(context):
    context.driver.close()
