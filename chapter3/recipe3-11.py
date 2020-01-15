# 3.11 行の削除

# 問題
# 1つもしくはそれ以上の列をDataFrameから削除したい。

import pandas as pd

# URLを作成
url = 'https://tinyurl.com/titanic-csv'

# データをロード
dataframe = pd.read_csv(url)

# 現在の列の状態
print(dataframe.head(2))

# 行を削除して最初の2行を表示
print(dataframe[dataframe['Sex'] != 'male'].head(2))

# 特定の行を削除
print(dataframe[dataframe['Name'] != 'Allison, Miss Helen Loraine'].head(2))

# 最初の行を削除
print(dataframe[dataframe.index != 0].head(2))
