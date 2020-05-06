import time
import datetime
import re
from wc_kernel import get_html
from wc_kernel import get_text
from url import  generate_search_url_wechat
from wc_kernel import single_page_proc
import pandas as pd
import requests
from lxml import etree
url = generate_search_url_wechat('动物森友',1,2)
html = get_html(url)

class WechatSpider(object):
    def __init__(self, keyword):
        self.popularity = []
        self.keyword = keyword
        self.data = pd.DataFrame(columns=['title','article_link','author','author_link','post','view','post_time'])
        self.output_dir = 'D:/wechatsogou_result.csv'
    def run(self):
        total_hot = 0
        page = 0
        for page in range(100):
            hot = 0
            url = generate_search_url_wechat(self.keyword,page+1,2)
            [single_page_hot, single_page_df] = single_page_proc(url)
            if (single_page_hot == None):
                break  # todo 确实可以跳出此级循环
            else:
                hot = hot + single_page_hot
                total_hot = total_hot +hot
                time.sleep(3)
            print("hot_page = %f" % hot)
            print("page = %d" %page)
        print("total_hot = %f" % total_hot)

def main():
    try:
        wcspd = WechatSpider('动物森友')
        wcspd.run()
    except Exception as e:
        print('Error: ', e)

if __name__ == '__main__':
    main()


