# 1.19 行列の乗算

# 問題
# 2つの行列を掛け合わせたい。

import numpy as np

# 行列を作成
matrix_a = np.array([[1, 1], [1, 2]])

# 行列を作成
matrix_b = np.array([[1, 3], [1, 2]])

# 2つの行列を乗算
print(np.dot(matrix_a, matrix_b))

# Python3.5以降、@演算子を使用して乗算することが可能
print(matrix_a @ matrix_b)

# 2つの行列の要素ごとの乗算は、*演算子を使用する
print(matrix_a * matrix_b)
