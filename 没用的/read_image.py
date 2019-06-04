#conding=utf-8
import base64

import pytesseract
from PIL import Image
image = Image.open(r'G:\seleium3\c1.png')
# 识别率低
# text = pytesseract.image_to_string(image=image)
# print(text )


from ShowapiRequest import ShowapiRequest
# 秘钥123456
r = ShowapiRequest("http://route.showapi.com/184-5","95852","11b2e667952d400596286de04efc4e03" )
r.addBodyPara("img_base64", "")
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
with open(r'G:\seleium3\c1.png', 'rb') as f:
    data = base64.b64encode(f.read())

r.addFilePara("imge", data) #文件上传时设置
res = r.post()
# text= res.json(['showapi_res_body'],['Result'])
print(res.text) # 返回信息


