"""
@File: re_use_all.py
@CreateTime: 2020/2/27 上午11:52
@Desc: 正则的使用,match findall search
http://www.codeceo.com/article/20-regular-expressions.html   常用的正则表达式
"""
import re
import requests
from setting import HEADERS


class ReAllUse(object):

    def __init__(self):
        self.url_str = "https://author.baidu.com/home/1611994554344933"
        self.check_str = ''

    def save_str(self):
        res = requests.get(url=self.url_str, headers=HEADERS)
        self.check_str = res.text

    @staticmethod
    def search_re():

        # \b 匹配单词的开始或结束  \w匹配字母或数字或下划线  r表示原生字符串
        regex = re.compile(r'\b\w{6}\b')
        text = regex.search("My phone number is 421-2343-121")
        print(text.group())

        # 分支条件的使用，分支条件相当于可以添加多个规则进行数据匹配
        regex = re.compile(r'0\d{2}-\d{8}|0\d{3}-\d{7}')
        text_one = regex.search("My phone number is 021-76483929")
        text_two = regex.search("My phone number is 0132-2384753")
        print(text_one.group(), text_two.group())

        # 括号分组的使用,分组可以取得自己想要的一部分数据
        regex = re.compile(r'(0\d{2})-(\d{8})')
        text = regex.search("My phone number is 032-23847533")
        print(text.group(0), text.group(1), text.group(2))

        # ?之前的分组表示可选的分组，如果需要匹配真正的?, 就使用转义字符\?
        regex = re.compile(r'(0\d{2}-)?(\d{8})')
        text_one = regex.search("My phone number is 032-23847533")
        print(text_one.group())
        text_two = regex.search("My phone number is 23847533")
        print(text_two.group())

        # python默认是贪心 尽可能匹配最长的字符串
        regex = re.compile(r'(Py){3,5}')
        text = regex.search('PyPyPyPyPy')
        print(text.group())

        # ?声明非贪心， 尽可能匹配最短的字符串
        regex = re.compile(r'(Py){3,5}?')
        text = regex.search("PyPyPyPyPy")
        print(text.group())

    @staticmethod
    def findall_re():
        regex = re.compile(r'0\d{2}-\d{8}|0\d{3}-\d{7}')
        return_list = regex.findall("Cell: 021-38294729, Work: 0413-3243243")
        print(return_list)

    def match_re(self):
        pass

    def run(self):
        self.search_re()
        self.findall_re()


if __name__ == '__main__':
    rau = ReAllUse()
    rau.run()








