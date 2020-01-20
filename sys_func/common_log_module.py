"""
@File: common_log_module.py
@CreateTime: 2020/1/20 下午3:31
@Desc: 通用日志模块使用
"""
import logging


class BaseLogger(object):

    def __init__(self, level='info', fmt='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.level_relations = {
            'debug': logging.DEBUG,
            'info': logging.INFO,
            'warning': logging.WARNING,
            'error': logging.ERROR,
            'critical': logging.CRITICAL
        }
        self.logger = logging.getLogger('logger')
        self.format_str = logging.Formatter(fmt)      # 设置日志格式
        level = str.lower(level)
        self.logger.setLevel(self.level_relations.get(level))


class OutputToConsole(BaseLogger):

    def __init__(self):
        super().__init__()
        sh = logging.StreamHandler()        # 往屏幕上输出
        sh.setFormatter(self.format_str)    # 设置屏幕上的格式
        self.logger.addHandler(sh)          # 把对象添加到logger里

    def back_logger(self):
        return self.logger


class OutputToAll(BaseLogger):

    def __init__(self, filename):
        super().__init__()
        sh = logging.StreamHandler()                    # 往屏幕上输出
        sh.setFormatter(self.format_str)                # 设置屏幕上的格式
        self.logger.addHandler(sh)                      # 把对象添加到logger里
        fh = logging.FileHandler(filename=filename)     # 往文件里输出
        fh.setFormatter(self.format_str)                # 设置往文件里输出的格式
        self.logger.addHandler(fh)                      # 把对象添加到logger里










