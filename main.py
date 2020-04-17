import csv
import json
import os
import requests
from collections import OrderedDict

class WeiboSpider(object):
    def __init__():
        self.hot =

    def generate_search_url_weibo(keyword, page=1, timesn=WechatSogouConst.search_article_time.anytime,
                            st=None, et=None):
        assert isinstance(page, int) and page > 0

        url_sufix = OrderedDict()
        url_sufix["page"] = page
        url_sufix["suball"] = 1  #代表是全部类型，有的是含图片什么的
        url_sufix["Refer"] = "g" #或weibo_weibo代表搜索的是综合
        if st or et:
            url_sufix[]



    def request(self):

    def analysis(self):

    def set_parameter(self):

    def output(self):

    def run(self):

    def reset(self):



def main():
    try:
        config_path = os.path.split(
            os.path.realpath(__file__))[0] + os.sep + 'config.json'
        if not os.path.isfile(config_path):
            sys.exit(u'当前路径：%s 不存在配置文件config.json' %
                     (os.path.split(os.path.realpath(__file__))[0] + os.sep))
        with open(config_path) as f:
            try:
                config = json.loads(f.read())
            except ValueError:
                sys.exit(u'config.json 格式不正确，请参考 '
                         u'https://github.com/dataabc/weiboSpider#3程序设置')
        wbspd = WeiSpider(config)
        wbspd.run()  # 爬取信息
    except Exception as e:
        print('Error: ', e)
        traceback.print_exc()


if __name__ == '__main__':
    main()