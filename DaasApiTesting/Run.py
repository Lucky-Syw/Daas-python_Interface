# -*- coding: utf-8 -*-
# @Time    : 2020/3/6 上午10:38
# @Author  : Hui
# @File    : manage.py
from Config.config import *
import Common.HTMLTestRunner
import unittest
import pytest
import time
from test_Case.test_case import Test
from test_Case import test_case
import test_Case

class run:

	def pytest_report_style(self):
		'''pytest的方式运行'''
		now = time.strftime("%Y-%m-%d_%H_%M_%S")
		pytest.main(['-s',TESTCASE_PATH+"/test_case.py" , '--html=report/DaaSApiTesting{}_report.html'.format(now)])
		# import subprocess
		# subprocess.call(['pytest', '--tb=short', str(__file__),'--html=report/DaaSApiTesting{}_report.html'.format(now)])

	def unittest_report_style(self):
		'''unittest的方式运行'''
		s = unittest.TestSuite()  # 实例化
		s.addTests(unittest.TestLoader().loadTestsFromTestCase(Test))  # 加载用例
		record_time =  time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		# 定义报告存放路径
		filename = REPORT_PATH +record_time+ '_ReportResult.html'
		fp=open(filename,'wb')
		#定义测试报告
		runner=Common.HTMLTestRunner.HTMLTestRunner(stream=fp, title='Daas_接口测试报告', retry =2, description='接口用例输出如下：')
		runner.run(s)
		# 关闭报告文件
		fp.close()
	def unittest_report_style2(self):
		#待添加utx中的报告样式
		pass

if __name__ == '__main__':
	real_run = run()
	real_run.pytest_report_style()   #使用哪个报告，此处调用如上的方法即可