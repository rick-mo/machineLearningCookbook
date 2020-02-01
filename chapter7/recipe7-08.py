# 7.8 移動時間窓の利用

# 問題
# 時系列データの移動時間窓に対して、統計量を計算したい。

import pandas as pd

# 日時データを作成
time_index = pd.date_range('1/1/2001', periods=5, freq='M')

# データフレームを作成し、インデックスを設定
dataframe = pd.DataFrame(index=time_index)

# 特徴量を作成
dataframe['Stock_Price'] = [1, 2, 3, 4, 5]

# 移動平均を計算
print(dataframe.rolling(window=2).mean())
