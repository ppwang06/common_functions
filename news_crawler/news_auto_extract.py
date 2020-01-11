"""
@File: news_auto_extract.py
@CreateTime: 2020/1/10 上午9:46
@Desc: 文章内容的提取 gne模块的使用
"""
import requests
from gne import GeneralNewsExtractor


class GetPageContent(object):

    def __init__(self):
        self.headers = {}
        self.extractor = GeneralNewsExtractor()

    def static_page_dict(self, url: str) -> str:
        res = requests.get(url=url, headers=self.headers, timeout=15)
        detail_html = res.text
        return detail_html

    def extractor_html(self, detail_html):
        result = self.extractor.extract(detail_html)
        return result

    def extractor_html_code(self, detail_html):
        result = self.extractor.extract(detail_html, with_body_html=True)
        return result

    def extractor_html_abstract_path(self, detail_html, host=""):
        result = self.extractor.extract(detail_html, host=host)
        return result

    def extractor_html_noise_code(self, detail_html, title_xpath="", noise_node_list=""):
        result = self.extractor.extract(detail_html, title_xpath=title_xpath, noise_node_list=noise_node_list)
        return result


if __name__ == '__main__':
    url = "https://www.infoq.cn/article/kXBaKpzLfrdxVcYh8hUV"
    gpc = GetPageContent()
    html = gpc.static_page_dict(url=url)
    result = gpc.extractor_html(html)
    print(result)



