
"""
接口测试用例
"""
__author__ = 'zhaicao'

from utils import unittest
from utils.config import Config, REPORT_PATH
from utils.client import HTTPClient
from utils.log import logger
from utils.HTMLTestRunner import HTMLTestRunner
from utils.assertion import assertHTTPCode

class TestBaiDuHTTP(unittest.TestCase):
    URL = Config().getByKeys('websites', 'URL')

    def setUp(self):
        self.client = HTTPClient(url=self.URL, method='GET')

    def test_baidu_http(self):
        res = self.client.send()
        logger.debug(res.text)
        assertHTTPCode(res, [400])
        self.assertIn('百度一下，你就知道', res.text)

if __name__ == '__main__':
    report = REPORT_PATH + '/API_report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='接口自动测试', description='接口html报告')
        runner.run(TestBaiDuHTTP('test_baidu_http'))