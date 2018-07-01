"""
添加各种自定义的断言，断言失败抛出AssertionError。
"""

__author__ = 'zhaicao'

def assertHTTPCode(response, code_list=None):
    res_code = response.status_code
    if not code_list:
        code_list = [200]
    if res_code not in code_list:
        # 抛出AssertionError，unittest会自动判别为用例Failure，不是Error
        raise AssertionError('响应code不在列表中！')