import tkinter
from MorphologicalAnalysis import getTweet, mecab
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class MainUi:

    def __init__(self):
        # メイン画面
        self.mainWin = tkinter.Tk()
        self.mainWin.title('形態素解析')
        self.mainWin.geometry('700x600')

        self.canvas = tkinter.Canvas(self.mainWin, height=350, width=760, relief=tkinter.SOLID)
        self.fig = plt.Figure()
        self.cvs = FigureCanvasTkAgg(self.fig, master=self.canvas)

        self.label = tkinter.Label(self.mainWin, text='検索ワードを入力してください : ')
        self.search_text = tkinter.Entry(self.mainWin, width=80, bd=1)
        self.search_button = tkinter.Button(self.mainWin, text='クリア', width=10, command=self.search_clear)
        self.clear_button = tkinter.Button(self.mainWin, text='検索', width=10, command=self.search_push)

        # 表示設定
        self.setting()

        self.mainWin.mainloop()

    def setting(self):
        # フレーム
        self.canvas.place(x=20, y=100)
        # ラベル
        self.label.place(x=20, y=10)
        # テキストボックス
        self.search_text.place(x=190, y=10)
        # クリアボタン
        self.clear_button.place(x=600, y=50)
        # 検索
        self.search_button.place(x=500, y=50)

    def search_push(self):
        word = self.search_text.get()
        if word == '':
            tkinter.messagebox.showerror('入力エラー', '検索ワードを入力してください')
        else:
            self.data_plot()

    def data_plot(self):
        # twitterインスタンス作成
        tw = getTweet.GetTweet()
        # ツイートの取得
        tweet_list = tw.get_tweet(self.search_text.get())

        # Mecabを使用して形態素解析
        mb = mecab.mecab(tweet_list)
        mb.analysis()
        print(mb.rtn_list)

        # グラフ作成
        ax = self.fig.add_subplot(111)
        ax.hist(mb.rtn_list, bins=50, range=(-1, 1))
        ax.set_title('P/N Frequency of Twitter')
        ax.set_xlabel("P/N value")
        ax.set_ylabel("Frequency")

        self.cvs.draw()
        self.cvs.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    def search_clear(self):
        self.search_text.delete('0', 'end')
        self.cvs.get_tk_widget().destroy()
