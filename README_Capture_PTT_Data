import requests
from bs4 import BeautifulSoup                     # import BeautifulSoup套件
 
ptt = "https://www.ptt.cc/bbs/Salary/index.html"  # Salary網址

x = input("您想要抓取Salary版最新幾頁的資料? ")

y = int(x)                      # 輸入為str型態，轉為int

file = open("Salary.txt", "w")  # 創造並開啟Salary.txt，參數w為覆寫 Salary.txt內容

if y > 0: 

    print("抓取Salary " + x + "頁的資料，從最新到舊排序\n")
    
    
    for i in range(y):        
        response = requests.get(ptt)
        soup = BeautifulSoup(response.text,"html.parser")                       #以html.parser來解析
        data = soup.select("div.title a, div.date, div.author, div.nrec span")  #抓取標題 / 時間 / 作者 / 推文數，F12網站解析找到對應的html屬性
        icon = soup.select("div.btn-group.btn-group-paging a")                  #ptt中 最舊 / 上頁 / 下頁 / 最新 icon 所對應的 div class
        
        print ("本頁網址: "+ ptt)
        file.write("本頁網址: "+ ptt) 
        for s in data: 
            print(s.text)
            file.write(s.text + "\n")                # 寫入檔案
  
        ptt = "https://www.ptt.cc"+ icon[1]["href"]  # 上一頁網址，最舊icon[0] / 上頁icon[1]     
else:

     print("Error, 請輸入正數 !!")
    
file.close()                                         #寫入完成關閉檔案




