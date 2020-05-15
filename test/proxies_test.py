import requests
import redis
from tools.proxypool_connect import get_ip
#pool = redis.ConnectionPool(host='127.0.0.1',port=6379,max_connections=10)
#db = redis.StrictRedis(host='127.0.0.1',port=6379, decode_responses=True)
proxy = get_ip()
proxies = {
            'http': 'http://' + proxy,
            'https': 'https://' + proxy
        }
r = requests.get('https://weixin.sogou.com/', proxies = proxies)
print(r.text)