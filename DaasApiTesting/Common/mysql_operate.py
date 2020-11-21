# -*- coding: utf-8 -*-
# @Time    : 2020/10/25 8:56 AM
# @Author  : Hui
# @File    : mysql_operate.py

from Config.config import *
import pymysql

class MySQLOperate():
    '''
        mysql执行器
    '''
    def __init__(self,DB):

        self.db = pymysql.Connect(
            host=DB_IP,
            user=DB_NAME,
            password=DB_PASSWORD,
            database=DB,
            port=PORT
        )

    def execute_sql(self,sql):
        '''
        执行sql
        :param sql: 增删改查
        :return:
        '''
        cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)
        result = cursor.execute(sql)
        if sql.lower().startswith("select"):
            return cursor.fetchone()
        else:
            self.db.commit()
            return result
        # return cursor.fetchone()


if __name__ == '__main__':
    print(MySQLOperate("test").execute_sql("select *from student" ))