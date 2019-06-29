# coding=utf-8
import os

from util.excel_util import ExcelUtil
from keywords.actionMethod import ActionMethod


# 此文件中操作Excel中的数据，有的单元格没有数据，判断时候 ‘’而不是None
class KeywordCase():
    def run_main(self):
        self.action_method = ActionMethod()
        path_file = os.getcwd()
        file_name = os.path.abspath(os.path.dirname(path_file) + '/config/' + 'keyword.xls')
        #     4.else 没有输入的数据
        #         执行方法（操作元素）
        handle_excle = ExcelUtil(excel_path=file_name)
        # 1.拿到行数
        cae_lines = handle_excle.get_lines()
        # 2.循环行数，去执行每一行的case从第1行开始
        for i in range(1, cae_lines):
            #     1.拿到执行方法,回归执行
            is_run = handle_excle.get_col_value(i, 3)
            # print(is_run)
            #     2.拿到操作值‘
            #     3.if 是否有输入的数据
            #         执行方法（输入数据-->>操作元素）
            if is_run == 'yes':
                # 执行方法
                method = handle_excle.get_col_value(i, 4)
                # 输入的数据
                send_value = handle_excle.get_col_value(i, 5)
                # print(send_value)
                # 操作元素
                handle_value = handle_excle.get_col_value(i, 6)
                # 预期结果
                except_result_method = handle_excle.get_col_value(i, 7)
                # 预期结果值
                except_result = handle_excle.get_col_value(i, 8)

                self.run_method(method, send_value, handle_value)
                if except_result != '':
                    except_value = self.get_except_result_value(except_result)
                    # 判断获取预期结果的值-两种情况text element
                    if except_value[0] == 'text':
                        result = self.run_method(except_result_method)
                        # print(except_result_method)
                        if except_value[1] in result:
                            handle_excle.write_value(i, 'pass')
                        else:
                            handle_excle.write_value(i, 'fail')
                    elif except_value[0] == 'element':
                        # except_value[1]就是等于handle_value
                        result = self.run_method(except_result_method, except_value[1])
                        if result:
                            handle_excle.write_value(i, 'pass')
                        else:
                            handle_excle.write_value(i, 'fail')
                    else:
                        print('没有else')
                else:
                    print('预期结果为空')

    # 获取预期结果的值
    def get_except_result_value(self, data):
        # 返回的是列表
        return data.split('=')

    # Excel中有数据--是否执行：yes ;method--执行方法：获取文字、获取title、获取元素；
    #  4中情况

    def run_method(self, method, send_value='', handle_value=''):
        method_value = getattr(self.action_method, method)
        # 有值则获取操作词send_value--场景就是类似打开浏览器
        if send_value == '' and handle_value != '':
            result = method_value(handle_value)
        # 若是没有输入的数据，则直接操作元素
        # 不是空而是没有输入数据---场景就是类似全部有值输入操作元素
        elif send_value == '' and handle_value == '':
            result = method_value()
        # 预期结果这使用：预期结果 为空；预期结果值不为空
        elif send_value != '' and handle_value == '':
            result = method_value(send_value)
        else:
            result = method_value(send_value, handle_value)
        return result


if __name__ == '__main__':
    key_wordcase = KeywordCase()
    key_wordcase.run_main()
