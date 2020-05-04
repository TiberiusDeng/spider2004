import requests
from lxml import  etree
import traceback
import re
from header import wechat_header
def get_html(url):
    try:
        header = wechat_header()
        html = requests.get(url,headers = header).text.replace('<!--red_beg-->','').replace('<!--red_end-->','').replace('<em>','').replace('</em>','')
        selector = etree.HTML(html)
        return selector
    except Exception as e:
        print('Error: ', e)
        traceback.print_exc()
def single_page_proc(url):
    html = get_html(url)
    if html == None:
        return [None, None]
    infolist = []

def get_text(url):
    try:
        header = wechat_header()
        text = requests.get(url,headers = header).text
        return text
    except Exception as e:
        print('Error: ', e)
