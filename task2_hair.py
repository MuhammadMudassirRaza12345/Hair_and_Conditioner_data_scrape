import requests 
from bs4 import BeautifulSoup
import pandas as pd
base_url = "https://www.lushusa.com/hair/?cgid=all-hair&start=0&sz=56"
response = requests.get(url=base_url)
# print(response.text)
# type(response.text)
soup = BeautifulSoup(response.text, "html.parser")
# print(soup)

div_of_product_title=soup.select('div.d-flex div.product-tile')
print(div_of_product_title)

produt_name=soup.select_one('div.d-flex div.product-tile h3.product-tile-name').text.strip() 
# print(produt_name)

original_price=soup.select_one("div.d-flex div.tile-price-size span.tile-price").text.strip()
# print(original_price)

size=soup.select_one("div.d-flex div.product-tile div.tile-price-size span.tile-size").text.strip().replace('/','')
# print(size)


 

df2=pd.DataFrame()

for i in div_of_product_title:
    produt_name=i.select_one('div.d-flex div.product-tile h3.product-tile-name').text.strip() 
    print(produt_name)
    original_price=i.select_one("div.d-flex div.tile-price-size span.tile-price").text.strip()
    print(original_price)
    size=i.select_one("div.d-flex div.product-tile div.tile-price-size span.tile-size").text.strip().replace('/','')
    print(size)
    hair_data_dict = {
    "produt_name":produt_name,
    "original_price":original_price,
    "size":  size
    }
    df2=df2.append(hair_data_dict,ignore_index=True)


print(df2)    
df2.to_csv("hair_data.csv")





 
 
    
    

 
   