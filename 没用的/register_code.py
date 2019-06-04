import random
import time

from PIL import Image
from selenium import webdriver

# 秘钥123456
from selenium_lfj.ShowapiRequest import ShowapiRequest

driver = webdriver.Chrome()

# 浏览器初始化
def driver_int():
    driver.get('http://www.5itest.cn/register')
    driver.maximize_window()
    time.sleep(3)

# 获取element信息
def  get_element(id):
    element = driver.find_element_by_id(id)
    return element

# 获取随机数
def get_range_user():
    user_info = ''.join(random.sample('1234567890asdfghjk', 5))
    return user_info

# 保存图片

def get_code_image (file_path):
    driver.save_screenshot(file_path)
    code_element = driver.find_element_by_id('code_image')
    left = code_element.location["x"]
    top = code_element.location["y"]
    rigth = code_element.size['width'] + left
    height = code_element.size['height'] + top
    im = Image.open(file_path)
    img = im.crop((left, top, rigth, height))
    img.save(file_path)

# 解析图片
def code_online(file_path):
    r = ShowapiRequest("http://route.showapi.com/184-4", "95852", "11b2e667952d400596286de04efc4e03")
    r.addBodyPara("typeId", "35")
    r.addBodyPara("convert_to_jpg", "0")
    r.addBodyPara("needMorePrecise", "0")
    r.addFilePara("image", file_path)  # 文件上传时设置
    res = r.post()
    text = res.json()["showapi_res_body"]["Result"]
    return text

# 运行程序
def run():
    driver_int()
    user_nickname = get_range_user()
    user_email = user_nickname +'@126.com'
    file_path = r'G:\seleium3\c.png'
    get_element('register_email').send_keys(user_email)
    get_element('register_nickname').send_keys(user_nickname)
    get_element('register_password').send_keys(user_nickname)
    get_code_image(file_path)
    text = code_online(file_path)
    get_element('captcha_code').send_keys(text)
    get_element('register-btn').click()

    driver.quit()

if __name__ == '__main__':
    run()