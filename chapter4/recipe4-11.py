# 4.11 欠損値の補完

# 問題
# データに欠損値があり、欠損値を予測した値で補完したい。

# データの量が少ないなら、欠損値をk-最近傍法(KNN)で予測して補完する。

import numpy as np
from fancyimpute import KNN
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_blobs

# 人工的に特徴量行列を作成
features, _ = make_blobs(n_samples=1000, n_features=2, random_state=1)

# 特徴量を標準化
scaler = StandardScaler()
standardized_features = scaler.fit_transform(features)

# 最初の特徴量の最初の値を欠損値に置換
true_value = standardized_features[0, 0]
standardized_features[0, 0] = np.nan

# 特徴量行列中の欠損値を補完
features_knn_imputed = KNN(k=5, verbose=0).complete(standardized_features)
