"""
百度搜索测试Demo
"""
__author__ = 'zhaicao'

import time
# 引入重写的Testcase
from utils import unittest
from utils.config import Config, DATA_PATH
from utils.log import logger
from utils.file_reader import ExcelReader
from src.test.page.baidu_result_page import BaiDuMainPage, BaiDuResultPage


class TestBaiDu(unittest.TestCase):
    URL = Config().getByKeys('websites', 'URL')
    excel = DATA_PATH + '/data.xlsx'

    def sub_setUp(self):
        # 打开初始页面BaiDuMainPage，传入浏览器类型打开浏览器，获得当前页面的driver
        self.page = BaiDuMainPage(browser_type='chrome').get(self.URL, maximize_window=False)

    def sub_tearDown(self):
        self.page.quit()

    # 数据未分离测试单个查询条件
    def test_search2(self):
        """百度搜索测试"""
        with self.subTest(data='翟操'):
            print("搜索关键字:翟操")
            self.sub_setUp()
            self.page.search('翟操')
            time.sleep(2)
            self.page = BaiDuResultPage(self.page)
            self.assertEqual('百度_百度搜索', self.page.result_title, self)
            self.sub_tearDown()

    def test_search(self):
        '''
        测试百度搜索title中内容与查询关键字是否一致
        :return:
        '''
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                # BaiDuMainPage调用自身的search方法。类似于self.driver.search()
                self.page.search(d['search'])
                time.sleep(2)
                # 跳转到结果页面
                self.page = BaiDuResultPage(self.page)
                # 断言title
                try:
                    self.assertEqual('{}_百度搜索'.format(d['expection']), self.page.result_title)
                    links = self.page.result_links
                    for link in links:
                        logger.info(link.text)
                except:
                # 断言失败，截图
                    self.page.save_screen_shot()
                    raise AssertionError('Title Error')
                finally:
                    self.sub_tearDown()

    def test_out(self):
        self.assertEqual('Test', '1')