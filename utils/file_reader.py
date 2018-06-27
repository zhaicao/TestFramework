"""
封装读取Yaml文件的类
"""
__author__ = 'zhaicao'

import yaml
import os


class YamlReader():
    def __init__(self, yamlfile):
        if os.path.exists(yamlfile):
            self.yamlfile = yamlfile
        else:
            raise FileNotFoundError('Yaml文件不存在！')
        self._data = None

    @property
    def data(self):
        if not self._data:
            with open(self.yamlfile, 'rb') as f:
                self._data = list(yaml.safe_load_all(f)) # load后是个generator，用list组织成列表
        return self._data