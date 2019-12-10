"""
@File: operate.py
@CreateTime: 2019/12/10 上午10:09
@Desc: 使用redis数据库
redis可以存  字符串string  列表list  散列hash  集合set  有序集合sorted set
redis链接：https://blog.csdn.net/lq18050010830/article/details/79715691
"""
import redis
from redis import ConnectionPool
from operate_database.settings import redis_settings


class OperateRedis(object):

    def __init__(self):
        self.conn = redis.Redis(**redis_settings)

    def add_operate(self, url):
        """
        对字符串的操作，用于去重
        :return:
        """
        if self.conn.get(url) is None:
            self.conn.set(url, 1)
            print("数据不存在，增加")
        else:
            print("数据已存在")


if __name__ == '__main__':
    ors = OperateRedis()
    ors.add_operate("https://www.infoq.cn/article/xDM8ITtjdqfvH8WRo8K4")
