import sys

sys.path.append('../')

from Public.Publicfunction import validUsefulProxy
from Manager.Proxymanger import Proxymanger

class ProxyValidSchedule(Proxymanger):
    """实时检查代理是否可用"""
    def __init__(self):
        super(ProxyValidSchedule,self).__init__()

    def __validproxy__(self):
        while 1:
            self.db.changeTable(self.useful_proxy_queue)
            for each_proxy in self.db.getAll():
                if validUsefulProxy(each_proxy):
                    print(each_proxy,"可用")
                else:
                    self.db.delete(each_proxy)

    def main(self):
        self.__validproxy__()

def run():
    p = ProxyValidSchedule()
    p.main()

if __name__ == '__main__':
    run()