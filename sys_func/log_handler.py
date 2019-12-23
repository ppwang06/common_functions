"""
@File: log_handler.py
@CreateTime: 2019/12/19 下午5:22
@Desc: Python日志模块的使用  使用方法如log_handler_employ
"""
import os
import logging
import datetime
from logging import Handler, FileHandler, StreamHandler


class PathFileHandle(FileHandler):

    def __init__(self, path, filename, mode='a', encoding=None, delay=False):
        filename = os.fspath(filename)
        if not os.path.exists(path):
            os.mkdir(path)
        self.baseFilename = os.path.join(path, filename)
        self.mode = mode
        self.encoding = encoding
        self.delay = delay
        if delay:
            Handler.__init__(self)
            self.stream = None
        else:
            StreamHandler.__init__(self, self._open())


class Loggers(object):

    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }
    now_time = datetime.datetime.now()
    file_name = now_time.strftime("%Y-%m-%d")

    def __init__(self, filename='{filename}.log'.format(filename=file_name), level='info', log_dir='log',
                 fmt='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                 ):
        self.logger = logging.getLogger(filename)
        abspath = os.path.dirname(os.path.abspath(__file__))
        self.directory = os.path.join(abspath, log_dir)
        format_str = logging.Formatter(fmt)  # 设置日志格式
        self.logger.setLevel(self.level_relations.get(level))  # 设置日志级别
        stream_handler = logging.StreamHandler()  # 往屏幕上输出
        stream_handler.setFormatter(format_str)
        file_handle = PathFileHandle(path=self.directory, filename=filename, mode='a')
        file_handle.setFormatter(format_str)
        self.logger.addHandler(stream_handler)
        self.logger.addHandler(file_handle)



