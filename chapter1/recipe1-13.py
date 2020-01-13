# 1.13 行列式の計算

# 問題
# 行列の行列式を知りたい。

import numpy as np

# 行列を作成
matrix = np.array([
  [1, 2, 3], 
  [2, 4, 6], 
  [3, 8, 9]
])

# 行列の行列式を算出
print(np.linalg.det(matrix))
