"""
重写unittest的部分方法
"""
__author__ = 'zhaicao'

import unittest
# 引入装饰器
from utils.decoraters import deco

_MAX_LENGTH = 80

def safe_repr(obj, short=False):
    try:
        result = repr(obj)
    except Exception:
        result = object.__repr__(obj)
    if not short or len(result) < _MAX_LENGTH:
        return result
    return result[:_MAX_LENGTH] + ' [truncated]...'

# 重写TestCase
class TestCase(unittest.TestCase):
    # 加上用例异常截图装饰器
    @deco.exceptionCase
    def assertEqual(self, first, second, pageObj=None, msg=None):
        """Fail if the two objects are unequal as determined by the '=='
           operator.
        """
        assertion_func = self._getAssertEqualityFunc(first, second)
        assertion_func(first, second, msg=msg)

    # 加上用例异常截图装饰器
    @deco.exceptionCase
    def assertNotEqual(self, first, second, pageObj=None, msg=None):
        """Fail if the two objects are equal as determined by the '!='
           operator.
        """
        if not first != second:
            msg = self._formatMessage(msg, '%s == %s' % (self.safe_repr(first),
                                                         self.safe_repr(second)))
            raise self.failureException(msg)

# 继承TestSuite
class TestSuite(unittest.TestSuite):
    pass