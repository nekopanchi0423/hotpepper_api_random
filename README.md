# hotpepper_api_random
ホットペッパーのAPIを使って、飲食店をランダムに提案してくれるプログラムです。

# ホットペッパーAPI
無料で使えるホットペッパーAPIを使います。利用するには登録が必要です。  
ホットペッパーAPIリファレンス → [ホットペッパー | APIリファレンス - リクルートWEBサービス](https://webservice.recruit.co.jp/doc/hotpepper/reference.html). 
ホットペッパーAPIはここから登録 → [APIキー発行登録 - リクルートWEBサービス](https://webservice.recruit.co.jp/register/). 
(登録は数分程度で完了できます)

# プログラムの流れ
1. キーワードを入力
2. キーワードをもとに飲食店を検索
3. 検索結果を取得し、そこからランダムで飲食店を選択する

# コードの説明
```python
import requests
import random

URL = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'

API_KEY = '取得したAPIキー'
KEYWORD = input('キーワードを入力：')
```
最初にPythonAPIを叩くのに必要なrequestsとリストの要素をランダムに抽出するためにrandomを呼び出します。次にリクエストURLを指定しています。リクエストURLは変わっている可能性があるので、APIリファレンスで確認してください。そして、登録申請で取得したAPIキーを設定していきます。
<br>
```python
body = {
    'key':API_KEY,
    'keyword':KEYWORD,
    'format':'json',
    'count':100
}
```
bodyにAPIキーと各パラメータを指定していきます。今回はjson形式で、検索結果の最大出力データ数を100で設定しています。
<br>
```python
response = requests.get(URL,body)
```
getメソッドでリクエストを送ります。
<br>
```python
datum = response.json()
stores = datum['results']['shop']
select_shop = random.sample(stores, 3)
for store_info in select_shop:
    genre = store_info['genre']['name']
    name = store_info['name']
    hp = store_info['urls']['pc']
    print(genre, name, hp)
```
jsonデータを取得し、さらにそこからお店のデータを取得しています。random.sampleによって、ランダムに飲食店情報を3つ選ぶようにしていますが、ここは自由に1個や10個にカスタマイズ可能です。ループ処理の中では、お店のジャンルと店名、URLを表示するようにしています。

### コード全体
```python
import requests
import random

URL = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'

API_KEY = '取得したAPIキー'
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
```

# 実行例
```terminal
$ python hotpepper_api.py
キーワードを入力：札幌駅
居酒屋 炭火居酒屋 炎 北2条店 https://www.hotpepper.jp/strJ001040307/?vos=nhppalsa000016
居酒屋 ミートボーイニューヨーク MEAT BOY N.Y 札幌駅前店 https://www.hotpepper.jp/strJ001009952/?vos=nhppalsa000016
居酒屋 楓 Kaede 札幌駅前店 https://www.hotpepper.jp/strJ001028475/?vos=nhppalsa000016
```
