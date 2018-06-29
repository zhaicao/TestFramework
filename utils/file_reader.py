"""
文件读取。YamlReader读取Yml文件，ExcelReader读取Excel
"""
__author__ = 'zhaicao'

import yaml
import os
from xlrd import open_workbook


class YamlReader(object):
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

class SheetTypeError(Exception):
    pass

class ExcelReader(object):
    """
       读取excel文件中的内容。返回list。
       如：
       excel中内容为：
       | A  | B  | C  |
       | A1 | B1 | C1 |
       | A2 | B2 | C2 |

       print(ExcelReader(excel, title_line=True).data)，输出结果：
       [{A: A1, B: B1, C:C1}, {A:A2, B:B2, C:C2}]

        print(ExcelReader(excel, title_line=False).data)，输出结果：
       [[A,B,C], [A1,B1,C1], [A2,B2,C2]]

       可以指定sheet，通过index或者name：
       ExcelReader(excel, sheet=2)
       ExcelReader(excel, sheet='BaiDuTest')
    """
    def __init__(self, excel, sheet=0, title_line=True):
        if os.path.exists(excel):
            self.excel = excel
        else:
            raise FileNotFoundError('文件不存在！')
        self.sheet = sheet
        self.title_line = title_line
        self._date = list()

    @property
    def data(self):
        if not self._date:
            workbook = open_workbook(self.excel)
            if type(self.sheet) not in (int, str):
                raise SheetTypeError('Please pass in <type int> or <type str>, not {0}'.format(type(self.sheet)))
            elif type(self.sheet) == int:
                s = workbook.sheet_by_index(self.sheet)
            else:
                s = workbook.sheet_by_name(self.sheet)

            if self.title_line:
                title = s.row_values(0)
                for col in range(1, s.nrows):
                    # 遍历其他行，与首行组成dict
                    self._date.append(dict(zip(title, s.row_values(col))))
            else:
                for col in range(0, s.nrows):
                    # 遍历全部行
                    self._date.append(s.row_values(col))
        return self._date


if __name__ == '__main__':
    e = 'D:/Python/TestFramework/data/data.xlsx'
    reader = ExcelReader(e, title_line=True)
    print(reader.data)