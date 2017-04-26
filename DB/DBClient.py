from Public.GetConfig import GetConfig
import os
import sys
"""
该模块定义了一个DbClient的类,它能按配置文件初始化数据库并操作数据库
"""

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

class DBClient(object):

    def __init__(self):
        # 初始化对象
        self.config = GetConfig()  # 获得配置文件
        self.__initDBClient()  # 初始化数据库

    def __initDBClient(self):

        # 初始化数据库
        __type = None

        # 如果数据库的类型是'MONGODB'
        if 'MONGODB' == self.config.db_type():
            __type = 'MongoDBClient'
        else:
            pass

        # 导入  __type模块,并获得的该模块的__type所对的MongoDBClient类，创建它的实例self.client并根据配置文件初始化

        name = self.config.db_name()
        host = self.config.db_host()
        port = int(self.config.db_port())

        self.client = getattr(__import__('MongoDBClient'),__type)(name,host,port)

    def get(self, **kwargs):
        return self.client.get(**kwargs)

    def put(self, value, **kwargs):
        return self.client.put(value, **kwargs)

    def pop(self, **kwargs):
        return self.client.pop(**kwargs)

    def delete(self, value, **kwargs):
        return self.client.delete(value, **kwargs)

    def getAll(self):
        return self.client.getAll()

    def changeTable(self, name):
        self.client.changetable(name)


if __name__ == '__main__':
    db = DBClient()
    print(db.get())

