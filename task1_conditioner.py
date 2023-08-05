import requests 
from bs4 import BeautifulSoup
import pandas as pd
base_url = "https://www.lushusa.com/hair/conditioners/"
response = requests.get(url=base_url)
# print(response.text)
# type(response.text)
soup = BeautifulSoup(response.text, "html.parser")
# print(soup)

div_of_product_title=soup.select('div.product-tiles')
# print(div_of_title)

produt_name=soup.select_one('div.d-flex div.product-tile h3.product-tile-name').text.strip() 
print(produt_name)

original_price=soup.select_one("div.d-flex:nth-of-type(7) div.tile-price-size span.tile-price").text.strip()
print(original_price)

size=soup.select_one("div span.tile-size ").text.strip().replace('/','')
print(size)


 

df1=pd.DataFrame()

for i in div_of_product_title:
    produt_name=i.select_one('div.d-flex div.product-tile h3.product-tile-name').text.strip()
    print(produt_name)
    original_price=i.select_one("div.d-flex div.tile-price-size span.tile-price").text.strip()
    print(original_price)
    size=i.select_one("div span.tile-size ").text.strip().replace('/','')
    print(size)
    conditioner_data_dict = {
    "produt_name":produt_name,
    "original_price":original_price,
    "size":  size
    }
    df1=df1.append(conditioner_data_dict,ignore_index=True)


print(df1)    
df1.to_csv("conditioner_data.csv")





 
 
    
    

# def extract_conditioner_data(conditioner_block, conditioner_data_dict):
#     for i, quote in enumerate(quotes_block):
#         quote_text = quote.select_one('span.text').text.strip()
#         author = quote.select_one('small.author').text.strip()
#         try:
#             author_url = quote.select_one('span a').get('href')
#         except:
#             author_url = 'NONE'
#         conditioner_data_dict['quote_text'].append(quote_text)
#         conditioner_data_dict['author'].append(author)
#         conditioner_data_dict['author_url'].append(author_url)

# extract_conditioner_data(conditioner_block, conditioner_data_dict) 
   