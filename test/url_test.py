import sys
sys.path.append('../')
from url import generate_search_url_weibo

a = generate_search_url_weibo('动森', 1, '2020-04-01-0', '2020-04-02-0')
print(a)