from collections import OrderedDict

import urllib.parse

def generate_search_url_weibo(keyword, page=1,
                              st=None, et=None):
    assert isinstance(page, int) and page > 0

    url_sufix = OrderedDict()
    url_sufix['q'] = keyword
    url_sufix['page'] = page
    url_sufix['suball'] = 1  # 代表是全部类型，有的是含图片什么的
    url_sufix['Refer'] = 'g'  # 或weibo_weibo代表搜索的是综合
    if st or et:
        url_sufix['timescope'] = 'custom:{}:{}'.format(st, et)
    return 'https://s.weibo.com/weibo?{}'.format(urllib.parse.urlencode(url_sufix)) #urllib.parse.quot就是urlencode

a = generate_search_url_weibo('动森', 1, '2020-04-01-0', '2020-04-02-0')
print(a)