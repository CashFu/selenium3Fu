# coding=utf-8
# 总结添加log有两种方式：一个加入到字节流，输出到控制台、另一个是柄句，输出到文件夹
import logging
import os
import datetime


class UserLog(object):
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 创建一个字节流--工作台
        # console = logging.StreamHandler()
        # logger.addHandler(console)
        # logger.debug('test')


        # 文件名字
        base_dir = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.path.join(base_dir, 'logs')
        log_file = datetime.datetime.now().strftime('%Y-%m-%d-%H-%m') + '.log'
        log_name = log_dir + '/' + log_file
        # 文件输出到日志
        self.file_handle = logging.FileHandler(log_name, 'a', encoding='utf-8')
        self.file_handle.setLevel(logging.INFO)
        formatter = logging.Formatter(
            '%(asctime)s %(filename)s %(funcName)s  %(levelname)s-->> %(levelno)s line: %(message)s')
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)
        # self.logger.debug('cuo')

    def get_log(self):
        return self.logger

    def close_handle(self):
        self.logger.removeHandler(self.file_handle)
        self.file_handle.close()


if __name__ == '__main__':
    user_log = UserLog()
    user_log.get_log()
    user_log.close_handle()
