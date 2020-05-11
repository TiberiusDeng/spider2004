import requests
from tools.proxypool_connect import get_ip
proxy = get_ip()
proxies = {
            'http': 'http://' + proxy,
            'https': 'https://' + proxy
        }
r = requests.get('https://weixin.sogou.com/', proxies = proxies)
print(r.text)