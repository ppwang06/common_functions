"""
@File: time_change.py
@CreateTime: 2019/12/13 下午2:16
@Desc: 时间戳，时间格式，字符串的转换
"""
import time
import datetime


def string_datetime_change():
    """
    datetime数据类型与字符串str的转换
    :return:
    """
    # datetime转str
    now_time = datetime.datetime.now()
    now_str = now_time.strftime("%Y-%m-%d %H:%M:%S")
    print(now_time, now_str)
    # str 转 datetime
    later_str = "2019-12-11 14:29:01"
    later_time = datetime.datetime.strptime(later_str, "%Y-%m-%d %H:%M:%S")
    print(later_time, later_str)


def timestamp_datetime_change():
    """
    timestamp与datetime相互转换
    :return:
    """
    # 获取10位的时间戳， 获取13位的时间戳*1000即可
    now_timestamp = time.time()
    now_timestamp = int(now_timestamp)
    print(type(now_timestamp), now_timestamp)
    # 时间戳timestamp转datetime
    data_time = datetime.datetime.fromtimestamp(now_timestamp)
    print(data_time)
    # datetime数据类型转时间戳
    now_time = datetime.datetime.now()
    data_timestamp = time.mktime(time.strptime(now_time.strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S"))
    print(data_timestamp)


def timestamp_string_change():
    """
    timestamp与string相互转换
    :return:
    """
    # 字符串转为时间戳
    time_str = "2019-11-05 23:25:56"
    time_array = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    time_timestamp = int(time.mktime(time_array))
    print(time_timestamp)
    # 时间戳转字符串
    data_time = datetime.datetime.fromtimestamp(time_timestamp)
    now_time_str = data_time.strftime("%Y-%m-%d %H:%M:%S")
    print(now_time_str)


if __name__ == '__main__':
    timestamp_string_change()


