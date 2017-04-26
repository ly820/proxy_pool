
from bs4 import BeautifulSoup
import re
from Public.Publicfunction import get_web_page

"""
该模块定义了一个GetFreeProxy的类，类里有四种方法:
    get_proxy_from_kuaidaili
    get_proxy_from_66daili
    get_proxy_from_youdaili
    get_proxy_from_xicidaili
分别从不同的网站获取代理

"""


class GetFreeProxy(object):

    def __init__(self):
        pass



    def get_proxy_from_kuaidaili(self,page = 10):
        """
        爬取快代理网：http://www.kuaidaili.com/proxylist/
        :param page: 快代理的页数
        :return: 一个代理的生成器
        """

        urls = ["http://www.kuaidaili.com/proxylist/" + str(i) for i in range(1, page+1)]
        for url in urls:
            headers = None
            html = get_web_page(url,headers)
            if html:
                soup = BeautifulSoup(html,"lxml")
                ips = soup.find_all("td",{"data-title":"IP"})
                ports = soup.find_all("td",{"data-title":"PORT"})
                proxies = (ip.get_text() + ':' +port.get_text() for ip,port in zip(ips,ports))
                for proxy in proxies:
                    yield proxy

    def get_proxy_from_66daili(self,page=100):
        """
        爬取66代理网：http://www.66ip.cn/
        :param page: 66代理的页数
        :return: 一个代理生成器
        """
        headers = None
        urls = ["http://www.66ip.cn/{0}.html".format(i) for i in range(2,page+1)]
        for url in urls:

            html = get_web_page(url,headers)
            if html:
                pattern = re.compile(r'<tr><td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td><td>(\d{1,5})</td>')
                results = re.findall(pattern,html)
                if results:
                    proxies = (item[0]+':'+item[1] for item in results)
                    for proxy in proxies:
                        yield proxy


    def get_proxy_from_youdaili(self,days=1):
        """
        爬取有代理网：http://www.youdaili.net/Daili/http
        :param days: 天数,爬取哪几天的代理
        :return: 代理生成器
        """
        headers = None
        base_url = "http://www.youdaili.net/Daili/http/"
        base_html = get_web_page(base_url,headers)
        if base_html:
            base_soup = BeautifulSoup(base_html,"lxml")
            items = base_soup.select('.chunlist ul li  a')
            if items:
                for item in items[0:days]:
                    url = item.get("href")
                    html = get_web_page(url,headers)
                    if html:
                        pattern = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}')
                        proxies = re.findall(pattern,html)
                        for proxy in proxies:
                            yield proxy

    def get_proxy_from_xicidaili(self,page=50):
        headers = {
            'Host': 'www.xicidaili.com',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36'
        }
        url_list = ['http://www.xicidaili.com/nn/', # 高匿
                    'http://www.xicidaili.com/nt/'  # 透明
                    ]
        for url in url_list:
            urls = [url + str(i) for i in range(1,page+1)]
            for url in urls:
                html = get_web_page(url,headers)
                if html:
                    pattern = re.compile(r'<tr.*?"odd">.*?<td.*?country"><img.*?<td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td>.*?<td>(\d{1,5})</td>',re.S)
                    results = re.findall(pattern,html)
                    if results:
                        proxies = (item[0] + ':' + item[1] for item in results)
                        for proxy in proxies:
                            yield proxy

    def get_proxy_from_yun_daili(self,page=10):
        headers = None
        url_list = ['http://www.yun-daili.com/?stype=3&page={0}'.format(i) for i in range(1,page+1)]
        for url in url_list:
            html = get_web_page(url,headers)
            if html:
                soup = BeautifulSoup(html,"lxml")
                ips = soup.select('td.style1')
                ports = soup.select('td.style2')
                if ips:
                    for ip,port in zip(ips,ports):
                        proxy = ip.get_text() + ':' + port.get_text()
                        yield proxy

    def get_proxy_from_ip181(self):
        header = None
        url = 'http://www.ip181.com/'
        html = get_web_page(url, header)
        pattern = re.compile(r'<td>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}<td>(\d{1,5})</td>', re.S)
        if html:
            soup = BeautifulSoup(html, 'lxml')
            results = soup.find_all('tr')[1:]
            for result in results:
                item = list(result.strings)
                proxy = item[1] + ':' + item[3]
                yield proxy


if __name__ == '__main__':
    gg = GetFreeProxy()
    for proxy in gg.get_proxy_from_kuaidaili():
        print(proxy)
    for i in gg.get_proxy_from_66daili():
        print(i)
    for j in gg.get_proxy_from_youdaili():
        print(j)
    for y in gg.get_proxy_from_xicidaili():
        print(y)