import datetime


class Aggregate:

    def __init__(self):
        self.__tweet_list = []

    @property
    def tweet_list(self):
        return self.__tweet_list

    @tweet_list.setter
    def tweet_list(self, tweet_list: list):
        self.__tweet_list = tweet_list

    def sort_tweet(self, tweet_list):
        data_list = {}
        if tweet_list:
            for tweet in tweet_list:
                tweet_datetime = datetime.datetime.strptime(str(tweet[1]), '%Y-%m-%d %H:%M:%S')
                dt = '{}/{}/{} {:02}:{:02}'.format(tweet_datetime.year, tweet_datetime.month, tweet_datetime.day,
                                                   tweet_datetime.hour, tweet_datetime.minute, tweet_datetime.second)
                if dt in data_list:
                    val = data_list[dt]
                    data_list[dt] = val + 1
                else:
                    data_list[dt] = 1

        return data_list
