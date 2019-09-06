
from utils import unittest
from src.test.case.UI.test_baidu import TestBaiDu
from utils.config import REPORT_PATH
from utils.mail import Email
from utils.HTMLTestRunner import HTMLTestRunner

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