"""
@File: operate_mysql.py
@CreateTime: 2019/12/9 下午8:35
@Desc: python操作mysql数据库,用法文档 https://orator-orm.com/docs/0.9/orm.html
"""
import logging
from orator import DatabaseManager
from operate_database.settings import CONFIG


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(filename)s %(process)d %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


class MainOperate:

    def __init__(self):
        self.db = DatabaseManager(config=CONFIG).connection()

    def one_mysql_link(self):
        """
        根据offset limit 查询数据
        :return:
        """
        result = self.db.table("corpus").offset(2).limit(5).get()
        for num, data in enumerate(result):
            #  根据字段名获取每一条信息
            logging.info(data.get("url"))
        return result

    def two_add_column(self):
        """
        给已存在的数据表增加一列数据
        :return:
        """
        new_data = {
            "title": "测试标题",
            "url": "https://www.baidu.com",
            "content": "测试正文",
            "published": "2019-11-02 12:16:01",
        }
        result = self.db.table("corpus").insert(new_data)
        logging.info(result)

    def three_update_data(self):
        """
        更新数据库操作
        :return:
        """
        corpus = self.db.table("corpus").where('id', '1').update({'published': '2019-12-03 09:25:01'})
        logging.info(corpus)

    def four_delete_data(self):
        """
        根据id来删除一行数据
        :return:
        """
        delete_data = self.db.table("corpus").delete('1899')
        logging.info(delete_data)


if __name__ == '__main__':
    mo = MainOperate()
    mo.four_delete_data()



