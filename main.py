import csv
import json
import os
from kernel import single_page_proc
import time
import datetime
from url import generate_search_url_weibo

from datetime import timedelta

from collections import OrderedDict

def if_add_zero(val):
    if val < 10:
        return '0'
    else:
        return ''

class WeiboSpider(object):
    def __init__(self, keyword, date_list):
        self.popularity = []
        self.keyword = keyword
        self.date_list = date_list
        self.timestep = 0



    #def request(self):

    #def analysis(self):

    #def set_parameter(self):

    #def output(self):

    def run(self):
        for day in self.date_list:
            hot_by_day = 0
            for hour in range(22):
                hot = 0
                for page in range(50):
                    st = "{}-{}{}-{}{}-{}".format(day.year, if_add_zero(day.month), day.month,
                                                  if_add_zero(day.day), day.day, hour)
                    et = "{}-{}{}-{}{}-{}".format(day.year, if_add_zero(day.month), day.month,
                                                  if_add_zero(day.day), day.day, hour + 1)
                    url = generate_search_url_weibo(self.keyword, page + 1, st, et)

                    single_page = single_page_proc(url)
                    if(single_page==None):
                        break#todo 确实可以跳出此级循环
                    else:
                        hot = hot + single_page
                        time.sleep(3)
                hot_by_day = hot_by_day + hot
            self.popularity.append(hot_by_day)
            print(hot_by_day)


    #def reset(self):

    def output_print(self):
        for i in self.popularity:
            print(self.popularity)



def main():
    try:
        st = datetime.date(2020, 3, 1)
        et = datetime.date(2020, 3, 5)
        day = timedelta(days=1)
        date_list = []
        for i in range((et - st).days):
            date_list.append(st + i * day)
        wbspd = WeiboSpider('动物森友会', date_list)
        wbspd.run()  # 爬取信息
    except Exception as e:
        print('Error: ', e)
        #traceback.print_exc()


if __name__ == '__main__':
    main()