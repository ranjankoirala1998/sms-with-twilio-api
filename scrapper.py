from bs4 import BeautifulSoup
import requests
import pandas as pd

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}

url = "https://merolagani.com/StockQuote.aspx"

r = requests.get(url)

soup = BeautifulSoup(r.text, 'lxml')

columns = ['As Of']
for elem in soup.find_all('span') :
    try :
        columns.append(elem['title'])
    except:
        continue

def getValues() :

    d = soup.find('span', {'id' : "ctl00_ContentPlaceHolder1_lblMarketDate"}).text.split()
    date = ' '.join(d[2:])

    table = soup.find('table', {'class':'table table-bordered table-striped table-hover sortable'})
    table_body = table.find('tbody')

    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        
        values = [e.text.strip() for e in cols]
        if values[1] == 'CGH' :
            break
    
    values[0] = date 

    for i in range(2,len(values)):
        values[i] = float(values[i].replace(',', ''))

    return values

def get_body() :

    stock_info = getValues()
    cgh = {columns[i]: stock_info[i] for i in range(len(columns))}

    body = """\n****** STOCK INFO ******\n"""
    for key, value in cgh.items() :
        body += f'{key} : {value} \n'
    
    return body
            
