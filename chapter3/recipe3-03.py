# 3.3 DataFrameの操作

# 問題
# DataFrameから、一部のデータやスライスを選択したい。

import pandas as pd

# URLを作成
url = 'https://tinyurl.com/titanic-csv'

# データをロード
dataframe = pd.read_csv(url)

# 最初の行を選択
print(dataframe.iloc[0])

# 2、3、4行目を選択
print(dataframe.iloc[1:4])

# 1〜4行目を選択
print(dataframe.iloc[:4])

# インデックスを設定
dataframe = dataframe.set_index(dataframe['Name'])

# 行を表示
print(dataframe.loc['Allen, Miss Elisabeth Walton'])

# DataFrameで個々の行や行スライスを指定する方法
# ・DataFrameのインデックスがラベルの場合にはlocを用いる。
# ・DataFrameでの位置を用いる場合にはilocを用いる。
