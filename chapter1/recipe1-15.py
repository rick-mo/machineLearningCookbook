# 1.15 行列トレースの計算

# 問題
# 行列のトレース（跡）を計算したい。

import numpy as np

# 行列を作成
matrix = np.array([
  [1, 2, 3], 
  [2, 4, 6], 
  [3, 8, 9]
])

# トレースを返す
print(matrix.trace())

# 行列のトレースとは、対角要素の和である。

# 対角要素を足し合わせたものを返す
print(sum(matrix.diagonal()))
