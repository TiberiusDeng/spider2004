from get_html import get_html
import re
url = 'https://s.weibo.com/weibo?q=%E5%8A%A8%E7%89%A9%E6%A3%AE%E5%8F%8B%E4%BC%9A&page=1&suball=1&Refer=g&timescope=custom%3A2020-03-01-0%3A2020-03-01-1'#'https://s.weibo.com/weibo/%25E5%258A%25A8%25E6%25A3%25AE?topnav=1&wvr=6&page=1'
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36',
    'Cookie':'16fc3f4312f572-0828f60c43b54-c383f64-1fa400-16fc3f43130583; SINAGLOBAL=7069396849272.771.1579540558483; UOR=login.sina.com.cn,vdisk.weibo.com,www.baidu.com; login_sid_t=9ae580473c017ff479f8e80bb779cc67; cross_origin_proto=SSL; _s_tentry=passport.weibo.com; Apache=92364930047.13075.1587135246861; ULV=1587135246872:10:3:3:92364930047.13075.1587135246861:1586969290193; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW4mZj5Ic3JNch96O_OPTwR5JpX5K2hUgL.Fo2pSK.NSo.cSoz2dJLoIEBLxKBLB.qLBo2LxK-L122L1-zLxKBLB.eLB.BLxKMLB.BL1KMt; SSOLoginState=1587135656; SCF=AufY7eUSyXlc1zEsy79SvgaNfq2-weR2j3qQieICIfervAWRkxBvpLtu9DZIP2kJjgUMf_5sa3MZVqpI6zZB2Kk.; SUB=_2A25znbT4DeThGedP7lsW9ifKzT6IHXVQ6qEwrDV8PUJbmtAKLUGlkW9NX29I_zIXVF4MbVM5-jCY2V25QAptf_U-; SUHB=0mxFTTLlGeOCbl; un=tom123156@sina.com; wvr=6; webim_unReadCount=%7B%22time%22%3A1587135722295%2C%22dm_pub_total%22%3A2%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A55%2C%22msgbox%22%3A0%7D'
}

html = get_html(url,header)

infolist = []

nicks = html.xpath('//*[@id="pl_feedlist_index"]//a[@class = "name"]')
comments = html.xpath('//*[@id="pl_feedlist_index"]//li[3]/a')
reposts = html.xpath('//*[@id="pl_feedlist_index"]//li[2]/a')
likes = html.xpath('//*[@id="pl_feedlist_index"]//li[4]/a/em')
contents = html.xpath('//*[@id="pl_feedlist_index"]//p[@class = "txt"][last()]') #todo [last()]取了p下的最后一个标签（即展开后的）

def ifNone(item):
    if item == None:
        item = '0'
    return item
def content_proc(item):
    sincontent = item.xpath("normalize-space(string(.))")
    content = re.sub(r'\u200b|\ue627', '', sincontent)
    return content

i = 0
hot = 0.0
for nick in nicks:
    #nick = nicks[i].text
    repost = reposts[i].text
    comment = comments[i].text
    like = ifNone(likes[i].text) #todo 先判断是否为空
    content = content_proc(contents[i])

    infolist.append({
        'nickname': nick.text,
        'repost': repost,
        'comment': comment,
        'like': like,
        'content': content
    })
    i = i + 1
    #print(comment)
    if re.search('\d+', repost):
        repost_val = re.search('\d+', repost).group()
    else:
        repost_val = 0
    like_val = like
    if re.search('\d+', comment):
        comment_val = re.search('\d+', comment).group()
    else:
        comment_val = 0
    #print(repost_val)
    hot = hot + float(like_val) * 0.1 + float(repost_val) * 0.5 + float(comment_val) * 0.05

print(infolist)
print(hot)




