import requests
from lxml import  etree
import traceback
import re
from header import wechat_header
import datetime
from url import generate_search_url_wechat
import pandas as pd
def get_html(url):
    try:
        header = wechat_header()
        html = requests.get(url,headers = header).text.replace('<!--red_beg-->','').replace('<!--red_end-->','').replace('<em>','').replace('</em>','')
        selector = etree.HTML(html)
        return selector
    except Exception as e:
        print('Error: ', e)
        traceback.print_exc()

def get_text(url):
    try:
        header = wechat_header()
        text = requests.get(url,headers = header).text
        return text
    except Exception as e:
        print('Error: ', e)



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

def get_post_view(author):
    perm_list = []
    url = generate_search_url_wechat(author, 1, 1)
    resp = get_text(url)
    post_view_perms = __get_post_view_perm(resp)
    if len(post_view_perms)==0:
        return [0,0]
    page = get_html(url)
    sin_info = page.xpath('//ul[@class="news-list2"]/li')[0]
    headimg = sin_info.xpath('div/div[1]/a/img/@src')
    open_id = headimg[0].split('/')[-1]
    post = post_view_perms.get(open_id).split(',')
    post_perm = post[0]
    view_perm = post[1]
    perm_list.append(post_perm)
    perm_list.append(view_perm)
    return perm_list

def time_trans(post_time):
    time = int(re.findall(r"\d+\.?\d*", post_time)[0])
    dateArray = datetime.datetime.fromtimestamp(time)
    otherStyleTime = dateArray.strftime("%Y--%m--%d %H:%M:%S")
    return otherStyleTime

def single_page_proc(url):
    html = get_html(url)
    if html == None:
        return [None, None]
    infolist = []
    data_set = pd.DataFrame(columns=['title','article_link','author','author_link','post','view','post_time'])
    i = 0
    titles = html.xpath('//*[@class = "news-list"]//div[@class = "txt-box"]/h3/a')
    article_links = html.xpath('//*[@class = "news-list"]//div[@class = "txt-box"]/h3/a/@href')
    authors = html.xpath('//*[@class = "news-list"]//div[@class = "txt-box"]/div/a')
    author_links = html.xpath('//*[@class = "news-list"]//div[@class = "txt-box"]/div/a/@href')
    post_view = []
    post_times = html.xpath('//*[@class = "news-list"]//div[@class = "txt-box"]/div/span/script')
    for title in titles:
        post_view = []
        title = titles[i].text
        article_link = 'http://weixin.sogou.com{}'.format(article_links[i])
        author = authors[i].text
        author_link = 'http://weixin.sogou.com{}'.format(author_links[i])
        post_view = get_post_view(author) #todo 处理为空
        post = post_view[0]
        view = post_view[1]
        post_time = time_trans(post_times[i].text)
        data_item = {
            'title' : title,
            'article_link' : article_link,
            'author' : author,
            'author_link' : author_link,
            'post' : post,
            'view' : view,
            'post_time' : post_time
        }
        data_set = data_set.append(data_item, ignore_index=True)
        i = i+1
