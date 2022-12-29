import requests
import random

URL = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'

API_KEY = '0ca1dae061b9cc16'
KEYWORD = input('キーワードを入力：')

body = {
    'key':API_KEY,
    'keyword':KEYWORD,
    'format':'json',
    'count':100
}

response = requests.get(URL,body)

datum = response.json()
stores = datum['results']['shop']
select_shop = random.sample(stores, 3)
for store_info in select_shop:
    genre = store_info['genre']['name']
    name = store_info['name']
    hp = store_info['urls']['pc']
    print(genre, name, hp)
# for store_name in stores:
#    name = store_name['name']
#    print(name)