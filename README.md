# Explanation for README_Capture_PTT_Data 
# 使用BeautifulSoup套件抓取&解析資料
# 再使用 html.parser 來解析
# 按照PTT網頁F12後所對應的 標題 / 時間 / 作者 / 推文數 部分做選取
# 因為我是寫更新最新幾頁的，因此會從新至舊，以需要抓取前幾頁的功能
# "上頁" button 是對應到 div.btn-group.btn-group-paging a 這部分
# 後來再Print出來，寫入txt檔
# txt檔會出現在 "user名稱" 的資料夾裡
# 先輸入您想要抓取PTT哪個版 E.g. Salary / Boy-Girl ...
# 再輸入您想抓取的頁數，如果是最新的一頁就是 1
# 會print出該PTT您所選取幾頁的資料，並寫入名為"Output"的txt裡




# Explanation for README_Capture_Yahoo_News
# 相較於上一支program，這支就比較簡單
# 一樣使用使用Beautiful套件，可將Yahoo首頁的 焦點/運動/娛樂/觀點/生活/影音 這幾個Topic & url link print出來
# 並寫入 txt 檔

