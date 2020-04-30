import time
import datetime
import re
from wc_kernel import get_html
from url import  generate_search_url_wechat
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


article_link = html.xpath('//*[@class = "news-list"]//div[@class = "txt-box"]/h3/a/@href') #todo 补前缀
sin_link = html.xpath('//*[@class = "news-list"]//div[@class = "txt-box"]/h3/a/@href')[2]
print(sin_link)
titles = html.xpath('//*[@class = "news-list"]//div[@class = "txt-box"]/h3/a/text()')
sin_title = html.xpath('//*[@class = "news-list"]//div[@class = "txt-box"]/h3/a')[1].text
#title = get_elem_text(title).replace("red_beg", "").replace("red_end", "")
print(sin_title)
author = html.xpath('//*[@class = "news-list"]//div[@class = "txt-box"]/div/a/text()')
print(author)

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


