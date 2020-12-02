# -*- coding: utf-8 -*-
# @Time    : 2020/10/25 8:53 AM
# @Author  : Hui
# @File    : read_excel.py
################################这个页面是测试一些代码使用的，不用关注##############

from xlrd import open_workbook
# #
file_name = "/Users/lucky/Desktop/Auto/Daas_Interface/python_Interface_new/DaasApiTesting/case_data/case.xlsx"

def getdatafromtable(file_name):
    table=open_workbook(file_name)   #打开文件
    get_sheets = table.sheet_names()    #获取excel的sheet页的名称，全部打印出来
    print(get_sheets)
    for i in get_sheets:
        get_each_sheet = table.sheet_by_name(i)  #获取到每个sheet页的名称，单独打印
        print("________________________________________")
        print(get_each_sheet.name)
        count_rows = get_each_sheet.nrows   #获取到当前sheet页的总行数
        print(count_rows)
        for j in range(count_rows):
            # 返回该行所有单元格的数据组成的列表
            col_values = get_each_sheet.row_values(j, start_colx=0, end_colx=None)
            print("################################")
            print(col_values)

getdatafromtable(file_name)


# a = [['cc','dd'],['aa','bb']]
# b = [ i for item in a for i in item]
# print(b)