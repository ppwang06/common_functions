"""
@File: log_handler_employ.py
@CreateTime: 2019/12/23 下午2:04
@Desc: 日志的使用， 配合log_handler进行使用
"""
from sys_func.common_log_module import OutputToConsole, OutputToAll
from useful_func.custom_errors import TaskFull


def simple_log_employ():
    logger = OutputToConsole().logger
    logger.info("日志记录的使用，既可以输出到屏幕上，也可以保存到日志内")
    logger.info("该日志会在当前目录下创建一个log文件")


def complicated_log_employ():
    filename = "./test.log"
    logger = OutputToAll(filename=filename).logger
    logger.info("这是测试用例一，会保存至log日志文件内")
    logger.info("这是测试用例二，会保存至log日志文件内")


if __name__ == '__main__':
    complicated_log_employ()


