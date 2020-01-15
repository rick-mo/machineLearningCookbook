# 3.8 ユニークな値の算出

# 問題
# ある列にある全てのユニークな値を知りたい。すなわち重複を排除した値のリストを取得したい。

import pandas as pd

# URLを作成
url = 'https://tinyurl.com/titanic-csv'

# データをロード
dataframe = pd.read_csv(url)

# ユニークな値のリストを取得
print(dataframe['Sex'].unique())

# 現れた回数を表示
print(dataframe['Sex'].value_counts())

# カウント数を表示し、問題なデータが含まれることを確認
print(dataframe['PClass'].value_counts())

# ユニークな値の数を表示
print(dataframe['PClass'].nunique())
