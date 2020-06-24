#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from bs4 import BeautifulSoup                          #import BeautifulSoup套件
from datetime import datetime                          # import時間函數
 
ptt = input('您想要抓取哪個PTT版的資料? ')
url = 'https://www.ptt.cc/bbs/' + ptt + '/index.html'  
x = input('您想要抓取最新幾頁的資料? ')
y = int(x)                                             # 輸入為str型態，轉為int
file = open('Output.txt', 'w')                         # 建立並開啟 Output.txt，參數w為覆寫 Output.txt內容
file.write('PTT '+ ptt + ' 版的資料\n' + 'Date:' + datetime.now().strftime('%Y-%m-%d') + ' / Time:' + datetime.now().strftime('%H:%M:%S') +' Updated\n\n')

if y > 0: 
    print('抓取' + ptt + '版最新' + x + '頁的資料，從最新到舊排序\n')
    for i in range(y):        
        response = requests.get(url)
        soup = BeautifulSoup(response.text,'html.parser')                       #以html.parser來解析
        data = soup.select('div.title a, div.date, div.author, div.nrec span')  #抓取 標題 / 時間 / 作者 / 推文數，F12網站解析找到對應的html屬性
        icon = soup.select('div.btn-group.btn-group-paging a')                  # ptt中 最舊 / 上頁 / 下頁 / 最新 icon 所對應的 div class

        print ('本頁網址: '+ url)
        file.write('本頁網址: '+ url) 
        for s in data: 
            print(s.text)
            file.write(s.text + '\n')                # 寫入檔案
            
        url = 'https://www.ptt.cc'+ icon[1]['href']  # 上一頁網址，最舊icon[0] / 上頁icon[1] 
        
else:
    print('Error, 請輸入正數 !!')
    
    
file.close()                                         # 寫入完成關閉檔案
input()                                              # 程式暫停在輸出畫面

