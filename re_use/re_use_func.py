"""
@File: re_use_func.py
@CreateTime: 2020/2/27 上午10:29
@Desc: python中正则表达式的使用 脚本文件,修改链接为接口数据,
"""
import re
import requests
from setting import HEADERS


class ChangeUrlToApi(object):

    def __init__(self):
        self.url = "https://author.baidu.com/home/1611994554344933"
        self.cookies = {
            'BAIDUID': '497B32CD69E2C1A2B1B8F866A725ADBF:FG=1',
        }

    def handler_url(self):
        res = requests.get(url=self.url, headers=HEADERS)
        result = re.search(r'"uk":"(.*?)"', res.text)
        hash_id = result.group(1)
        api_url = f"https://mbd.baidu.com/webpage?tab=article&num=6&uk={hash_id}&type=newhome&format=json"
        print(api_url)
        response = requests.get(url=api_url, headers=HEADERS, cookies=self.cookies)
        all_list = response.json().get("data").get("dynamic").get("list")
        for num, data in enumerate(all_list):
            need_data = data.get("itemData")
            title = need_data.get("title")
            print(title)

    def run(self):
        self.handler_url()


if __name__ == '__main__':
    cut = ChangeUrlToApi()
    cut.run()


