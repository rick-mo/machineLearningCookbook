# 4.10 欠損値がある観測値を取り除く

# 問題
# 欠損値がある観測値を取り除くコードは、NumPyを使えば簡単に書ける。

import numpy as np

# 特徴量行列を作成
features = np.array([
  [1.1, 11.1],
  [2.2, 22.2],
  [3.3, 33.3],
  [4.4, 44.4],
  [np.nan, 55],
])

# 欠損値のない観測値だけを残す
print(features[~np.isnan(features).any(axis=1)])

# pandasを使って、欠損している観測値だけを捨てることも可能

import pandas as pd

dataframe = pd.DataFrame(features, columns=['feature_1', 'feature_2'])

print(dataframe.dropna())

# ほとんどの機械学習アルゴリズムは、欠損値に対応出来ないため、前処理で対応する。
# 最も簡単な対応方法は、欠損値のある観測点を削除すること。
# ただしこの場合は、観測点の欠損地以外に含まれる情報を失うことになる。
