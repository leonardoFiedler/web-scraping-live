from bs4 import BeautifulSoup
import requests
import pandas as pd

# Fazendo a request para o site
r = requests.get("https://egol.fcf.com.br/sisgol/Derw0757_TABELA_POR_FASEB.asp?SelStart1=&SelStop1=&SelStart2=441&SelStop2=441&SelStart3=&SelStop3=&SelStart4=&SelStop4=&SelStart5=&SelStop5=&Index=2&RunReport=Run+Report")

soup = BeautifulSoup(r.text, "html.parser")

# print(soup.prettify)

# Pegando todos os itens da promoção
items = soup.find_all("table", class_="ReportTable")

l_promo = []

# Iterando os itens
found = False
for item in items:
    body = item.text

    if body == "PRIMEIRA FASE":
        found = True
    
    if found:
        tr = item.find("tr")
        td = tr.find_all('td')
        if len(td) > 0:
            pos = td[0].text
            name = td[1].text
            print(f"{pos} | {name}")
