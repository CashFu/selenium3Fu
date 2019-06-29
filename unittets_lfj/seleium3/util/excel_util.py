# coding=utf-8
import os

import xlrd

import xlutils
from xlutils.copy import copy


# 拿到ex测开中的数据--可写入、读取
class ExcelUtil:
    def __init__(self, excel_path=None, index=None):
        if excel_path == None:
            path_file = os.getcwd()
            file_name = os.path.abspath(os.path.dirname(path_file) + '/config/' + 'casedata.xls')
            self.excel_path = file_name
        else:
            self.excel_path =excel_path
        if index == None:
            index = 0
        self.data = xlrd.open_workbook(self.excel_path)
        # index代表那个sheet页
        self.table = self.data.sheets()[index]

        # [[],[]]

    # 获取Excel中的数据，按照每一个list，添加到大的list中
    def get_data(self):
        result = []
        # 限制总行数
        rows = self.get_lines()
        if rows != None:
            for i in range(rows):
                col = self.table.row_values(i)
                result.append(col)
            return result
        return None

    # 读Excel的行数
    def get_lines(self):
        # 获取行数
        rows = self.table.nrows
        # 判断行数
        if rows >= 1:
            return rows
        return None

    # 读单元格的数据
    def get_col_value(self, row, col):

        if self.get_lines() > row:
            data = self.table.cell(row, col).value
            return data
        return None

    # 写入数据  写入行 列
    def write_value(self, row, value):
        # 读取--全部的数据
        read_value = xlrd.open_workbook(self.excel_path)
        # 复制Excel一份数据
        write_data = copy(read_value)
        write_data.get_sheet(0).write(row, 9, value)
        # 保存数据
        path_file = os.getcwd()
        file_name1 = os.path.abspath(os.path.dirname(path_file) + '/config/' + 'keyword.xls')
        # write_data.save(r'G:\unittets_lfj\seleium3\config\keyword.xls')
        write_data.save(self.excel_path)

if __name__ == '__main__':
    path_file = os.getcwd()
    file_name = os.path.abspath(os.path.dirname(path_file) + '/config/' + 'keyword.xls')

    ex = ExcelUtil(excel_path=file_name)
    # ex.write_value(7,'123')
    # ex = ExcelUti、ol_value(1, 4))
    # print(ex.get_data())
