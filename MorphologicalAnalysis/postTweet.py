# config.pyの読み込み
import config
# OAuthのライブラリの読み込み
from requests_oauthlib import OAuth1Session

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
# 認証処理
twitter = OAuth1Session(CK, CS, AT, ATS)

# ツイートポストエンドポイント
url = "https://api.twitter.com/1.1/statuses/update.json"

print("内容を入力してください。")
# キーボード入力の取得
tweet = input('>> ')
print('*******************************************')

params = {"status" : tweet}

# post送信
res = twitter.post(url, params=params)

# 正常投稿出来た場合
if res.status_code == 200:
    print("Success.")
# 正常投稿出来なかった場合
else:
    print("Failed. : %d"% res.status_code)
