"""
@File: pandas_operate_excel.py
@CreateTime: 2019/12/13 下午5:23
@Desc: python操作excel文件
"""
import pandas as pd
from useful_func.settings import all_dict


class OperateCsv(object):

    def __init__(self):
        pass

    @staticmethod
    def read_csv(path: str):
        """
        header=none从第一行开始读取, utf-8-sig：解决出现乱码问题
        :param path: 文件路径
        :return:
        """
        df = pd.read_csv(path, encoding="utf-8-sig", engine="python", header=None)
        for num, data in enumerate(df.values, start=1):
            print(num, data)

    @staticmethod
    def save_csv(datalist: list):
        """
        每一行需要进行存储的数据列表,a为续写，header，index为首行，首列
        :param datalist:
        :return:
        """
        df = pd.DataFrame(data=[datalist])
        df.to_csv("/Users/ppwang/Desktop/1_update.csv", mode='a', encoding='utf-8-sig', header=False, index=False)


class OperateExcel(object):

    def __init__(self):
        pass

    @staticmethod
    def read_excel(path: str):
        """
        读取excel文件，如果不指定sheet_name默认为第一个,header=None读取第一条
        :return:
        """
        data = pd.read_excel(path, sheet_name="网站")
        # data.values获取所有的数据
        for num, cdata in enumerate(data.values, start=1):
            print(num, cdata)

    @staticmethod
    def save_one_sheet_excel():
        """
        存储为一个表格
        :return:
        """
        data_list = [["a", "b", "c"], ["a1", "b1", "c1"], ["a2", "b2", "c2"]]
        df = pd.DataFrame(data_list, columns=["第一列", "第二列", "第三列"])
        df.to_excel("output.xlsx", sheet_name="测试数据", index=False)

    def save_more_sheet_excel(self):
        """
        模拟在一个excel文件中存储多个sheet，将多个sheet表格存入到一个文件中
        参考链接:  https://blog.csdn.net/midion9/article/details/89000131
        :return:
        """
        writer = pd.ExcelWriter("output.xlsx")
        for key, value in all_dict.items():
            data_list = list()
            for data in value:
                data_list.append([key, data])
            df = pd.DataFrame(data_list)
            df.to_excel(writer, sheet_name=key, header=["名称", "链接"], index=False)
        writer.save()


if __name__ == '__main__':
    oc = OperateCsv()
    oe = OperateExcel()
    oe.save_more_sheet_excel()



