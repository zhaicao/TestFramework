"""
页面结果。百度测试结果
"""

__author__ = 'zhaicao'

from selenium.webdriver.common.by import By
from src.test.page.baidu_main_page import BaiDuMainPage

class BaiDuResultPage(BaiDuMainPage):
    loc_result_links = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    @property
    def result_links(self):
        """
        self为自身的
        :return:
        """
        return self.find_elements(*self.loc_result_links)