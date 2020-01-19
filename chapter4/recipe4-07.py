# 4.7 外れ値の取り扱い

# 問題
# 外れ値がある。

# 方法1:外れ値を捨てる。

import pandas as pd

# DataFrameを作成
houses = pd.DataFrame()
houses['Price'] = [534433, 392333, 293222, 4322032]
houses['Bathrooms'] = [2, 3.5, 2, 116]
houses['Square_Feet'] = [1500, 2500, 1500, 48000]

# 観測値をフィルタリング
print(houses[houses['Bathrooms'] < 20])

# 方法2:外れ値に印を付け、それを特徴量として取り込む。

import numpy as np

# 真偽条件に基づいて特徴量を作る
houses['Outlier'] = np.where(houses['Bathrooms'] < 20, 0, 1)

print(houses)

# 方法3:特徴量を変換して、外れ値の影響を小さくする。

# 特徴量を対数にする
houses['Log_Of_Square_Feet'] = [np.log(x) for x in houses['Square_Feet']]

print(houses)
