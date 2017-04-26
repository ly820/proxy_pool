import pymongo
import random

"""
该模块定义了MongoDBClient的类,该类有get/put/delete/pop/getAll/clean/delete_all/changetable等方法来操作数据库
"""


class MongoDBClient(object):
    def __init__(self, name, host, port):
        """
        :param name: Mongodb 中表的名子
        :param host: 连接数据库的地址
        :param port: 连接数据库的端口
        """

        self.client = pymongo.MongoClient(host, port)  # 连接数据库
        self.db = self.client.PROXY  # 使用PROXY数据库
        self.name = name  # PROXY数据库中的表的名字（kuaidaili,youdiali,66daili,xici）

    def changetable(self, name):
        """
        切换数据表
        :param name: 数据表的表名
        :return: None
        """
        self.name = name

    def get(self):
        """随机取出一个代理"""
        proxies = self.getAll()
        return random.choice(proxies) if proxies else None

    def put(self, value):
        # 向数据库中添加代理
        if self.db[self.name].find_one({'proxy': value}):
            return None
        else:
            self.db[self.name].insert_one({'proxy': value})

    def pop(self):
        # 随机从数据库中弹出一个代理，并返回
        value = self.get()
        if value:
            self.delete(value)
        return value

    def delete(self, value):
        # 删除value对应的代理
        self.db[self.name].remove({'proxy': value})

    def getAll(self):
        # 获得数据表中所有的代理
        return [item['proxy'] for item in self.db[self.name].find()]

    def clean(self):
        # 删除数据库PROXY
        self.client.drop_database('PROXY')

    def delete_all(self):
        # 删除数据表中所有代理
        self.db[self.name].remove()


if __name__ == '__main__':
    db = MongoDBClient('xici', 'localhost', 27017)
    db.put('127.0.0.1:1')
    db2 = MongoDBClient('youdaili', 'localhost', 27017)
    db2.put('127.0.0.1:1')
