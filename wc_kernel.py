import requests
from lxml import  etree
import traceback
import re
from header import wechat_header
import datetime
from url import generate_search_url_wechat
from tools.proxypool_connect import get_ip
import pandas as pd
def get_html(url):
    try:
        header = wechat_header()
        # proxy = get_ip()
        # proxies = {
        #     'http': 'http://' + proxy,
        #     'https': 'https://' + proxy
        # }

        # r = requests.get(url,headers = header)
        # a = r.raise_for_status()
        # print(a)
        html = requests.get(url,headers = header).text.replace('<!--red_beg-->','').replace('<!--red_end-->','').replace('<em>','').replace('</em>','')
        selector = etree.HTML(html)
        antisp = selector.xpath('/html/body/div[2]/p[2]')
        if antisp:
            header = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36',
                'Cookie': 'SUV=004EC7C5B68B2D9E5C9C863F54DD0309; ssuid=2186822895; SUID=2DABCE654F18910A000000005C9E628E; CXID=C97698A2DC90848074428F38DC885A57; IPLOC=CN1100; ad=UkpJvZllll2Wz6XGlllllVfW0cGlllllWTYvcyllllylllllVylll5@@@@@@@@@@; sw_uuid=7366557983; SNUID=BFEEC46D0206A79AF0F575A803944467; sct=9; ppinf=5|1588262130|1589471730|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToxODolRTklQkIlODMlRTUlODYlQUN8Y3J0OjEwOjE1ODgyNjIxMzB8cmVmbmljazoxODolRTklQkIlODMlRTUlODYlQUN8dXNlcmlkOjQ0Om85dDJsdUVkZUlVTHVnbU5Gb0xCZE55WTdwRFVAd2VpeGluLnNvaHUuY29tfA; pprdig=qgmiCbTf7bMbeExfyLUeyP1pJJtlWbnnkDtgg60NDvb0KNDtCIZV6nAAXuCFNpGzXgvgj9JI4knIlpHMBgqxgKVo2Ke-YqQq6CLvkBS8YFs_x8YlNT1I214Jfo4LWnZDWvoGW_5E4Yz_cDFkNZzcXiQEKmNFaiIU5yB7oAUkdrI; sgid=16-47716061-AV6q9PLkn1PPRsZplD8M1kY'}
            html2 = requests.get(url, headers=header).text.replace('<!--red_beg-->', '').replace('<!--red_end-->','').replace('<em>','').replace('</em>', '')
            selector2 = etree.HTML(html2)
            return selector2
        noresult = selector.xpath('//*[@id="noresult_part1_container"]')
        if noresult:
            return None
        else:
            return selector #todo 查找迭代器内是否有元素
    except Exception as e:
        print('Error: ', e)
        traceback.print_exc()
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36',
            'Cookie': 'SUV=004EC7C5B68B2D9E5C9C863F54DD0309; ssuid=2186822895; SUID=2DABCE654F18910A000000005C9E628E; CXID=C97698A2DC90848074428F38DC885A57; IPLOC=CN1100; ad=UkpJvZllll2Wz6XGlllllVfW0cGlllllWTYvcyllllylllllVylll5@@@@@@@@@@; sw_uuid=7366557983; SNUID=BFEEC46D0206A79AF0F575A803944467; sct=9; ppinf=5|1588262130|1589471730|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToxODolRTklQkIlODMlRTUlODYlQUN8Y3J0OjEwOjE1ODgyNjIxMzB8cmVmbmljazoxODolRTklQkIlODMlRTUlODYlQUN8dXNlcmlkOjQ0Om85dDJsdUVkZUlVTHVnbU5Gb0xCZE55WTdwRFVAd2VpeGluLnNvaHUuY29tfA; pprdig=qgmiCbTf7bMbeExfyLUeyP1pJJtlWbnnkDtgg60NDvb0KNDtCIZV6nAAXuCFNpGzXgvgj9JI4knIlpHMBgqxgKVo2Ke-YqQq6CLvkBS8YFs_x8YlNT1I214Jfo4LWnZDWvoGW_5E4Yz_cDFkNZzcXiQEKmNFaiIU5yB7oAUkdrI; sgid=16-47716061-AV6q9PLkn1PPRsZplD8M1kY'}
        html2 = requests.get(url, headers=header).text
        selector2 = etree.HTML(html2)
        return selector2


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
    if (page == None):
        print("return none in get_html")
        return None
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
    hot = 0
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
        post = float(post_view[0])
        view = float(post_view[1])
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
        hot = hot+0.1+post*5+view*8
    print(i)
    return [hot,data_set]
