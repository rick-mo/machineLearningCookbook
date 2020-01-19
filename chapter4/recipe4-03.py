# 4.3 観測値の正規化

# 問題
# 観測値の特徴量の値を単位ノルム(長さ1)となるようにスケールを変換したい。

import numpy as np
from sklearn.preprocessing import Normalizer

# 特徴量行列を作成
features = np.array([
  [0.5, 0.5], 
  [1.1, 3.4], 
  [1.5, 20.2], 
  [1.63, 34.4], 
  [10.9, 3.3]
])

# 正規化器を作成(l2:ユークリッドノルム)
normalizer = Normalizer(norm='l2')

# 特徴量行列を変換
features_l2_norm = normalizer.transform(features)

# 特徴量行列を表示
print(features_l2_norm)

# 特徴量行列を変換(l1:マンハッタンノルム)
features_l1_norm = Normalizer(norm='l1').transform(features)

# 特徴量行列を表示
print(features_l1_norm)
