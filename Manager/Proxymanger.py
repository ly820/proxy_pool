from Proxy_get.ProxyGetter import GetFreeProxy
from Public.GetConfig import GetConfig
from DB.DBClient import DBClient


class Proxymanger(object):
    def __init__(self):
        self.db = DBClient()
        self.config = GetConfig()
        self.raw_proxy_queue = 'raw_proxy_queue'
        self.useful_proxy_queue = 'useful_proxy_queue'

    def refresh(self):
        for proxyGetter in self.config.proxy_getter_functions():
            proxy_set = set()
            gg = GetFreeProxy()
            for proxy in getattr(GetFreeProxy, proxyGetter.strip())(gg):
                print(proxy)
                if proxy.strip():
                    proxy_set.add(proxy.strip())



            self.db.changeTable(self.raw_proxy_queue)
            for proxy in proxy_set:
                print(proxy)
                self.db.put(proxy)

    def get(self):
        self.db.changeTable(self.useful_proxy_queue)
        return self.db.get()

    def delete(self, proxy):
        self.db.changeTable(self.useful_proxy_queue)
        self.db.delete(proxy)

    def getAll(self):
        self.db.changeTable(self.useful_proxy_queue)
        return self.db.getAll()


if __name__ == '__main__':
    pp = Proxymanger()
    pp.get()
