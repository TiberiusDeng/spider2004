import csv
import json
import os
from kernel import single_page_proc
import time
import datetime
import pandas as pd
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
        self.hot_day = []  # todo 每日热度
        self.data = pd.DataFrame(columns=["id", "comment_num", "forward", "like", "time"])
        self.output_dir = 'D:/weibo_result.csv'
    #def request(self):

    #def analysis(self):

    #def set_parameter(self):

    #def output(self):

    def run(self):
        for day in self.date_list:
            hot_by_day = 0
            for hour in range(24):
                hot = 0 #todo 每小时热度
                #todo 构建每日表
                for page in range(50):
                    st = "{}-{}{}-{}{}-{}".format(day.year, if_add_zero(day.month), day.month,
                                                  if_add_zero(day.day), day.day, hour)
                    et = "{}-{}{}-{}{}-{}".format(day.year, if_add_zero(day.month), day.month,
                                                  if_add_zero(day.day), day.day, hour + 1)
                    url = generate_search_url_weibo(self.keyword, page + 1, st, et)

                    [single_page, single_page_df] = single_page_proc(url)


                    if (single_page==None):
                        break#todo 确实可以跳出此级循环
                    else:
                        hot = hot + single_page
                        time.sleep(3)
                    single_page_df['time'] = day
                    if (self.data.empty):
                        self.data = single_page_df
                    else:
                        self.data = pd.concat([self.data, single_page_df], ignore_index=True)
                hot_by_day = hot_by_day + hot

                print("hour = %d" % hour)
                print("hot = %f" % hot)
            #todo 导出list
            #self.hot_day.append(hot_by_day)
            print("%d" % (day.day))
            self.popularity.append({'today_hot':hot_by_day})
            print(hot_by_day)
        print(self.popularity)

    #def reset(self):

    def output_print(self):
        for i in self.popularity:
            print(self.popularity)

    def print_data(self):
        print(self.data)

    def output_file(self):
        self.data.to_csv(self.output_dir, sep=',', header=True, index=True,
                         encoding = 'utf_8_sig')

    def set_output_dir(self, out_dir):
        self.output_dir = out_dir


def main():
    try:
        st = datetime.date(2020, 2, 15)
        et = datetime.date(2020, 4, 15)
        day = timedelta(days=1)
        date_list = []
        for i in range((et - st).days):
            date_list.append(st + i * day)
        wbspd = WeiboSpider('动物森友会', date_list)
        wbspd.run()  # 爬取信息
        wbspd.print_data()
        wbspd.set_output_dir('D:/work/spider2004/result.csv')
        wbspd.output_file()
    except Exception as e:
        print('Error: ', e)
        #traceback.print_exc()


if __name__ == '__main__':
    main()