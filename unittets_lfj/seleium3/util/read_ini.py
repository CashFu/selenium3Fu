# conding=utf-8

import configparser
import os


class ReadIni():
    def __init__(self, file_name=None, node=None):
        if file_name == None:
            # path_file = os.getcwd()
            # file_name = os.path.abspath(os.path.dirname(path_file)+'/config_file'+'/Config.ini')
            file_name= r"G:\unittets_lfj\seleium3\config_file\Config.ini"
        if node == None:
            self.node = 'register_element'
        else:
            self.node = node
        self.cf = self.load_ini(file_name)

    # 加载配置文件
    def load_ini(self, file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf

    # 配置文件的去value值，
    def get_value(self, key):
        data = self.cf.get(self.node, key)
        return data


if __name__ == '__main__':
    read_ini = ReadIni()
    # print(read_ini.get_value('user_email'))
