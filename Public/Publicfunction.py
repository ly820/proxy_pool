import requests
from requests.exceptions import ConnectionError

def verifyProxy(proxy):
    """
    检验代理的格式
    :param proxy: 代理
    :return: bool值
    """
    import re
    verify_regex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}'
    return True if re.findall(verify_regex,proxy) else False

def validUsefulProxy(proxy):
    """
    用代理去请求百度,判断代理是否可用
    :param proxy: 代理
    :return: bool值
    """
    proxies = {
        "http":"http://{proxy}".format(proxy=proxy),
        "https": "http://{proxy}".format(proxy=proxy)
    }

    try:
        html = requests.get("http://www.baidu.com",proxies=proxies,timeout=30)
        if html.status_code == 200:
            return True
    except:
        return False

def get_web_page(url,headers):
    try:
        html = requests.get(url, headers=headers)
        if html.status_code == 200:
            return html.text
        else:
            return None
    except ConnectionError:
        print("链接失败")