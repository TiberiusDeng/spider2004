import requests
import json
import re
import csv
import pandas as pd
RAW_COOKIE = 'ABTEST=6|1589445065|v17;IPLOC=CN1100;SUID=2DABCE654F18910A000000005C9E628E;PHPSESSID=noim89j9f8mv7s57gqeanpctv6;SUIR=7366557983'

class cookiepool():
    def __init__(self):
        self.cookiepool = pd.DataFrame(columns=["SNUID"])
        self.output_dir = 'D:/work/spider2004/data/wc_cookie.csv'
        self.url = "https://www.sogou.com/web?query=333&_asf=www.sogou.com&_ast=1488955851&w=01019900&p=40040100&ie=utf8&from=index-nologin"
        self.cookie = {'Cookie':RAW_COOKIE}
        self.df = pd.read_csv(self.output_dir)
    #产生cookie池，每次增加十个
    def gen_cookiepool(self):
        url = self.url
        cookiepool = self.cookiepool
        headers = self.cookie
        for i in range(10):
            f = requests.head(url, headers=headers).headers
            a = json.loads(json.dumps(dict(f)))  # a的类型为dict
            list = a.get('Set-Cookie')
            pattern = re.compile(r'SNUID=(.*?);')
            SNUID = pattern.findall(list)[0] #获取SNUID
            #print(SNUID)
            cookiepool = cookiepool.append({"SNUID":SNUID},ignore_index=True)
        cookiepool.to_csv(self.output_dir,mode='a+',header=False, index=False)
    #删除cookie池最后一项（调用过的）
    #todo 调用失败，可能是因为已经打开文件了
    def del_SNUID(self):
        df = self.df
        df.drop([len(df)-1],inplace=True)
        df.to_csv(self.output_dir,header=False,index=False)

    def get_new_cookies(self):
        df = self.df
        count = len(df)
        print(count)
        if count<5:
            self.gen_cookiepool()
        else:
            print('enoughSNUID')
        line = df.iloc[-1,0]
        print(line)
        str_list = [RAW_COOKIE,';SNUID={}']
        a = ''
        cookie_val = a.join(str_list).format(line)
        new_cookie = {'Cookie':cookie_val}
        self.del_SNUID()
        return new_cookie
