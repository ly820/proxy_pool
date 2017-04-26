from Public.Publicfunction import validUsefulProxy
from Manager.Proxymanger import Proxymanger
from multiprocessing import Process
from apscheduler.schedulers.blocking import BlockingScheduler
import sys

sys.path.append('../')

class ProxyRefreshSchedule(Proxymanger):
    def __init__(self):
        # 初始化父类
        super(ProxyRefreshSchedule,self).__init__()

    # 选出有效的代理添加到useful_proxy_queue中
    def valid_proxy(self):
        self.db.changeTable(self.raw_proxy_queue)  # 切换到最初的代理数据队列（一张数据表）
        raw_proxy = self.db.pop()  # 随机弹出一个代理
        while raw_proxy:
            # 如果该代理有效，存储到useful_proxy_queue中
            if validUsefulProxy(raw_proxy):
                print('有效代理：',raw_proxy)
                # 切换到useful_proxy_queue
                self.db.changeTable(self.useful_proxy_queue)
                # 添加代理
                self.db.put(raw_proxy)
            else:
                print('无效的代理：',raw_proxy)
            # 切换回raw_proxy_queue
            self.db.changeTable(self.raw_proxy_queue)
            # 再随机弹出一个
            raw_proxy = self.db.pop()

def refresh_pool():
    """刷新代理"""
    p = ProxyRefreshSchedule()
    p.valid_proxy()

def main(process_num=10):
    pool = ProxyRefreshSchedule()
    # 获取新代理
    pool.refresh()
    # 检验新代理
    pl = []
    for num in range(process_num):
        proc = Process(target=refresh_pool,args=())
        pl.append(proc)

    for num in range(process_num):
        pl[num].start()

    for num in range(process_num):
        pl[num].join()


if __name__ == '__main__':
    sched = BlockingScheduler()
    sched.add_job(main,'interval',minutes=10)
    sched.start()
    # main()
