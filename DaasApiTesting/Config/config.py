# -*- coding: utf-8 -*-
# @Time    : 2020/3/6 下午12:02
# @Author  : Hui
# @File    : config.py

import os

# 是否指定用例  开关
IS_RUN_ALL = True


# 获取项目路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_PATH = os.path.abspath(os.path.dirname(__file__)[:-7])
print(ROOT_PATH)
# 定义测试用例的路径
TESTCASE_PATH = os.path.join(ROOT_PATH, 'test_Case')
# 定义测报告的路径
REPORT_PATH = os.path.join(BASE_PATH, 'Report/')
# 定义日志文件的路径
LOG_PATH = os.path.join(ROOT_PATH, 'logs/log.log')

# mysql数据库的连接信息
DB_NAME = 'root'
DB_PASSWORD = 'root'
DB_IP = '39.105.34.24'
PORT = 3306

# redis数据库的连接信息
REDIS_HOST = '10.54.16.9'
REDIS_PORT = 6379
REDIS_PASSWORD = 'wYgXEBujiLq@'

# host
TEST_HOST = 'http://daas.test.deepexi.top'


