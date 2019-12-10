"""
@File: settings.py
@CreateTime: 2019/12/9 下午8:45
@Desc: 数据库的配置信息
"""

# mysql
CONFIG = {
    'default': 'mysql',
    'mysql': {
        "driver": "mysql",
        "host": "127.0.0.1",
        "database": "test_one",
        "user": "root",
        "password": "123456",
        "prefix": "",
        "port": 3306
    }
}


# redis

redis_settings = {
    "host": "127.0.0.1",
    "port": 6379,
    "password": "",
    "db": 0
}

# MongoDB

URI = "mongodb://127.0.0.1:27017/"
DB_NAME = "test-data"
DOC_NAME = "record"
USERNAMR = "libai"
PASSWORD = "123456"