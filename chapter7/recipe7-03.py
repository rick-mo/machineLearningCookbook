# 7.3 日付と時間による選択

# 問題
# 日時データを格納したベクトルから、いくつかの日時を選択したい。

import pandas as pd

# データフレームを作成
dataframe = pd.DataFrame()

# 日時データを作成
dataframe['date'] = pd.date_range('1/1/2001', periods=100000, freq='H')

# 2つの日時の間の観測値を選択
print(dataframe[
  (dataframe['date'] > '2002-1-1 01:00:00') &
  (dataframe['date'] <= '2002-1-1 04:00:00')
])

# locを用いてスライスを取得する方法もある

# dateをインデックスとして設定
dataframe = dataframe.set_index(dataframe['date'])

# 2つの日時の間の観測値を選択
print(dataframe.loc['2002-1-1 01:00:00' : '2002-1-1 04:00:00'])
