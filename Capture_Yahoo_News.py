#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from bs4 import BeautifulSoup

from datetime import datetime                  # import時間函數
data = requests.get('https://tw.yahoo.com/')   # Get Yahoo 首頁內容
soup = BeautifulSoup(data.text, 'html.parser') 

file = open('Yahoo_News.txt', 'w')
news = soup.find_all('a', class_='story-title')   #抓出各頭條新聞
file.write('Date: ' + datetime.now().strftime('%Y-%m-%d') + ' / Time: ' + datetime.now().strftime('%H:%M:%S') +'\nYahoo 首頁焦點新聞\n')  #此刻時間功能
print('Date: ' + datetime.now().strftime('%Y-%m-%d') + ' / Time: ' + datetime.now().strftime('%H:%M:%S') +'\n')
print('Yahoo 首頁焦點新聞')

for x in news:
    print('標題：'+ x.text + '\n' + x.get('href') + '\n\n')
    file.write('標題：' + x.text + '\n' + x.get('href') + '\n\n')


file.close()                                         # 寫入完成關閉檔案
input()                                              # 程式暫停在輸出畫面

