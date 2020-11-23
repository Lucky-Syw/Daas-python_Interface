# -*- coding: utf-8 -*-
# @Time    : 2020/3/6 上午10:38
# @Author  : Hui
# @File    : manage.py
from Config.config import *

if __name__ == '__main__':
	# API test Run
	import pytest
	import time

	now = time.strftime("%Y-%m-%d_%H_%M_%S")
	pytest.main(['-s',TESTCASE_PATH+"/test_case.py" , '--html=report/DaaSApiTesting{}_report.html'.format(now)])
