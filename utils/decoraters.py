"""
装饰器，定义各种装饰器
"""
__author__ = 'zhaicao'

class deco(object):
    """
    装饰器类，定义装饰器函数
    """
    # 定义用例断言失败及截图
    def exceptionCase(func):
        def wrapper(self, first, second, pageObj=None, msg=None):
            try:
                func(self, first, second, pageObj=None, msg=None)
            except AssertionError:  # 等待AssertionError
                # 截图
                if pageObj:
                    pageObj.page.save_screen_shot()
                    pageObj.sub_tearDown()
                raise AssertionError(msg)  # 抛出AssertionError和信息

        return wrapper