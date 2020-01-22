# 5.1 名義カテゴリ特徴量の数値化

# 問題
# 本質的に順序を持たない名義クラスを持つ特徴量(例:りんご、梨、バナナ)がある。

import numpy as np
from sklearn.preprocessing import LabelBinarizer, MultiLabelBinarizer

# 特徴量を作成
feature = np.array([['Texas'], ['California'], ['Texas'], ['Delaware'], ['Texas']])

# ワンホットエンコーダを作成
one_hot = LabelBinarizer()

# 特徴量をワンホットエンコード
print(one_hot.fit_transform(feature))

# 特徴量クラスを表示
print(one_hot.classes_)

# ワンホットエンコードされた特徴量を逆変換
print(one_hot.inverse_transform(one_hot.transform(feature)))

# pandasを用いてワンホットエンコードすることも可能

import pandas as pd

# 特徴量からダミー変数を生成
print(pd.get_dummies(feature[:,0]))

# scikit_learnは、個々の特徴量クラスのリストである場合にも対応できる。

# 複数クラス特徴量を作成
multiclass_feature = [
  ('Texas', 'Florida'), 
  ('California', 'Alabama'),
  ('Texas', 'Florida'),
  ('Delware', 'Florida'),
  ('Texas', 'Alabama'),
]

# 複数クラス用ワンホットエンコーダを作成
one_hot_multiclass = MultiLabelBinarizer()

# 複数クラス特徴量をワンホットエンコード
print(one_hot_multiclass.fit_transform(multiclass_feature))

# クラスを表示
print(one_hot_multiclass.classes_)

