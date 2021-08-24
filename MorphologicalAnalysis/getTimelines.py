# 標準のjsonモジュールとconfig.pyの読み込み
import json
import config
# OAuthのライブラリの読み込み
from requests_oauthlib import OAuth1Session

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
# 認証処理
twitter = OAuth1Session(CK, CS, AT, ATS)

# タイムライン取得エンドポイント
url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

# 取得数
params = {'count': 1000}
res = twitter.get(url, params=params)

# 正常通信出来た場合
if res.status_code == 200:
    # レスポンスからタイムラインリストを取得
    timelines = json.loads(res.text)
    # タイムラインリストをループ処理
    for line in timelines:
        print(line['user']['name']+'::'+line['text'])
        print(line['created_at'])
        print('*******************************************')
# 正常通信出来なかった場合
else:
    print("Failed: %d" % res.status_code)
