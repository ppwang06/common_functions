"""
@File: operate.py
@CreateTime: 2019/12/10 上午10:09
@Desc: 使用redis数据库
"""
import redis
from operate_database.settings import redis_settings


class OperateRedis:

    def __init__(self):
        self.conn = redis.Redis(**redis_settings)

    def add_operate(self):
        pass