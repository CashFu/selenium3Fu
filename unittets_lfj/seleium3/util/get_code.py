# coding=utf-8
import time
from PIL import Image
from selenium import webdriver
from selenium_lfj.ShowapiRequest import ShowapiRequest
from selenium_lfj.find_element import FindElement


class GetCode():
    def __init__(self, driver):
        self.driver = driver

    def get_code_image(self, file_name):
        print(8.2)
        self.driver.save_screenshot(file_name)
        code_element = self.driver.find_element_by_id('getcode_num')
        left = code_element.location["x"]
        top = code_element.location["y"]
        rigth = code_element.size['width'] + left
        height = code_element.size['height'] + top
        im = Image.open(file_name)
        img = im.crop((left, top, rigth, height))
        img.save(file_name)
        print('code_image')
        print(1)
        time.sleep(5)
        print(8.21)

    # 解析图片
    # file_path=是验证code码
    def code_online(self, file_name):
        self.get_code_image(file_name)
        print(8.3)
        r = ShowapiRequest("http://route.showapi.com/184-4", "95852", "11b2e667952d400596286de04efc4e03")
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addBodyPara("needMorePrecise", "0")
        r.addFilePara("image", file_name)  # 文件上传时设置
        res = r.post()
        text = res.json()["showapi_res_body"]["Result"]
        time.sleep(2)
        print(8.4)
        return text
