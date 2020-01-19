# 4.2 特徴量の標準化

# 問題
# 特徴量を平均が0で標準偏差が1になるように変換したい。

import numpy as np
from sklearn import preprocessing

# 特徴量を作成
x = np.array([[-1000.1], [-200.2], [500.5], [600.6], [9000.9]])

# スケール変換器を作成
scaler = preprocessing.StandardScaler()

# 特徴量を変換
standardized = scaler.fit_transform(x)

# 特徴量を表示
print(standardized)

# 値が特徴量の平均値から標準偏差でいくつ離れているかを示す特徴量(Zスコアと呼ぶ)
# 一般にはこのスケール変換方法が機械学習でmin-maxスケール変換よりも用いられるが、
# どちらを用いるかは、機械学習のアルゴリズムに依存する。

# 平均と標準偏差を表示
print('平均:', round(standardized.mean()))
print('標準偏差:', round(standardized.std()))

# データ中に、値が他のものと大きく異なる「外れ値」があると、
# 特徴量の平均と分散が影響されるため、標準化がうまく機能しない。

# スケール変換器を作成
robust_scaler = preprocessing.RobustScaler()

# 特徴量を変換
print(robust_scaler.fit_transform(x))
