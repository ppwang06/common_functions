"""
@File: parse_xml_data.py
@CreateTime: 2020/1/20 下午8:04
@Desc: 解析xml的返回数据
"""
from xml.dom.minidom import parse
import xml.dom.minidom
import requests
import re


def get_xml_data():
    url = ""
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
    }
    res = requests.get(url=url, headers=headers, timeout=15)
    res.encoding = "utf-8"
    data = res.text
    return data


def parse_xml_data():
    result_string = get_xml_data()
    print("所有数据获取完毕，开始解析")
    DOMTree = xml.dom.minidom.parseString(result_string)
    collection = DOMTree.documentElement
    items = collection.getElementsByTagName('item')
    for item in items:
        title = item.getElementsByTagName('title')[0].childNodes[0].data
        link = item.getElementsByTagName('link')[0].childNodes[0].data
        category = item.getElementsByTagName('category')[0].childNodes[0].data
        source = item.getElementsByTagName('source')[0].childNodes[0].data
        pub_date = item.getElementsByTagName('pubDate')[0].childNodes[0].data
        description = item.getElementsByTagName('description')[0].childNodes[0].data
        content = re.compile('<.*?>').sub('', description)
        print('title:', title)
        print('link:', link)
        print('category', category)
        print('source', source)
        print('pub_date', pub_date)
        print('content', content)
        break


if __name__ == '__main__':
    parse_xml_data()























