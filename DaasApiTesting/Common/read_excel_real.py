# -*- coding: utf-8 -*-
# @Time    : 2020/10/25 8:53 AM
# @Author  : Hui、shangyanwen
# @File    : read_excel.py
from xlrd import open_workbook
from Config.config import *
from Common.test_base import *
from xlrd import open_workbook
import configparser
excel_path=ROOT_PATH + "/case_data/case.xlsx"
cfg1='/Users/lucky/Desktop/Auto/Daas_Interface/python_Interface_new/DaasApiTesting/Config/module_run.ini'

def read_excel_write_ini(excel_path):
    table = open_workbook(excel_path)  # 打开文件
    get_sheets = table.sheet_names()  # 获取excel的sheet页的名称，全部打印出来
    print("@@@@@@@@@@@@@@@@@@@@2")
    print(get_sheets)
    print(type(get_sheets))
    config = configparser.ConfigParser()
    # set a number of parameter
    config.add_section("operation")
    # for i in get_sheets:
    config.set("operation","module_run", str(get_sheets))
    config.write(open(cfg1, "w"))  # 没有新建  存在打开
read_excel_write_ini(excel_path)


def read_excel(excel_path):
    conf = configparser.ConfigParser()
    # cfg1="/Users/lucky/Desktop/Auto/Daas_Interface/python_Interface_new/DaasApiTesting/Config/module_run.ini"
    conf.read(cfg1)
    get_sheets1 = conf.get("operation","module_run")
    print("*********--------************")
    get_sheets=''.join(get_sheets1)
    print(type(''.split(get_sheets)))
    print("*********--------************")

    # get_sheets = table.sheet_names()  # 获取excel的sheet页的名称，全部打印出来
    all_rows = []  # 获取到Excel表中的所有行数，已[]的形式添加的[]中，格式为：[[][]]
    rows_dict2 = ''  # 每行的内容已字典的形式添加到列表中，格式为:[{}{}]
    table = open_workbook(excel_path)  # 打开文件
    # # 读取ini文件中的内容
    for i in get_sheets:
        rows_dict = []
        get_each_sheet = table.sheet_by_name(i)  # 获取到每个sheet页的名称，单独打印
        count_rows = get_each_sheet.nrows  # 获取到当前sheet页的总行数
        first_row = get_each_sheet.row_values(0)
        for j in range(count_rows):
            # 返回该行所有单元格的数据组成的列表
            col_values = get_each_sheet.row_values(j, start_colx=0, end_colx=None)  # 获取第一行的内容

            if j == 0:  # 跳过第一行
                continue
            all_rows.append(col_values)
        for row in all_rows:
            if is_run.upper() == "ALL":
                lis = dict(zip(first_row, row))
                rows_dict.append(lis)
            elif is_run.upper() == "NO":
                lis = dict(zip(first_row, row))
                if lis.get("is_run").upper() == "NO":
                    rows_dict.append(lis)
            elif is_run.upper() == "YES":
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
