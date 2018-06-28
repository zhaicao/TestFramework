
__author__ = 'zhaicao'

import os
import logging
from logging.handlers import TimedRotatingFileHandler
from utils.config import LOG_PATH
from utils.config import Config

class Logger(object):
    def __init__(self, logger_name = 'framework'):
        self.logger =  logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)
        conf = Config().get('log')
        self.log_file_name = conf.get('file_name') if conf and conf.get('file_name') else 'test.log'
        self.backup_count = conf.get('backup') if conf and conf.get('backup') else 5
        # 日志输出级别
        self.console_output_level = conf.get('console_level') if conf and conf.get('console_level') else 'WARNING'
        self.file_output_level = conf.get('file_level') if conf and conf.get('file_level') else 'DEBUG'
        # 日志输出格式
        pattern = conf.get('pattern') if conf and conf.get('pattern') else '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        self.formatter = logging.Formatter(pattern)

    def get_logger(self):
        """在logger中添加日志句柄并返回，如果logger已有句柄，则直接返回"""
        # 避免重复日志
        if not self.logger.handlers:
            # 控制台打印Log
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            # 最低级别
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)

            # 每天重新创建一个日志文件，最多保留backup_count份
            file_handler = TimedRotatingFileHandler(filename=os.path.join(LOG_PATH, self.log_file_name),
                                                    when='D',
                                                    interval=1,
                                                    backupCount=self.backup_count,
                                                    delay=True,
                                                    encoding='UTF-8'
                                                    )
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)

        return self.logger

logger = Logger().get_logger()


