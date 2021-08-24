# config.pyの読み込み
import tweepy
import config

# 認証情報の取得
CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET


class GetTweet:

    def get_tweet(self, word):
        # twitterの認証
        auth = tweepy.OAuthHandler(CK, CS)
        auth.set_access_token(AT, ATS)
        api = tweepy.API(auth)

        # 検索情報
        q = word
        count = 100

        # 検索情報保存リスト
        tweet_list = []

        tweets = api.search(q=q, locale="ja", count=count, tweet_mode='extended')
        for tweet in tweets:
            tweet_list.append([tweet.id, tweet.created_at, tweet.full_text, tweet.favorite_count])

        return tweet_list

    def show_tweet(self):
        # 表示
        for tweet in self.__tweet_list:
            print('twid : {}'.format(tweet[0]))
            print('date : {}'.format(tweet[1]))
            print(tweet[2])
            print('fava : {}'.format(tweet[3]))
            print('=' * 80)
