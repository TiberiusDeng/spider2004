import time
import datetime
import re
from wc_kernel import get_html
from wc_kernel import get_text
from url import  generate_search_url_wechat
import requests
from lxml import etree
url = generate_search_url_wechat('动物森友',1)
html = get_html(url)


def get_elem_text(elem):
    """抽取lxml.etree库中elem对象中文字

    Args:
        elem: lxml.etree库中elem对象

    Returns:
        elem中文字
    """
    if elem != '':
        return ''.join([node.strip() for node in elem.itertext()])
    else:
        return ''


get_post_view_perm = re.compile('<script>var account_anti_url = "(.*?)";</script>') #TODO 又来这里啦

def __get_post_view_perm(text):  # TODO 到这里啦
    result = get_post_view_perm.findall(text)
    if not result or len(result) < 1 or not result[0]:
        return None

    r = requests.get('http://weixin.sogou.com{}'.format(result[0]))  # TODO 将result[0]以前面那种格式格式化
    if not r.ok:
        return None

    if r.json().get('code') != 'success':
        return None

    return r.json().get('msg')  # TODO 取了msg的信息出来


article_link = html.xpath('//*[@class = "news-list"]//div[@class = "txt-box"]/h3/a/@href') #todo 补前缀
#sin_link = html.xpath('//*[@class = "news-list"]//div[@class = "txt-box"]/h3/a/@href')[2]
sin_link = 'http://weixin.sogou.com{}'.format(article_link[0])
print(sin_link)
titles = html.xpath('//*[@class = "news-list"]//div[@class = "txt-box"]/h3/a/text()')
sin_title = html.xpath('//*[@class = "news-list"]//div[@class = "txt-box"]/h3/a')[1].text
#title = get_elem_text(title).replace("red_beg", "").replace("red_end", "")
print(sin_title)

authors = html.xpath('//*[@class = "news-list"]//div[@class = "txt-box"]/div/a/text()')
print(authors)
author_links = html.xpath('//*[@class = "news-list"]//div[@class = "txt-box"]/div/a/@href')
sin_author_link = 'http://weixin.sogou.com{}'.format(author_links[0])
print(sin_author_link)




testlink = 'https://weixin.sogou.com/weixin?type=1&s_from=input&query=%E6%9C%BA%E5%99%A8%E4%B9%8B%E5%BF%83&ie=utf8&_sug_=y&_sug_type_=&w=01019900&sut=4841&sst0=1588597172085&lkt=0%2C0%2C0'
    # 'https://weixin.sogou.com/weixin?type=1&s_from=input&query=1626%E6%BD%AE%E6%B5%81%E7%B2%BE%E9%80%89&ie=utf8&_sug_=n&_sug_type_=&w=01019900&sut=15459&sst0=1588597122525&lkt=0%2C0%2C0'
testlink2 = 'https://weixin.sogou.com/weixin?type=1&s_from=input&query=%E8%99%8E%E5%97%85&ie=utf8&_sug_=y&_sug_type_=&w=01019900&sut=7506&sst0=1588596983876&lkt=0%2C0%2C0'
testlink3 = 'https://weixin.sogou.com/weixin?type=1&s_from=input&query=%E8%82%A5%E8%A5%BF%E8%82%A5%E8%A5%BF&ie=utf8&_sug_=n&_sug_type_=&w=01019900&sut=4960&sst0=1588597584707&lkt=0%2C0%2C0'
resp = get_text(testlink)
post_view_perms = __get_post_view_perm(resp)
#post = int(post_view_perms[0])

page = get_html(testlink)
sin_info = page.xpath('//ul[@class="news-list2"]/li')[0]
headimg = sin_info.xpath('div/div[1]/a/img/@src')
open_id = headimg[0].split('/')[-1]






#open_id = 'oIWsFt5kliJ_t2oh2ibk-D8xr_fk'
post = post_view_perms.get(open_id).split(',')
#post_view_perm = post_view_perms[0['open_id']].split(',')
post_perm = post[0]
view_perm = post[1]
print(post_view_perms)


times = html.xpath('//*[@class = "news-list"]//div[@class = "txt-box"]/div/span/script')
#times = re.findall(r"\d+\.?\d*",times)
time = times[1].text
time = int(re.findall(r"\d+\.?\d*",time)[0])
#print(time[0])
#time = 1557502800
# time_local = time.localtime(time)
# print(time_local)

dateArray = datetime.datetime.fromtimestamp(time)
otherStyleTime = dateArray.strftime("%Y--%m--%d %H:%M:%S")
print(otherStyleTime)






