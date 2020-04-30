import sys
sys.path.append('../')
import weibo_spider
import datetime

try:
    st = datetime.date(2020, 2, 15)
    et = datetime.date(2020, 4, 15)
    day = datetime.timedelta(days=1)
    date_list = []
    for i in range((et - st).days):
        date_list.append(st + i * day)
    wbspd = weibo_spider.WeiboSpider('动物森友会', date_list)
    wbspd.run()  # 爬取信息
    wbspd.print_data()
    wbspd.set_output_dir('D:/work/spider2004/result.csv')
    #wbspd.output_file()
except Exception as e:
    print('Error: ', e)