# 1.5 行列の性質を取得する

# 問題
# 行列の形状、サイズ、次元数を調べたい。

import numpy as np

# 行列を作成
matrix = np.array([
  [1, 2, 3, 4], 
  [5, 6, 7, 8], 
  [9, 10, 11, 12]
])

# 行数、列数を表示
print(matrix.shape)

# 要素数(行数×行数)を表示
print(matrix.size)

# 次元数を表示
print(matrix.ndim)
