# 4.9 クラスタリングによる観測値のグループ分け

# 問題
# 観測値をクラスタに分割して、類似した観測値同士をグループにまとめたい。

# k個のグループがあるとわかっている場合には、k-平均法クラスタリングを用いる。

import pandas as pd
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# 人工的な特徴量行列を作成
features, _ = make_blobs(n_samples=50, n_features=2, centers=3, random_state=1)

# DataFrameを作成
dataframe = pd.DataFrame(features, columns=['feature_1', 'feature_2'])

# k-meansクラスタリング器を作成
clusterer = KMeans(3, random_state=0)

# クラスタリング器を作成
clusterer.fit(features)

# クラスタリングを実行
dataframe['group'] = clusterer.predict(features)

print(dataframe.head(5))
