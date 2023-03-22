from bs4 import BeautifulSoup
import requests
import pandas as pd

# Fazendo a request para o site
r = requests.get("https://www.mercadolivre.com.br/ofertas")

soup = BeautifulSoup(r.text, "html.parser")

# Pegando todos os itens da promoção
items = soup.find_all("div", class_="promotion-item__container")

l_promo = []

# Iterando os itens
for item in items:
    item_content = item.find_all("div", class_="promotion-item__description")
    title = item.find_all("p", class_="promotion-item__title")[0]
    p_symbol = item.find_all("span", class_="andes-money-amount__currency-symbol")[0]

    prices = item.find_all("span", class_="andes-money-amount__fraction")

    if len(prices) >= 2:
        p_old = prices[0]
        p_current = prices[1]
    else:
        p_old = -1
        p_current = prices[0]

    promo = {
        "title": title.text,
        "price_old": "Não Informado" if type(p_old) is int else p_old.text,
        "price_current": p_current.text,
        "price_symbol": p_symbol.text,
    }

    l_promo.append(promo)


print("Vamos as promoções do dia!")
for promo in l_promo:
    print(
        f"{promo['title']} de {promo['price_symbol']}{promo['price_old']} por {promo['price_symbol']}{promo['price_current']}"
    )

df = pd.DataFrame.from_dict(l_promo, orient="columns")
df.to_csv("promos.csv", index=False)
