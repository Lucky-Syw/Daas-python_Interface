#!/usr/bin/env python
# coding = UTF-8
#Author:Lucky,time:2020/12/2

from Config.config import *
from xlrd import open_workbook
import configparser

def read_excel_write_ini(excel_path=ROOT_PATH + "/case_data/case.xlsx"):
    '''
    :param excel_path: 测试用例的存放路径
    :purpose：获取excel文件中的sheet页名称，并写入到module_run.ini文件中
    '''
    table = open_workbook(excel_path)  # 打开文件
    get_sheets = table.sheet_names()  # 获取excel的sheet页的名称，全部打印出来
    print(get_sheets)
    config = configparser.ConfigParser()
    # set a number of parameter
    config.add_section("Module")
    config.add_section("Case")
    # for i in get_sheets:
    config.set("Module","module_run", str(get_sheets))
    config.set("Case", "case_run", "ALL")
    config.write(open('module_run.ini', "w"))  # 没有新建  存在打开

read_excel_write_ini()