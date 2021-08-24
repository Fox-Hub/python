import MeCab
import re
import pandas as pd


class mecab:

    def __init__(self, tweet_list):
        self.tweet_list = tweet_list
        self.__rtn_list = []

    def analysis(self):
        # 辞書の読み込み
        pn_df = pd.read_csv('pn_ja.dic.txt',
                            sep=':',
                            encoding='utf-8',
                            names=('Word', 'Reading', 'POS', 'PN')
                            )
        # listへ変換
        word_list = list(pn_df['Word'])
        pn_list = list(pn_df['PN'])

        for tweet in self.tweet_list:
            point = 0
            count = 0
            parse = MeCab.Tagger().parse(tweet[2])
            lines = parse.split('\n')
            items = (re.split('[\t]]', line) for line in lines)

            for item in items:
                key = item[0].split(',')[0].split('\t')
                # EOSだったら終了
                if key[0] == 'EOS' or len(key) < 2:
                    break
                # 品詞を取得
                hinshi = key[1]
                # 単語を取得
                word = key[0]

                if not (hinshi in ['名詞', '動詞', '形容詞']):
                    continue

                # 取得した単語の原型が含まれているか
                for i in range(0, len(word_list)):
                    if word_list[i] == word:
                        count += 1
                        point += pn_list[i]
                        break

            if point != 0 or count != 0:
                p_n_value = point / count
                self.__rtn_list.append(p_n_value)
                print(tweet[2])
                print('point : {}, count : {}'.format(point, count))

    @property
    def rtn_list(self):
        return self.__rtn_list
