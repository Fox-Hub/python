from matplotlib import pyplot as plt


class Graph:

    def drawing(self, data_list):

        # 日付を昇順にソート
        # data_list = sorted(data_list.items(), key=lambda x: x[0])
        # print(data_list)

        # データの定義
        # x_list = [key[0] for key in data_list]
        # x_list = [data[0:4] for data in data_list]

        # グラフの描画
        plt.hist(data_list, bins=50, range=(-1, 1))
        plt.title('P/N Frequency of Twitter')
        plt.xlabel("P/N value")
        plt.ylabel("Frequency")
        plt.show()
