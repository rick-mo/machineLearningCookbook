# 4.4 多項式特徴量と交互作用特徴量

# 問題
# 多項式特徴量(polynomial feature)と、交互作用特徴量(interaction feature)を生成したい。

import numpy as np
from sklearn.preprocessing import PolynomialFeatures

# 特徴量行列を作成
features = np.array([
  [2, 3], 
  [2, 3], 
  [2, 3], 
])

# PolynomialFeaturesオブジェクトを作成
polynomial_interaction = PolynomialFeatures(degree=2, include_bias=False)

# 多項式特徴量を作成
print(polynomial_interaction.fit_transform(features))

interaction = PolynomialFeatures(degree=2, include_bias=False, interaction_only=True)
print(interaction.fit_transform(features))

# 多項式特徴量は、特徴量とターゲットの間に非線形な関係がありそうな場合によく用いられる。
# 交互作用特徴量は、個々の特徴量の積である。
