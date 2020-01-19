# 4.5 特徴量の変換

# 問題
# 複数の特徴量に対して特別な変換を行いたい。

import numpy as np
from sklearn.preprocessing import FunctionTransformer

# 特徴量行列を作成
features = np.array([
  [2, 3], 
  [2, 3], 
  [2, 3], 
])

# 簡単な関数を定義
def add_test(x):
  return x + 10

# 変換器を作成
ten_transformer = FunctionTransformer(add_test)

# 特徴量行列を変換
print(ten_transformer.transform(features))

# pandasのapplyを用いても同じことができる

import pandas as pd

df = pd.DataFrame(features, columns=['feature_1', 'feature_2'])

# 関数を適用
print(df.apply(add_test))
