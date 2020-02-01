# 7.9 時系列データ中の欠損値の取り扱い

# 問題
# 時系列データ中に欠損値がある。

import pandas as pd
import numpy as np

# 日時データを作成
time_index = pd.date_range('1/1/2001', periods=5, freq='M')

# データフレームを作成し、インデックスを設定
dataframe = pd.DataFrame(index=time_index)

# 欠損値を含む特徴量を作成
dataframe['Sales'] = [1.0, 2.0, np.nan, np.nan, 5.0]

# 欠損値を内挿して補完
print(dataframe.interpolate())

# 前方補完
print(dataframe.ffill())

# 後方補完
print(dataframe.bfill())
