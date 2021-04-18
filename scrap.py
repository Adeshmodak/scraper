import requests
from bs4 import BeautifulSoup
import time
import csv 
import mail_send
from datetime import date

urls=["https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch","https://finance.yahoo.com/quote/GOOGL?p=GOOGL&.tsrc=fin-srch","https://finance.yahoo.com/quote/MSFT?p=MSFT&.tsrc=fin-srch"]
headers={'user-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}

today = str(date.today()) + ".csv"
csv_file = open(today,"w")
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Stock Name','Previous Close','Open','Bid','Ask','Day Range','52 Week Range','Volume','Avg. Volume	'])

for url in urls:
    stock=[]
    html_pg=requests.get(url,headers=headers)
    soup=BeautifulSoup(html_pg.content,'lxml')

    h_info=soup.find_all("div",id="quote-header-info")[0]
    stock_title= h_info.find("h1").get_text()
    Current_price= h_info.find("div",class_="My(6px) Pos(r) smartphone_Mt(6px)").find("span").get_text()
    
    stock.append(stock_title)
    stock.append(Current_price)

    table_info = soup.find_all("div",class_="D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)")[0].find_all("tr")

    for i in range(0,8):
        head=table_info[i].find_all("td")[0].get_text()
        value=table_info[i].find_all("td")[1].get_text()
        stock.append(value)

    csv_writer.writerow(stock)
    time.sleep(5)
   
    
csv_file.close()
mail_send.send(filename=today)