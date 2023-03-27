from bs4 import BeautifulSoup
import requests
import pandas as pd

# Fazendo a request para o site
r = requests.get("https://www.mercadolivre.com.br/ofertas")

soup = BeautifulSoup(r.text, "html.parser")

# Procurando por todas as divs que sejam item
items = soup.find_all("div", "promotion-item__description")

l_promos = []

for item in items:

    # Buscando pelo titulo e pelos valores
    title = item.find("p", "promotion-item__title").text
    value_1 = int(item.find_all("span", "andes-money-amount__fraction")[0].text.replace(".", ""))
    value_2 = int(item.find_all("span", "andes-money-amount__fraction")[1].text.replace(".", ""))

    value_new, value_old = 0, 0

    # Como nao sabemos a ordem dos valores
    # Realize-se o processo de checagem
    if value_1 > value_2:
        value_old = value_1
        value_new = value_2
    else:
        value_new = value_1
        value_old = value_2
    
    # Armazena num dicionario e adiciona na lista
    d_promo = {
        "title": title,
        "value_old": value_old,
        "value_new": value_new
    }

    l_promos.append(d_promo)

    # print(f"{title} | {value_old} | {value_new}")

# Itera a lista de promocoes
# for promo in l_promos:
#     print(f"O produto {promo['title']} passou de R${promo['value_old']} para R${promo['value_new']}")

# Salva em um arquivo csv usando a biblioteca Pandas
df = pd.DataFrame.from_dict(l_promos)

df.to_csv("ml_promo.csv", index=False)