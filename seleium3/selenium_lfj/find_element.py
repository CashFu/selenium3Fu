#coding=utf-8
from util.read_ini import ReadIni
class FindElement():
    def __init__(self,driver):
        self.driver = driver

    def get_element(self,key):
        read_ini = ReadIni()
        data_ini = read_ini.get_value(key)
        by = data_ini.split('>')[0]
        value = data_ini.split('>')[1]
        try:
            if by =='id':
                return self.driver.find_element_by_id(value)
            elif by=='name':
                return self.driver.find_element_by_name(value)
            elif by=='className':
                return self.driver.find_element_by_class_name(value)
            else:
                return self.driver.find_element_by_xpath(value)
        except:
            return '没有找到定位的元素！'
