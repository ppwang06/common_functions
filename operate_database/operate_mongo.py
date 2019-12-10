"""
@File: operate_mongo.py
@CreateTime: 2019/12/10 上午10:09
@Desc: 使用MongoDB数据库
使用链接  https://www.cnblogs.com/aademeng/articles/9779271.html
"""
import pymongo
from bson.objectid import ObjectId
from operate_database.settings import URI, DB_NAME, DOC_NAME, USERNAMR, PASSWORD


class MongoAction(object):
    """
    mongo api
    uri mongodb地址  db_name 数据库  doc_name 指定集合
    """

    def __init__(self):
        self.client = pymongo.MongoClient(URI)
        self.db = self.client[DB_NAME]
        self.db.authenticate(USERNAMR, PASSWORD)
        self.table = self.db[DOC_NAME]

    def insert_one_data(self):
        student = {
            "id": "20170101",
            "name": "jordan",
            "age": 40,
            "gender": "male"
        }
        result = self.table.insert_one(student)
        print(result)
        print(result.inserted_id)

    def insert_many_data(self):
        student_one = {
            "id": "20171124",
            "name": "john",
            "age": 20,
            "gender": "male"
        }
        student_two = {
            "id": "20191121",
            "name": "tom",
            "age": 36,
            "gender": "woman"
        }
        result = self.table.insert_many([student_one, student_two])
        print(result)
        print(result.inserted_ids)

    def search_from_data(self):
        result = self.table.find_one({"name": "john"})
        print(result)
        # 根据objectId进行查询
        result = self.table.find_one({'_id': ObjectId('593278c115c2602667ec6bae')})
        print(result)
        results = self.table.find({"age": 50})
        for result in results:
            print(result)

        # 根据范围内进行查询  年龄大于20，也可以使用正则查询
        results = self.table.find({'age': {'$gt': 20}})
        # 查询以M开头的
        results = self.table.find({'name': {'$regex': '^M.*'}})

    def update_data(self):
        """
        update_one和update_many
        :return:
        """
        # 更新一条
        condition = {"name": "john"}
        student = self.table.find_one(condition)
        student['age'] = 26
        result = self.table.update_one(condition, {'$set': student})
        # 匹配的数据条数 和 影响的数据条数
        print(result.matched_count, result.modified_count)

        # 更新多条数据 年龄大于15的,更新条件为年龄加1
        condition = {"age": {"$gt": 15}}
        result = self.table.update_many(condition, {'$inc': {'age': 1}})
        print(result.matched_count, result.modified_count)

    def delete_data(self):
        result = self.table.delete_one({"name": "john"})
        print(result.deleted_count)
        result = self.table.delete_many({"age": {"$lt": 25}})
        print(result.deleted_count)


if __name__ == '__main__':
    ma = MongoAction()
    ma.update_data()

