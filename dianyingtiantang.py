import bs4,sys
import os
import requests
import urllib
import re
import time
os.makedirs('dianyingtiantang',exist_ok=True)


#print(url)
#http://www.dytt8.net/html/gndy/dyzz/2.html
#f_u2获取最终页面的ftp地址
def f_u2(url):
    #time.sleep(2)
    res=requests.get(url)
    res.encoding='gb2312'
    html=res.text
    #print(html)
    webre = re.compile(r'href="(.*?)">ftp:')
    webref = re.findall(webre,html)[0]
    print(webref)
    return(webref)
#url='http://www.dytt8.net/html/gndy/dyzz/20180909/57421.html'
#f_u2(url)

#获得列表界面的网址
def f_u1(url):
    headers={'User-Agent':
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
    response=requests.get(url,headers=headers)
    response.raise_for_status()
    html=response.text
#用正则表达式子找到网址
    webre=re.compile(r'href="/html/gndy/dyzz/(.*?.html)')
    webref=re.findall(webre,html)
    a=[ ]
    for i in webref:
        whweb='http://www.dytt8.net/html/gndy/dyzz/'+i
        time.sleep(0.8)
        a.append(f_u2(whweb))
    for kk in a:
        f = open('./dianyingtiantang/movieweb1.txt', 'a+', encoding='utf-8')
        f.write('%s' % (kk))
        f.write("\n")
        f.close()
#主程序，加入首页
url=['http://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'.format(str(i)) for i in range(2,10)]
url.insert(0,'http://www.dytt8.net/html/gndy/dyzz/index.html')
#开始爬取
for i in range(0,9):
    f_u1(url[i])
#保存到movieweb.txt中
print('Successfully!!!')
