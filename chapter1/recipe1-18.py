# 1.18 行列の加算、減算

# 問題
# 2つの行列の加算、減算を行いたい。

import numpy as np

# 行列を作成
matrix_a = np.array([
  [1, 1, 1], 
  [1, 1, 1], 
  [1, 1, 2]
])

# 行列を作成
matrix_b = np.array([
  [1, 3, 1], 
  [1, 3, 1], 
  [1, 3, 8]
])

# 2つの行列を加算
print(np.add(matrix_a, matrix_b))

# 2つの行列を減算
print(np.subtract(matrix_a, matrix_b))

# +演算子、-演算子を使用して加算、減算することも可能
# 2つの行列の加算
print(matrix_a + matrix_b)
