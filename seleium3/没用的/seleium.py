import base64
import random
import time

from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# 秘钥123456
from selenium_lfj.ShowapiRequest import ShowapiRequest

driver = webdriver.Chrome()
driver.get('http://www.5itest.cn/register')
time.sleep(3)

# 0、判断title是否打开了
print(EC.title_contains('注册'))

# 元素可不可见
el = driver.find_elements_by_class_name('controls')
locator = (By.CLASS_NAME, 'controls')
WebDriverWait(driver, 1).until(EC.visibility_of_element_located(locator))

#1、输入并获取邮箱中参数
emaile_element = driver.find_element_by_id('register_email')
emaile_element.get_attribute('placeholder')
emaile_element.send_keys('1213@123.com')
print(emaile_element.get_attribute('value'))

# 制造邮箱地址
for i in range(5):
    user_email = ''.join(random.sample('1234567890asdfghjk', 5))+'126.com'
    print(user_email)

# 2、输入用户名
# driver.find_element_by_id('register_email').send_keys('1112345@qq.com')
user_name_element_node = driver.find_elements_by_class_name('controls')[1]
user_element =user_name_element_node.find_element_by_class_name('form-control')
user_element.send_keys('用户名')



# 4、输入密码
driver.find_element_by_name('password').send_keys('123456')

# 5.1 保存图片
driver.save_screenshot(r'G:\seleium3\c.png')
code_element = driver.find_element_by_id('getcode_num')
print(code_element.location) #{'x':  'y'}
left = code_element.location["x"]
print(left)
top = code_element.location["y"]
rigth = code_element.size['width']+left
height = code_element.size['height']+top
im = Image.open(r'G:\seleium3\c.png')
img = im.crop((left,top,rigth,height))
img.save(r'G:\seleium3\c1.png')

r = ShowapiRequest("http://route.showapi.com/184-4","95852","11b2e667952d400596286de04efc4e03" )
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")

data=base64.b64encode( r"G:\seleium3\c1.png".encode('utf-8'))
data2= str(data,'utf-8')
r.addFilePara("imge",data2) #文件上传时设置
res = r.post()
print(res.text) # 返回信息
# res = r.post()
# text = res.json()['showapi_res_body']
# print(res.text) # 返回信息

# 5、输入验证码
driver.find_element_by_xpath('//*[@id="captcha_code"]').send_keys(text)

time.sleep(2)
driver.quit()
