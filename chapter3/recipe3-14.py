# 3.14 時刻による行のグループ分け

# 問題
# 時刻を用いて行をグループ分けしたい。

import pandas as pd
import numpy as np

# シード値を設定
np.random.seed(0)

# 日時の範囲を作成
time_index = pd.date_range('06/06/2017', periods=100000, freq='30S')

# DataFrameを作成
dataframe = pd.DataFrame(index=time_index)

# ランダムな値の行を作成
dataframe['Sale_Amount'] = np.random.randint(1, 10, 100000)

# 1週間ごとにグループ分けして、週ごとに値を集計
print(dataframe.resample('W').sum())

print(dataframe.resample('M').count())

# labelパラメータ：表示する時間グループを変更する
print(dataframe.resample('M', label='left').count())
