"""
@File: test_common_log.py
@CreateTime: 2020/1/20 下午4:06
@Desc: 测试自定义log模块
"""
import unittest
import os


class TestStringMethods(object):

    def __init__(self):
        pass

    def test_makedir(self):
        """
        makedir只会创建对应的目录，并不会创建对应的文件
        :return:
        """
        filename = "./num_test/bc.log"
        os.makedirs(filename, exist_ok=True)


if __name__ == '__main__':
    ts = TestStringMethods()
    ts.test_makedir()

















