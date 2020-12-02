"""
#@file   : test_case.py
#@ide    : PyCharm
#@time   : 2020-05-28 12:37:01
"""

import unittest
from ddt import *
from Common.read_excel import *
from Common.test_base import *
import jsonpath
from Common.functons import *
from Common.mysql_operate import MySQLOperate
from Common.redis_operate import RedisOperate


@ddt
class Test(unittest.TestCase):
    api_data = read_excel()

    # 全局变量池
    saves = {}
    # 识别${key}的正则表达式
    EXPR = '\$\{(.*?)\}'
    # 识别函数助手
    FUNC_EXPR = '__.*?\(.*?\)'

    def save_data(self, source, key, jexpr):
        '''
        提取参数并保存至全局变量池
        :param source: 目标字符串
        :param key: 全局变量池的key
        :param jexpr: jsonpath表达式
        :return:
        '''
        value = jsonpath.jsonpath(source, jexpr)
        if value:
            self.saves[key] = value[0]
            logger.info("保存 {}=>{} 到全局变量池".format(key, value))
        else:
            logger.error("保存失败，参数为空")

    def build_param(self, _string):
        '''
        识别${key}并替换成全局变量池的value,处理__func()函数助手
        :param _string:
        :param str: 待替换的字符串
        :return:
        '''

        # 遍历所有取值并做替换
        keys = re.findall(self.EXPR, _string)
        for key in keys:
            value = self.saves.get(key)
            _string = _string.replace('${' + key + '}', str(value))

        # 遍历所有函数助手并执行，结束后替换
        funcs = re.findall(self.FUNC_EXPR, _string)
        for func in funcs:
            fuc = func.split('__')[1]
            fuc_name = fuc.split("(")[0]
            fuc = fuc.replace(fuc_name, fuc_name.lower())
            value = eval(fuc)
            _string = _string.replace(func, str(value))
        return _string

    def execute_setup_sql(self, db_connect, setup_sql):
        '''
        执行setup_sql,并保存结果至参数池
        :param db_connect: mysql数据库实例
        :param setup_sql: 前置sql
        :return:
        '''
        for sql in [i for i in setup_sql.split(";") if i != ""]:
            result = db_connect.execute_sql(sql)
            if sql.lower().startswith("select"):
                logger.info("执行前置sql====>{}，获得以下结果集:{}".format(sql, result))
                # 获取所有查询字段，并保存至公共参数池
                for key in result.keys():
                    self.saves[key] = result[key]
                    logger.info("保存 {}=>{} 到全局变量池".format(key, result[key]))

    def execute_teardown_sql(self, db_connect, teardown_sql):
        '''
        执行teardown_sql,并保存结果至参数池
        :param db_connect: mysql数据库实例
        :param teardown_sql: 后置sql
        :return:
        '''
        for sql in [i for i in teardown_sql.split(";") if i != ""]:
            result = db_connect.execute_sql(sql)
            if sql.lower().startswith("select"):
                logger.info("执行后置sql====>{}，获得以下结果集:{}".format(sql, result))
                # 获取所有查询字段，并保存至公共参数池
                for key in result.keys():
                    self.saves[key] = result[key]
                    logger.info("保存 {}=>{} 到全局变量池".format(key, result[key]))

    def execute_redis_get(self, redis_connect, keys):
        '''
        读取redis中key值,并保存结果至参数池
        :param redis_connect: redis实例
        :param keys:
        :return:
        '''
        for key in [key for key in keys.split(";") if key != ""]:
            value = redis_connect.get(key)
            self.saves[key] = value
            logger.info("保存 {}=>{} 到全局变量池".format(key, value))

    @classmethod
    def setUpClass(cls):
        # 实例化测试基类，自带cookie保持
        cls.request = BaseTest()

    @classmethod
    def tearDownClass(cls):
        pass

    @data(*api_data)
    @unpack
    def test_(self,case_num, descrption, url, method, headers, cookies, params, body, file, verify, saves, dbtype, db, setup_sql,
              teardown_sql):

        logger.info("============================================")
        logger.info(case_num,descrption,method)

        if case_num == "yes":
            logger.info("用例描述====>" + descrption)
            db_connect = None
            redis_db_connect = None
            setup_sql = self.build_param(setup_sql)
            teardown_sql = self.build_param(teardown_sql)

            # 判断数据库类型,暂时只有mysql,redis
            if dbtype.lower() == "mysql":
                db_connect = MySQLOperate(db)
            elif dbtype.lower() == "redis":
                redis_db_connect = RedisOperate(db)
            else:
                pass

            if db_connect:
                # 执行teardown_sql
                self.execute_setup_sql(db_connect, setup_sql)

            if redis_db_connect:
                # 执行teardown_redis操作
                self.execute_redis_get(redis_db_connect, teardown_sql)

            url = self.build_param(TEST_HOST+url)
            headers = self.build_param(headers)
            params = self.build_param(params)
            body = self.build_param(body)
            params = eval(params) if params else params
            headers = eval(headers) if headers else headers
            cookies = eval(cookies) if cookies else cookies
            body = eval(body) if body else body
            file = eval(file) if file else file

            res = None

            # 判断接口请求类型
            if method.upper() == 'GET':
                res = self.request.get_request(url=url, params=params, headers=headers, cookies=cookies)
            elif method.upper() == 'POST':
                res = self.request.post_request(url=url, headers=headers, cookies=cookies, params=params, json=body)
            elif method.upper() == 'UPLOAD':
                res = self.request.upload_request(url=url, headers=headers, cookies=cookies, params=params, data=body,
                                                  files=file)
            elif method.upper() == 'PUT':
                res = self.request.put_request(url=url, headers=headers, cookies=cookies, params=params, data=body)
            elif method.upper() == 'DELETE':
                res = self.request.delete_request(url=url, headers=headers, cookies=cookies, params=params, data=body)
            else:
                pass  # 待扩展

            if db_connect:
                # 执行teardown_sql
                self.execute_teardown_sql(db_connect, teardown_sql)

            if saves:
                # 遍历saves
                for save in saves.split(";"):
                    # 切割字符串 如 key=$.data
                    key = save.split("=")[0]
                    jsp = save.split("=")[1]
                    self.save_data(res.json(), key, jsp)

            if verify:
                # 遍历verify:
                if verify.endswith(";"):
                    verify = verify.split(";")[0]
                for ver in verify.split(";"):
                    expr = ver.split("=")[0]
                    # 判断Jsonpath还是正则断言
                    if expr.startswith("$."):
                        actual = jsonpath.jsonpath(res.json(), expr)
                        if not actual:
                            logger.error("该jsonpath未匹配到值,请确认接口响应和jsonpath正确性")
                        actual = actual[0]
                    else:
                        actual = re.findall(expr, res.text)[0]
                    expect = ver.split("=")[1]
                    self.request.assertEquals(str(actual), expect)

            # 最后关闭mysql数据库连接
            if db_connect:
                db_connect.db.close()
