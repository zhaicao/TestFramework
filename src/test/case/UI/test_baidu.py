__author__ = 'zhaicao'

import os
import time
import unittest
from utils.config import Config, DATA_PATH, REPORT_PATH
from utils.log import logger
from utils.file_reader import ExcelReader
from utils.HTMLTestRunner import HTMLTestRunner
from utils.mail import Email
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
        with self.subTest(data='翟操'):
            self.sub_setUp()
            self.page.search('翟操')
            time.sleep(2)
            self.page = BaiDuResultPage(self.page)
            try:
                self.assertEqual('百度_百度搜索', self.page.result_title)
                links = self.page.result_links
                for link in links:
                    logger.debug(link.text)
            except:
                # 断言失败，截图
                self.page.save_screen_shot()
                raise AssertionError('Title Error')

            finally:
                self.sub_tearDown()

    # 数据分离用例
    def test_search(self):
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
                self.assertEqual('测试_百度搜索', self.page.result_title)
                links = self.page.result_links
                for link in links:
                    logger.info(link.text)
                self.sub_tearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    tests = [TestBaiDu("test_search")]
    suite.addTests(tests)

    # 测试报告
    report = REPORT_PATH + '/UI_report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f,
                                verbosity=2,
                                title='测试报告',
                                description='百度搜索测试')
        runner.run(suite)

    # 结果邮件
    e = Email(receiver='ricky2971@hotmail.com',
              acc='ricky2971@qq.com',
              title='百度搜索测试报告',
              message='最新鲜的测试报告，请各位查收！',
              path=report
              )
    e.send()
