# 5.3 特徴量辞書の数値化

# 問題
# 特徴量行列に変換したい辞書がある。

from sklearn.feature_extraction import DictVectorizer

# 辞書を作成
data_dict = [
    {'Red': 2, 'Blue': 4},
    {'Red': 4, 'Blue': 3},
    {'Red': 1, 'Yellow': 2},
    {'Red': 2, 'Yellow': 2},
]

# 辞書ベクトル変換器を作成
dictvectorizer = DictVectorizer(sparse=False)

# 辞書を特徴量行列に変換
features = dictvectorizer.fit_transform(data_dict)

print(features)

# 特徴量の名前を取得
feature_names = dictvectorizer.get_feature_names()

print(feature_names)

# pandasのDataFrameを作って、出力された特徴量をわかりやすく表示する。

import pandas as pd

print(pd.DataFrame(features, columns=feature_names))
