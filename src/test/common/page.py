"""
封装Page通用变量方法
"""

__author__ = 'zhaicao'

from src.test.common.browser import Brower

class Page(Brower):
    """
    继承Brower，封装page相关操作
    """
    def __init__(self, page=None, browser_type='chrome'):
        """
        初始化页面的driver。若page存在则获得page的webDriver，反之则调用父类构造方法获得获得浏览器本身对象(空webDriver)
        :param page:
        :param browser_type:
        """
        if page:
            self.driver = page.driver
        else:
            super(Page, self).__init__(browser_type=browser_type)

    def get_driver(self):
        """
        获得webDriver
        """
        return self.driver

    def find_element(self, *args):
        """
        找单个元素
        :param args: By对象
        :return:单个元素对象
        """
        return self.driver.find_element(*args)

    def find_elements(self, *args):
        """
        找多个元素
        :param args: By对象
        :return: 多个元素List
        """
        return self.driver.find_elements(*args)
