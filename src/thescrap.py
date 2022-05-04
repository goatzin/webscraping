# Hello O_o
from bs4 import BeautifulSoup
import requests

URL = "https://www.amazon.com.br/gp/browse.html?node=16364755011&ref_=nav_em__pc_laptops_0_2_15_3"
headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36" }
site = requests.get(URL, headers=headers)
soup = BeautifulSoup(site.content, "html.parser")

products = soup.find_all("span", class_="a-size-base a-color-base")
prices = soup.find_all("span", class_="a-price-whole")

for p, product in enumerate(products):
    for s, price in enumerate(prices):
        if p == s:
            print(product.get_text().strip())
            print(price.get_text().strip())

