# -*- coding: utf-8 -*-
# @Time    : 2018/3/6 11:25
# @Author  : Liunux
# @Email   : 103996977@qq.com
# @File    : crawl.py.py
# @Software: PyCharm

from bs4 import BeautifulSoup
import requests
import csv

csv_file = open("rent.csv","w")
csv_writer = csv.writer(csv_file, delimiter=',')

for i in range(1,3):
    start_url="http://gz.58.com/chuzu/b12/pn{page}".format(page=i)
    print (start_url)
    start_html=requests.get(start_url)
    pager=BeautifulSoup(start_html.text,'lxml')
    info_list=pager.find_all(class_='des')
    for info in info_list:
        name=info.h2.a.text.strip()
        print (name)
        money=pager.find(class_='money').text.strip()
        try:
            location=info.find(class_='add').find_all('a')[1].text.strip().replace('.','')
        except:
            location=info.find(class_='add').find_all('a')[0].text.strip().replace('.','')
        url=info.h2.a["href"].strip()
        csv_writer.writerow([name,money,location,url])

'''
    csv_writer.writerow([name,money,url])
TypeError: a bytes-like object is required, not 'str'
解决办法：python3中csv_file = open("rent.csv","w") 为w 不能是wb
'''