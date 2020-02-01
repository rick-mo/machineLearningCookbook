# 7.5 日付の差の算出

# 問題
# 2つの日時特徴量がある。観測値ごとにその差を計算したい。

import pandas as pd

# データフレームを作成
dataframe = pd.DataFrame()

# 2つの日時特徴量を作成
dataframe['Arrive'] = [pd.Timestamp('01-01-2017'), pd.Timestamp('01-04-2017')]
dataframe['Left'] = [pd.Timestamp('01-01-2017'), pd.Timestamp('01-06-2017')]

# 2つの日時特徴量の差を計算
print(dataframe['Left'] - dataframe['Arrive'])

# 単位をdaysではなく数値とする
print(pd.Series(delta.days for delta in (dataframe['Left'] - dataframe['Arrive'])))
