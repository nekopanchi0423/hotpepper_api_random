import requests
import json

url = "http://zip.cgis.biz/csv/zip.php"
payload = {"zn": "9608043"}

r = requests.get(url, params=payload)

data = r.text
print(data)