# -*- coding: utf-8 -*-
# @Time    : 2020/10/25 8:53 AM
# @Author  : Hui
# @File    : read_excel.py

import xlrd
from Config.config import *
from Common.test_base import *

def read_excel(excel_path=ROOT_PATH + "/case_data/case.xlsx"):
    '''
    读取excel文件内容
    :param excel_path: xlsx文件的路径
    :param sheet_name: 表格名称
    :return: k-v的列表
    '''
    # 打开文件
    workbook = xlrd.open_workbook(excel_path)
    # 获取所有sheet
    # print(workbook.sheet_names())  # [u'sheet1', u'sheet2']
    # 根据sheet索引或者名称获取sheet内容
    sheet_name = ''.join(workbook.sheet_names())
    sheet = workbook.sheet_by_name(sheet_name)  # sheet索引从0开始
    # 获取第一行作为key
    first_row = sheet.row_values(0)  # 获取第一行内容
    # 获取表的行数
    rows_length = sheet.nrows
    # 定义两个空列表，存放每行的数据
    all_rows = []
    rows_dict = []
    for i in range(rows_length):  # 循环逐行打印
        if i == 0:  # 跳过第一行
            continue
        all_rows.append(sheet.row_values(i))
    ##---根据Excel中的is_run字段读取要执行的用例
    for row in all_rows:
     if is_run.upper() == "ALL":
        lis = dict(zip(first_row, row))
        rows_dict.append(lis)
     elif is_run.upper() =="NO":
        lis = dict(zip(first_row, row))
        if lis.get("is_run").upper() == "NO":
            rows_dict.append(lis)
     elif is_run.upper() =="YES":
         lis = dict(zip(first_row, row))
         if lis.get("is_run").upper() == "NO":
             continue
         rows_dict.append(lis)
     else:
        logger.info("-------------------------")
    print("000000000000000000000000000")
    print(all_rows)
    # print(rows_dict)
    return rows_dict





if __name__ == '__main__':
    print(read_excel())
