# 7.4 日付データを複数の特徴量を分解

# 問題
# 日時データを収めた列がある。この列から、年月日時分をそれぞれ別の特徴量として取り出したい。

import pandas as pd

# データフレームを作成
dataframe = pd.DataFrame()

# 日時データを作成
dataframe['date'] = pd.date_range('1/1/2001', periods=150, freq='W')

# 年月日時分を特徴量として作成
dataframe['year'] = dataframe['date'].dt.year
dataframe['month'] = dataframe['date'].dt.month
dataframe['day'] = dataframe['date'].dt.day
dataframe['hour'] = dataframe['date'].dt.hour
dataframe['minute'] = dataframe['date'].dt.minute

print(dataframe.head(3))
