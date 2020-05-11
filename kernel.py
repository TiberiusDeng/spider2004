import requests
from lxml import  etree
import traceback
import re
import numpy
import pandas as pd
from tools.proxypool_connect import get_ip

def get_html(url,header):
    try:
        proxy = get_ip()
        proxies = {
            'http': 'http://' + proxy,
            'https': 'https://' + proxy
        }
        html = requests.get(url,headers = header,proxies=proxies).content #TODO bytes型如何查找
        selector = etree.HTML(html)
        noresult = selector.xpath('//*[@id="pl_feedlist_index"]//div[@class="card card-no-result s-pt20b40"]') #判断页面是否有内容
        if len(noresult):
            return None
        else:
            return selector #todo 查找迭代器内是否有元素
    except Exception as e:
        print('Error: ', e)
        traceback.print_exc()
#TODO 返回etree解析后的页面，还需设置cookie等其他参数

def ifNone(item):
    if not item:
        item = '0'
    return item

def content_proc(item):
    sincontent = item.xpath("normalize-space(string(.))")
    content = re.sub(r'\u200b|\ue627', '', sincontent)
    return content

def single_page_proc(url, header=''):
    if not header:
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36',
            'Cookie': 'UM_distinctid=16fc3f4312f572-0828f60c43b54-c383f64-1fa400-16fc3f43130583; SINAGLOBAL=7069396849272.771.1579540558483; un=tom123156@sina.com; UOR=login.sina.com.cn,vdisk.weibo.com,www.baidu.com; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW4mZj5Ic3JNch96O_OPTwR5JpX5KMhUgL.Fo2pSK.NSo.cSoz2dJLoIEBLxKBLB.qLBo2LxK-L122L1-zLxKBLB.eLB.BLxKMLB.BL1KMt; SCF=AufY7eUSyXlc1zEsy79SvgaNfq2-weR2j3qQieICIferqJrmNeUKbhrDfH-q2c8LELyLwe6wWKYT3dV5MDStz1c.; SUB=_2A25zrEpIDeThGedP7lsW9ifKzT6IHXVQ2DyArDV8PUNbmtAKLUzEkW9NX29I_3SdFX8zr55X8UC41HXPp5vBHdIl; SUHB=079ybQ1zM4bVrX; ALF=1619619223; SSOLoginState=1588083224; wvr=6; _s_tentry=www.baidu.com; Apache=1989272299331.1328.1588083236785; ULV=1588083236853:13:6:1:1989272299331.1328.1588083236785:1587704095996; webim_unReadCount=%7B%22time%22%3A1588083268742%2C%22dm_pub_total%22%3A2%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A53%2C%22msgbox%22%3A0%7D'
            #'Cookie': 'SINAGLOBAL=2418040951545.7856.1548059733707; UM_distinctid=170a9cbb12746b-0c8af34a752b61-4313f6a-144000-170a9cbb12841c; UOR=www.oracle.com,widget.weibo.com,login.sina.com.cn; un=20michael@sina.com; wvr=6; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhbhcQFFEpeFqfwBdXwVShB5JpX5KMhUgL.FozXSKzNeh.f1h22dJLoI7Uhds8Eq-y2; ALF=1618981962; SSOLoginState=1587445963; SCF=AmbSbnez8JBPvVvRWHN5b8GN-zkSHYHh00YZZWiR9L0qkjvJIqiyzxiSrIY2FP-_zIpA0zS9OwAEC7csp8BModU.; SUB=_2A25zmvCbDeRhGeRK7lAW8CfJwz2IHXVQ7mVTrDV8PUNbmtAKLUjNkW9NU1PQwBnUhDt9ncLTaefjTwMeOQ9nq-_B; SUHB=08JKiSgRI3FCCP; _s_tentry=login.sina.com.cn; Apache=5355000148563.683.1587445966359; ULV=1587445966372:20:3:2:5355000148563.683.1587445966359:1586871065796; webim_unReadCount=%7B%22time%22%3A1587446048235%2C%22dm_pub_total%22%3A135%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A1%2C%22msgbox%22%3A2%7D2418040951545.7856.1548059733707; UM_distinctid=170a9cbb12746b-0c8af34a752b61-4313f6a-144000-170a9cbb12841c; UOR=www.oracle.com,widget.weibo.com,login.sina.com.cn; un=20michael@sina.com; wvr=6; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhbhcQFFEpeFqfwBdXwVShB5JpX5KMhUgL.FozXSKzNeh.f1h22dJLoI7Uhds8Eq-y2; ALF=1618981962; SSOLoginState=1587445963; SCF=AmbSbnez8JBPvVvRWHN5b8GN-zkSHYHh00YZZWiR9L0qkjvJIqiyzxiSrIY2FP-_zIpA0zS9OwAEC7csp8BModU.; SUB=_2A25zmvCbDeRhGeRK7lAW8CfJwz2IHXVQ7mVTrDV8PUNbmtAKLUjNkW9NU1PQwBnUhDt9ncLTaefjTwMeOQ9nq-_B; SUHB=08JKiSgRI3FCCP; _s_tentry=login.sina.com.cn; Apache=5355000148563.683.1587445966359; ULV=1587445966372:20:3:2:5355000148563.683.1587445966359:1586871065796; webim_unReadCount=%7B%22time%22%3A1587446048235%2C%22dm_pub_total%22%3A135%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A1%2C%22msgbox%22%3A2%7D'
            #'Cookie': 'UM_distinctid=16fc3f4312f572-0828f60c43b54-c383f64-1fa400-16fc3f43130583; SINAGLOBAL=7069396849272.771.1579540558483; un=tom123156@sina.com; un=tom123156@sina.com; wvr=6; login_sid_t=b0497c3d4951e8fd40a028e1c947f968; cross_origin_proto=SSL; _s_tentry=passport.weibo.com; UOR=login.sina.com.cn,vdisk.weibo.com,www.baidu.com; Apache=5010395057361.728.1587444554059; ULV=1587444554070:11:4:1:5010395057361.728.1587444554059:1587135246872; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW4mZj5Ic3JNch96O_OPTwR5JpX5K2hUgL.Fo2pSK.NSo.cSoz2dJLoIEBLxKBLB.qLBo2LxK-L122L1-zLxKBLB.eLB.BLxKMLB.BL1KMt; ALF=1618980560; SSOLoginState=1587444560; SCF=AufY7eUSyXlc1zEsy79SvgaNfq2-weR2j3qQieICIferTJjImNXtF-v8xe-HnJRlT9SfEDssq8S8HDRzHlwmBJw.; SUB=_2A25zmgsADeThGedP7lsW9ifKzT6IHXVQ7nvIrDV8PUNbmtCOLULtkW9NX29I_zhCKzdLtph8ue6TqILTXEKAXujj; SUHB=0D-U4hiaCGa017; webim_unReadCount=%7B%22time%22%3A1587444847864%2C%22dm_pub_total%22%3A2%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A50%2C%22msgbox%22%3A0%7D'
            #'Cookie': '16fc3f4312f572-0828f60c43b54-c383f64-1fa400-16fc3f43130583; SINAGLOBAL=7069396849272.771.1579540558483; un=tom123156@sina.com; wvr=6; Ugrow-G0=6fd5dedc9d0f894fec342d051b79679e; login_sid_t=b0497c3d4951e8fd40a028e1c947f968; cross_origin_proto=SSL; TC-V5-G0=799b73639653e51a6d82fb007f218b2f; WBStorage=42212210b087ca50|undefined; _s_tentry=passport.weibo.com; UOR=login.sina.com.cn,vdisk.weibo.com,www.baidu.com; Apache=5010395057361.728.1587444554059; ULV=1587444554070:11:4:1:5010395057361.728.1587444554059:1587135246872; wb_view_log=1920*10801; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW4mZj5Ic3JNch96O_OPTwR5JpX5K2hUgL.Fo2pSK.NSo.cSoz2dJLoIEBLxKBLB.qLBo2LxK-L122L1-zLxKBLB.eLB.BLxKMLB.BL1KMt; ALF=1618980560; SSOLoginState=1587444560; SCF=AufY7eUSyXlc1zEsy79SvgaNfq2-weR2j3qQieICIferTJjImNXtF-v8xe-HnJRlT9SfEDssq8S8HDRzHlwmBJw.; SUB=_2A25zmgsADeThGedP7lsW9ifKzT6IHXVQ7nvIrDV8PUNbmtCOLULtkW9NX29I_zhCKzdLtph8ue6TqILTXEKAXujj; SUHB=0D-U4hiaCGa017; wb_view_log_1159769662=1920*10801; TC-Page-G0=04dc502e635144031713f186989293c7|1587444563|1587444563; webim_unReadCount=%7B%22time%22%3A1587444564875%2C%22dm_pub_total%22%3A2%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A50%2C%22msgbox%22%3A0%7D'
            #'Cookie': '2418040951545.7856.1548059733707; UM_distinctid=170a9cbb12746b-0c8af34a752b61-4313f6a-144000-170a9cbb12841c; _s_tentry=www.baidu.com; Apache=936137947756.5701.1586871065760; ULV=1586871065796:19:2:1:936137947756.5701.1586871065760:1585981660045; UOR=www.oracle.com,widget.weibo.com,login.sina.com.cn; login_sid_t=502fc2479cfec138908e63a95733d619; cross_origin_proto=SSL; un=20michael@sina.com; SSOLoginState=1587237127; un=20michael@sina.com; wvr=6; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhbhcQFFEpeFqfwBdXwVShB5JpX5KMhUgL.FozXSKzNeh.f1h22dJLoI7Uhds8Eq-y2; ALF=1618888314; SCF=AmbSbnez8JBPvVvRWHN5b8GN-zkSHYHh00YZZWiR9L0qpZn1dlczwxkRdLBEKV6_Np0vvRrm1REBUc61bBteExQ.; SUB=_2A25zmWKqDeRhGeRK7lAW8CfJwz2IHXVQ79NirDV8PUNbmtAKLXbskW9NU1PQwA_0LLrRt-i0Gzujpz9G20g3l5EB; SUHB=0xnzPMhm5uXSIc'
            #'Cookie':'16fc3f4312f572-0828f60c43b54-c383f64-1fa400-16fc3f43130583; SINAGLOBAL=7069396849272.771.1579540558483; UOR=login.sina.com.cn,vdisk.weibo.com,www.baidu.com; login_sid_t=9ae580473c017ff479f8e80bb779cc67; cross_origin_proto=SSL; _s_tentry=passport.weibo.com; Apache=92364930047.13075.1587135246861; ULV=1587135246872:10:3:3:92364930047.13075.1587135246861:1586969290193; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW4mZj5Ic3JNch96O_OPTwR5JpX5K2hUgL.Fo2pSK.NSo.cSoz2dJLoIEBLxKBLB.qLBo2LxK-L122L1-zLxKBLB.eLB.BLxKMLB.BL1KMt; SSOLoginState=1587135656; SCF=AufY7eUSyXlc1zEsy79SvgaNfq2-weR2j3qQieICIfervAWRkxBvpLtu9DZIP2kJjgUMf_5sa3MZVqpI6zZB2Kk.; SUB=_2A25znbT4DeThGedP7lsW9ifKzT6IHXVQ6qEwrDV8PUJbmtAKLUGlkW9NX29I_zIXVF4MbVM5-jCY2V25QAptf_U-; SUHB=0mxFTTLlGeOCbl; un=tom123156@sina.com; wvr=6; webim_unReadCount=%7B%22time%22%3A1587135722295%2C%22dm_pub_total%22%3A2%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A55%2C%22msgbox%22%3A0%7D'
        }#todo 换cookie才能跑
    html = get_html(url, header)
    if html == None:
        return [None, None]
    infolist = []
    nicks = html.xpath('//*[@id="pl_feedlist_index"]//div[@class = "content"]/div[@class = "info"]//a[@class = "name"]')
    comments = html.xpath('//*[@id="pl_feedlist_index"]//div[@class = "card"]/div[@class = "card-act"]//li[3]/a')
    forwards = html.xpath('//*[@id="pl_feedlist_index"]//div[@class = "card"]/div[@class = "card-act"]//li[2]/a')
    likes = html.xpath('//*[@id="pl_feedlist_index"]//div[@class = "card"]/div[@class = "card-act"]//li[4]/a/em')
    contents = html.xpath(
        '//*[@id="pl_feedlist_index"]//div[@class = "content"]/p[@class = "txt"][last()]')  # todo [last()]取了p下的最后一个标签（即展开后的）
    i = 0
    hot = 0
    data_set = pd.DataFrame(columns=["id", "comment_num", "forward", "like"])

    for nick in nicks:
        forward = forwards[i].text
        comment = comments[i].text
        forward = float(ifNone(re.sub(r'\D', '', forward)))
        comment = float(ifNone(re.sub(r'\D', '', comment)))
        like = float(ifNone(likes[i].text))  # todo 先判断是否为空
        content = content_proc(contents[i])
        single_info = {
            'nickname': nick.text,
            'forward': forward,
            'comment': comment,
            'like': like,
            'content': content
        }
        infolist.append(single_info)
        data_item = {"id": nick.text, "comment_num": comment, "forward": forward, "like": like}
        data_set = data_set.append(data_item, ignore_index=True)
        #print(data_item)
        i = i + 1
        hot = hot + like * 0.1 + forward * 0.5 + comment * 0.05
    print(i)

        # if __debug__:
        #     print(single_info)
        #     print(hot)
        #     print('html = %s' % html)
        #     print('hot = %f' % hot)

    return [hot, data_set]#todo 返回单页热度值