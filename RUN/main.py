from API.ProxyApi import run as ApiRun
from Schedule.ProxyValidSchedule import run as VailidRun
from multiprocessing import Process

def run():
    p1 = Process(target=ApiRun)
    p1.start()
    p2 = Process(target=VailidRun)
    p2.start()


if __name__ == "__main__":
    run()