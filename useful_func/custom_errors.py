"""
@File: custom_errors.py
@CreateTime: 2020/1/20 下午5:00
@Desc: 抛出错误
"""


class HttpConnectionError(ConnectionError):

    def __init__(self, url):
        self.message = f"{self.__class__.__name__}: {url}"


class HttpCodeError(Exception):

    def __init__(self, url, code):
        self.message = f"{self.__class__.__name__} {code}: {url}"


class DownloadError(Exception):

    def __init__(self, _id):
        self.message = f"{_id}下载失败"


class TaskFull(Exception):

    def __init__(self, size):
        self.message = "待处理任务数：{} 暂无新任务 Sleeping...".format(size)


class TaskEmpty(Exception):

    def __init__(self, size):
        self.message = "待处理任务数：{} 暂无新任务 Sleeping...".format(size)




