"""
封装测试页面的对象和方法
"""

__author__ = 'zhaicao'

from selenium.webdriver.common.by import By
from src.test.page.baidu_main_page import BaiDuMainPage
from src.test.common.page import Page

class BaiDuResultPage(Page):
    loc_result_links = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    @property
    def result_links(self):
        """
        self为自身的
        :return:
        """
        return self.find_elements(*self.loc_result_links)

    @property
    def result_title(self):
        return self.get_driver().title