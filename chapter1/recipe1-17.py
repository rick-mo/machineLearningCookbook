# 1.17 内積の計算

# 問題
# 2つのベクトルの内積を計算したい。

import numpy as np

# 2つのベクトルを作成
vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])

# 内積を計算
print(np.dot(vector_a, vector_b))

# python3.5以降では、@演算子を用いて内積が算出可能
print(vector_a @ vector_b)
