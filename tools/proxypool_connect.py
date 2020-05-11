import requests

#todo 两种获取IP方法：实时抓，需同时跑proxypool程序/redis取（未实现）
proxypool_url = 'http://127.0.0.1:5555/random'
target_url = 'http://httpbin.org/get'
target_urls = 'https://weixin.sogou.com/'#直接用目标网站测试


def get_random_proxy():
    """
    get random proxy from proxypool
    :return: proxy
    """
    return requests.get(proxypool_url).text.strip()

def get_ip():
    ip = 0
    for i in range(1000):
        try:
            proxy = get_random_proxy()
            print('get random proxy', proxy)
            proxies = {'https': 'https://' + proxy}
            r = requests.get(target_urls, proxies=proxies,timeout=3)
            print(r.status_code)
            r.raise_for_status()
            ip = proxy
            break
        except Exception as e:
            print('Error: ', e)
            continue
    print('ip:',ip)
    return ip

