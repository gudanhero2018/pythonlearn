import requests
import re
import os
import bs4
import urllib

k=1
while k!=23:

    url = 'http://www.umei.cc/p/gaoqing/cn/%s.htm'%k
    k+=1
    # 模拟抓取目标网站链接
    page = requests.get(url)
    page.encoding = 'utf-8'
    html = page.text
    soup = bs4.BeautifulSoup(page.text)

    # 新建文件夹
    os.makedirs('pic', exist_ok=True)

    # 找到src且后缀为.jpg的链接

    # imgre=re.compile(r'src="(.+?\.jpg)"')
    # picref=re.findall(imgre,html)
    # picref=soup.select('img[src]')
    picref = soup.select('.TypeList img[src]')
    picname = soup.select('.ListTit')
    # print(picname)

    # 显示照片的名字
    nam = []
    for i in picname:
        b = i.get_text()
        nam.append(b)
    print(nam)

    # 开始下载图片
    n = 0
    for img_url in picref:
        res = img_url.get('src')
        urllib.request.urlretrieve(res, './pic/%s.jpg' % nam[n])
        n += 1

    # 完成抓取，看图吧！！！'''
