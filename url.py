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

def generate_search_url_wechat(keyword,page = 1,type = 2):
    assert isinstance(page,int) and page>0
    url_sufix = OrderedDict()
    url_sufix['type'] = type # 2为搜索文章 1为搜索公众号
    url_sufix['page'] = page
    url_sufix['ie'] = 'utf8'
    url_sufix['query'] = keyword
    return 'http://weixin.sogou.com/weixin?{}'.format(urllib.parse.urlencode(url_sufix))

#a = generate_search_url_weibo('动森', 1, '2020-04-01-0', '2020-04-02-0')
#print(a)