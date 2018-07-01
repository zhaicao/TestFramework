"""
页面操作的封装。百度测试首页
"""

__author__ = 'zhaicao'

from selenium.webdriver.common.by import By
from src.test.common.page import Page

class BaiDuMainPage(Page):
    loc_search_input = (By.ID, 'kw')
    loc_search_button = (By.ID, 'su')

    def search(self, kw):
        """
         搜索功能。调用自身父类(Page)的find_element方法
        :param kw: 关键字
        """
        self.find_element(*self.loc_search_input).send_keys(kw)
        self.find_element(*self.loc_search_button).click()