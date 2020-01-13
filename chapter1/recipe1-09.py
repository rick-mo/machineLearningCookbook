# 1.9 配列形状の変更

# 問題
# 要素の値を変更せずに、配列の形状（行数と列数）を変更したい。

import numpy as np

# 行列を作成
matrix = np.array([
  [1, 2, 3], 
  [4, 5, 6], 
  [7, 8, 9],
  [10, 11, 12]
])

# 2x6の行列に形状変換
print(matrix.reshape(2, 6))

# 形状変換する際のルール：配列の要素数が同じとなること。
print(matrix.size)
