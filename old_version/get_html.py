import requests
from lxml import  etree
import traceback
def get_html(url,header):
    try:
        html = requests.get(url,headers = header).content #TODO cookie参数设不设
        selector = etree.HTML(html)
        return selector
    except Exception as e:
        print('Error: ', e)
        traceback.print_exc()
#TODO 返回etree解析后的页面，还需设置cookie等其他参数

# def get_info(keyword):
#     #url = get_url(keyword)
#     header = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36'
#     }
#     html = get_html(url,header)
#     nickname = html.xpath('//*[@id="pl_feedlist_index"]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/a[1]/text()')
#     print(nickname)