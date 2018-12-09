mport re
import requests
import time
from bs4 import BeautifulSoup

url='http://www.huajiao.com/category/1000'
#url='http://www.huajiao.com/l/253573735'
#技术不行，处理不了多个标签，只能用个函数了，哭死
def jjjj(tages,s):
    tage=''
    for i in range(s):
        tage=tage+' '+tages[i].get_text()
    return(tage)
#爬取一个主播网址标签
def url_part(url1,nn):

    headers = {'User-Agent':
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
    time.sleep(0.5)
    res1 = requests.get(url1, headers=headers)
    res1.encoding = 'utf-8'
    resp=res1.text
    #print(resp)
    soup=BeautifulSoup(resp,'lxml')
    names=soup.select('div.username > a > h3')
    tags=soup.select('.tag')
    s=len(tags)
    watches=soup.select('div.watches > p > span')
    #print(tags)
    fans=soup.select('span.number.js-fans')
    praises = soup.select('span.number.js-praises')
    currencys = soup.select('span.number.js-currency')
    followings = soup.select('span.number.js-followings')
    levels = soup.select('.number.js-level')
    authorlevels = soup.select('.number.js-authorlevel')
    alldata=[ ]
    for name,tag,watch,fan,praise,currency,following,level,authorlevel in zip(names,tags,watches,fans,praises,currencys,followings,levels,authorlevels):
        data={
            'name':name.get_text(),
            'tag':jjjj(tags,s),
            'watch':watch.get_text(),
            'fan':fan.get_text(),
            'praise':praise.get_text(),
            'currency':currency.get_text(),
            'following':following.get_text(),
            'level':level.get_text(),
            'authorlevel':authorlevel.get_text()
        }
        data.update({'url':url1})
        alldata.append(data)
    fb = open('huajiao.csv', 'a', encoding='utf-8')
    # 写表头
    if nn==1:
        fb.write('名字,标签,观看人数,粉丝,获赞,关注,用户等级,主播等级，url\n')
    # 一个商品一行数据
        for item in alldata:
            temp = '{name},{tag},{watch},{fan},{praise},{currency},{following},{level},{authorlevel},{url}\n'.format(**item)
            fb.write(temp)
        fb.close()
    else:
        for item in alldata:
            temp = '{name},{tag},{watch},{fan},{praise},{currency},{following},{level},{authorlevel},{url}\n'.format(**item)
            fb.write(temp)
        fb.close()
    print(alldata)
#找到界面列表中全部的链接
def url_main(url):
    headers={'User-Agent':
             'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
    res=requests.get(url,headers=headers)
    html=res.text
    webre = re.compile(r'<a href="(.*?)" class="figure"')
    webref = re.findall(webre,html)
    n=0
    for i in webref:
        pweb='http://www.huajiao.com'+i
        n=n+1
        print(pweb)
        time.sleep(2)
        url_part(pweb,n)

url_main(url)

