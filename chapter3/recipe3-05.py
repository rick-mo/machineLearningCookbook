# 3.5 値の置き換え

# 問題
# あるDataFrameの中の値を置き換えたい。

import pandas as pd

# URLを作成
url = 'https://tinyurl.com/titanic-csv'

# データをロード
dataframe = pd.read_csv(url)

# TitanicのデータセットのSex列のfemaleをWomanに置き換える。

# 値を置き換えて、最初の2行を表示
print(dataframe['Sex'].replace('female', 'Woman') .head(2))

# femaleとmaleをWomanとManにそれぞれ置き換える。
print(dataframe['Sex'].replace(['female', 'male'], ['Woman', 'Man']).head(5))

# DataFrame全体を指定すれば、DataFrameオブジェクト全体に対して置き換えを行うことができる。
print(dataframe.replace(1, 'One').head(2))

# replaceには正規表現を使うことができる。
print(dataframe.replace(r'1st', 'First', regex=True).head(2))
