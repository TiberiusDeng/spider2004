import sys
sys.path.append('../')
from url import generate_search_url_weibo
from url import generate_search_url_wechat
a = generate_search_url_weibo('动森', 1, '2020-04-01-0', '2020-04-02-0')
print(a)

b = generate_search_url_wechat('动物森友',1)
print(b)