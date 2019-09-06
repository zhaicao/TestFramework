"""
百度首页
"""

__author__ = 'zhaicao'

from selenium.webdriver.common.by import By
from src.test.common.page import Page

class BaiDuMainPage(Page):
    # 定义首页需要测试的元素

    loc_search_input = (By.ID, 'kw')
    loc_search_button = (By.ID, 'su')


    #下面定义在A页面索要进行的所有操作
    def search(self, kw):
        """
         搜索功能。调用自身父类(Page)的find_element方法
        :param kw: 关键字
        """
        self.find_element(*self.loc_search_input).send_keys(kw)
        self.find_element(*self.loc_search_button).click()

    # 跳转到新闻
    def cliecknews(self, kw):
        """
                 搜索功能。调用自身父类(Page)的find_element方法
                :param kw: 关键字
                """
        self.find_element(*self.loc_search_input).send_keys(kw)
        self.find_element(*self.loc_search_button).click()