#!/usr/bin/env python
# coding = UTF-8
#Author:Lucky,time:2020/11/20

from xlrd import open_workbook
import configparser

file_name = "/Users/lucky/Downloads/DaasApiTesting/case_data/case.xlsx"
class write_ini:
    def get_data_from_table(self,file_name):
        col_one_content = []
        table = open_workbook(file_name)  # 打开文件
        get_sheets = table.sheet_names()  # 获取excel的sheet页的名称，全部打印出来
        for i in get_sheets:
            get_each_sheet = table.sheet_by_name(i)  # 获取到每个sheet页的名称，单独打印
            count_rows = get_each_sheet.nrows  # 获取到当前sheet页的总行数
            # print(count_rows)
            for j in range(1, count_rows):  # 获取当前sheet页第一列除第一行外的所有内容
                # 返回该行所有单元格的数据组成的列表
                col_values = get_each_sheet.row_values(j, start_colx=0, end_colx=1)
                col_one_content.append(''.join(col_values))
        return (col_one_content)

    def write_Config_Ini(self):
        col_all_content = write_ini.get_data_from_table(self,file_name)
        config = configparser.ConfigParser()
        # set a number of parameter
        config.add_section("operation")
        for i in col_all_content:
            config.set("operation", "case_" + i, str(i))
        config.write(open('data.ini', "w"))  # 没有新建  存在打开

if __name__=="__main__":
    a = write_ini()
    a.get_data_from_table(file_name)
    a.write_Config_Ini()