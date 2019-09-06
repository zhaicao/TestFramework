"""
数据库
封装常规数据库操作的
"""
__author__ = 'zhaicao'

# Value为对应浏览器的webdriver对象
TYPES = ['mysql', 'sqlserver', 'oracle']

import pymysql
import pymssql

# 定义不支持异常
class UnSupportDatabaseTypeError(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self)
        self.errorinfo = ErrorInfo

    def __str__(self):
        return 'Do not supprt the type of database,please change the others.{}'.format(self.errorinfo)

class Database(object):
    def __init__(self, db_type='mysql', **kwargs):
        """
        根据参数获得对应的db实例
        :param db_type: 数据库类别
        """
        self._type = db_type.lower()
        if self._type in TYPES:
            if self._type == 'mysql':
                self.db = Mysql(**kwargs)
            elif self._type == 'mysql':
                self.db = MSSQL(**kwargs)
            else:
                self.db = None
        else:
            ('不支持')

class Mysql:
    '''python操作mysql的增删改查的封装'''
    def __init__(self, **kwargs):
        '''
        初始化参数
        :param host: 主机
        :param user: 用户名
        :param password: 密码
        :param database: 数据库
        :param port: 端口号，默认是3306
        :param charset: 编码，默认是utf8
        '''
        self.host = kwargs.get('host')
        self.port = kwargs.get('port', '3306')
        self.database = kwargs.get('database')
        self.user = kwargs.get('user')
        self.password = kwargs.get('password')
        self.charset = kwargs.get('charset', 'utf-8')

    def connect(self):
        '''
        获取连接对象和执行对象
        :return:
        '''
        self.conn = pymysql.connect(host=self.host,
        user=self.user,
        password=self.password,
        database=self.database,
        port=self.port,
        charset=self.charset)
        self.cur = self.conn.cursor()

    def fetchone(self, sql, params=None):
        '''
        根据sql和参数获取一行数据
        :param sql: sql语句
        :param params: sql语句对象的参数元组，默认值为None
        :return: 查询的一行数据
        '''
        dataOne = None
        try:
            count = self.cur.execute(sql, params)
            if count != 0:
                dataOne = self.cur.fetchone()
        except Exception as ex:
            print(ex)
        finally:
            self.close()
        return dataOne

    def fetchall(self, sql, params=None):
        '''
        根据sql和参数获取一行数据
        :param sql: sql语句
        :param params: sql语句对象的参数列表，默认值为None
        :return: 查询的一行数据
        '''
        dataall = None
        try:
            count = self.cur.execute(sql, params)
            if count != 0:
            dataall = self.cur.fetchall()
        except Exception as ex:
            print(ex)
        finally:
            self.close()
        return dataall

    def __item(self, sql, params=None):
        '''
        执行增删改
        :param sql: sql语句
        :param params: sql语句对象的参数列表，默认值为None
        :return: 受影响的行数
        '''
        count = 0
        try:
                count = self.cur.execute(sql, params)
                self.conn.commit()
        except Exception as ex:
                print(ex)
        finally:
                self.close()
        return count

    def update(self, sql, params=None):
        '''
        执行修改
        :param sql: sql语句
        :param params: sql语句对象的参数列表，默认值为None
        :return: 受影响的行数
        '''
        return self.__item(sql, params)

    def insert(self, sql, params=None):
        '''
        执行新增
        :param sql: sql语句
        :param params: sql语句对象的参数列表，默认值为None
        :return: 受影响的行数
        '''
        return self.__item(sql, params)

    def delete(self, sql, params=None):
        '''
        执行删除
        :param sql: sql语句
        :param params: sql语句对象的参数列表，默认值为None
        :return: 受影响的行数
        '''
        return self.__item(sql, params)

    def close(self):
        '''
        关闭执行工具和连接对象
        '''
        if self.cur != None:
                self.cur.close()
        if self.conn != None:
                self.conn.close()

class MSSQL:
    '''
    封装Sqlserver操作，待完善
    '''
    def __init__(self,**kwargs):
        '''
        初始化参数
        :param kwargs:
        '''
        self.dbInfo = kwargs

    def __GetConnect(self):
        '''
        获取连接对象和执行对象
        :return:
        '''
        self.conn = pymssql.connect(**self.dbInfo,charset = "utf8")
        cur = self.conn.cursor()
        if not cur:
            raise(NameError,"连接数据库失败")
        else:
            return cur

    def ExecQuery(self,sql):
        '''
        获取查询结果
        :param sql:
        :return:
        '''
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()
        self.conn.close()
        return resList

    def ExecNonQuery(self,sql):
        '''
        执行Sql
        :param sql:
        :return:
        '''
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()