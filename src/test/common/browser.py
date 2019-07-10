"""
封装浏览器通用方法
"""

__author__ = 'zhaicao'

import time
import os
from selenium import webdriver
from utils.config import DRIVER_PATH, REPORT_PATH

# 定义浏览器类别
CHROMEDRIVER_PATH = DRIVER_PATH + '\chromedriver.exe'
IEDRIVER_PATH = DRIVER_PATH + '\IEDriverServer.exe'
PHANTOMJSDRIVER_PATH = DRIVER_PATH + '\phantomjs.exe'

# Value为对应浏览器的webdriver对象
TYPES = {'firefox': webdriver.Firefox, 'chrome': webdriver.Chrome, 'ie': webdriver.Ie, 'phantomjs': webdriver.PhantomJS}
EXECUTABLE_PATH = {'firefox': 'wires', 'chrome': CHROMEDRIVER_PATH, 'ie': IEDRIVER_PATH, 'phantomjs': PHANTOMJSDRIVER_PATH}

# 定义不支持异常
class UnSupportBrowserTypeError(Exception):
    raise ('Do not supprt the type of browser,please change the others.')

class Brower(object):
    def __init__(self, browser_type='chrome'):
        """
        根据参数获得对应的driver
        :param browser_type: 浏览器类别
        """
        self._type = browser_type.lower()
        if self._type in TYPES:
            self.brower = TYPES[self._type]
        else:
            raise UnSupportBrowserTypeError('仅支持%s!' % ', '.join(TYPES.keys()))
        self.driver = None

    def get(self, url, maximize_window=True, implicitly_wait=30):
        """
        打开浏览器，获得页面的webDriver成员变量，并返回Browser类实例
        """
        self.driver = self.brower(executable_path=EXECUTABLE_PATH[self._type])
        self.driver.get(url)
        if maximize_window:
            self.driver.maximize_window()
        self.driver.implicitly_wait(implicitly_wait)
        return self

    def save_screen_shot(self, name='screen_shot'):
        """
        保存页面截图
        """
        day = time.strftime('%Y%m%d', time.localtime(time.time()))
        screenshot_path = os.path.join(REPORT_PATH, 'screenshot_%s' % day)
        if not os.path.exists(screenshot_path):
            os.makedirs(screenshot_path)

        tm = time.strftime('%H%M%S', time.localtime(time.time()))
        screenshot = self.driver.save_screenshot(screenshot_path + '\\%s_%s.png' % (name, tm))
        return screenshot

    def close(self):
        """
        关闭页面
        """
        self.driver.close()

    def quit(self):
        """
        退出driver
        """
        self.driver.quit()

if __name__ == '__main__':
    Brower().get('http://www.baidu.com').save_screen_shot()