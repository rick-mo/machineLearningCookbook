# 3.13 値による行のグループ分け

# 問題
# ある列の値で、行をグループ分けしたい。

import pandas as pd

# URLを作成
url = 'https://tinyurl.com/titanic-csv'

# データをロード
dataframe = pd.read_csv(url)

# Sex列の値で行をグループ分けし、グループごとの平均値を計算
print(dataframe.groupby('Sex').mean())

# 沈没を生き延びたかどうかでグループ分けし、グループごとに名前の数を数える
print(dataframe.groupby('Survived')['Name'].count())

# ある列でグループ分けした結果を、さらに別の列でグループ分けする
print(dataframe.groupby(['Sex', 'Survived'])['Age'].mean())
