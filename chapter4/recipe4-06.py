# 4.6 外れ値の検出

# 問題
# 他の観測値と大きく異なる観測値(外れ値:outlier)を特定したい。

import numpy as np
from sklearn.covariance import EllipticEnvelope
from sklearn.datasets import make_blobs

# 簡単な人工データを生成
features, _ = make_blobs(n_samples=10, n_features=2, centers=1, random_state=1)

# 最初の特徴量の値を極端な値に置換
features[0, 0] = 10000
features[0, 1] = 10000

# 検出器を作成(contamination:データがどの程度クリーンであるかを推定した値)
outlier_detector = EllipticEnvelope(contamination=.1)

# 検出器を訓練
outlier_detector.fit(features)

# 外れ値を予測
print(outlier_detector.predict(features))
