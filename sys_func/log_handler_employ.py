"""
@File: log_handler_employ.py
@CreateTime: 2019/12/23 下午2:04
@Desc: 日志的使用， 配合log_handler进行使用
"""
from sys_func.log_handler import Loggers


log = Loggers()


def simple_log_employ():
    log.logger.info("日志记录的使用，既可以输出到屏幕上，也可以保存到日志内")
    log.logger.info("该日志会在当前目录下创建一个log文件")


if __name__ == '__main__':
    simple_log_employ()


