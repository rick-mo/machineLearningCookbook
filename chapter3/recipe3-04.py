# 3.4 条件を用いた行の選択

# 問題
# 何らかの条件を用いてDataFrameの行を選択したい。

# Titanicのデータセットから全ての女性を選択する。

import pandas as pd

# URLを作成
url = 'https://tinyurl.com/titanic-csv'

# データをロード
dataframe = pd.read_csv(url)

# Sex列がfemaleの行のうち、最初の2行を表示
print(dataframe[dataframe['Sex'] == 'female'].head(2))

# 複数条件の場合：65歳以上の女性を選択
print(dataframe[(dataframe['Sex'] == 'female') & (dataframe['Age'] >= 65)])
