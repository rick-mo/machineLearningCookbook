# 3.2 データの性質を取得

# 問題
# DataFrameの何らかの性質を表示したい。

import pandas as pd

# URLを作成
url = 'https://tinyurl.com/titanic-csv'

# データをロード
dataframe = pd.read_csv(url)

# 最初の2行を表示
print(dataframe.head(2))

# データの形状を表示
print(dataframe.shape)

# 統計量を表示
print(dataframe.describe())
