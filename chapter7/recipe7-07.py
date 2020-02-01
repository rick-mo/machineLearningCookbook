# 7.7 時間遅れ特徴量の生成

# 問題
# n時間単位のラグがある(遅れた)特徴量を作りたい。

import pandas as pd

dataframe = pd.DataFrame()

# 日時データを作成
dataframe['dates'] = pd.date_range('1/1/2001', periods=5, freq='D')
dataframe['stock_price'] = [1.1, 2.2, 3.3, 4.4, 5.5]

# 1行分のラグのある値を作成
dataframe['previous_days_stock_price'] = dataframe['stock_price'].shift(1)

print(dataframe)
