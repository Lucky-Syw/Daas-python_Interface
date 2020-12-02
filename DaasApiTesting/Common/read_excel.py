# -*- coding: utf-8 -*-
# @Time    : 2020/10/25 8:53 AM
# @Author  : Hui、shangyanwen
# @File    : read_excel.py

from Config.config import *
from Common.test_base import *
from xlrd import open_workbook
import configparser

cfg1 = Config_PATH + "/module_run.ini"

def read_excel(excel_path=ROOT_PATH + "/case_data/case.xlsx"):
    conf = configparser.ConfigParser()
    conf.read(cfg1)
    get_module = conf.get("Module","module_run")  #获取到module_run.ini文件中的operation
    get_case = conf.get("Case","case_run")
    get_module2=''.join(get_module)
    get_module3=eval(get_module2)  #因是字符串类型，用eval转为list类型
    all_rows = []  # 获取到Excel表中的所有行数，已[]的形式添加的[]中，格式为：[[][]]
    rows_dict2 = ''  # 每行的内容已字典的形式添加到列表中，格式为:[{}{}]
    table = open_workbook(excel_path)  # 打开文件
    for i in get_module3:
        rows_dict = []
        print(i)
        get_each_sheet = table.sheet_by_name(i)  # 获取到每个sheet页的名称，单独打印
        print(get_each_sheet)
        count_rows = get_each_sheet.nrows  # 获取到当前sheet页的总行数
        first_row = get_each_sheet.row_values(0)
        for j in range(count_rows):
            # 返回该行所有单元格的数据组成的列表
            col_values = get_each_sheet.row_values(j, start_colx=0, end_colx=None)  # 获取第一行的内容
            if j == 0:  # 跳过第一行
                continue
            all_rows.append(col_values)
        for row in all_rows:
            if get_case.upper() == "ALL":
                lis = dict(zip(first_row, row))
                rows_dict.append(lis)
            elif get_case.upper() == "NO":
                lis = dict(zip(first_row, row))
                if lis.get("is_run").upper() == "NO":
                    rows_dict.append(lis)
            elif get_case.upper() == "YES":
                lis = dict(zip(first_row, row))
                if lis.get("is_run").upper() == "NO":
                    continue
                rows_dict.append(lis)
            else:
                logger.info("-------------------------")
        rows_dict2 = rows_dict
    print("******************---rows_dict2")
    return rows_dict2

# read_excel(excel_path)
