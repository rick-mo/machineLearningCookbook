# 1.7 最大値と最小値を見つける

# 問題
# 配列中の最大値もしくは最小値を見つけたい。

import numpy as np

# 行列を作成
matrix = np.array([
  [1, 2, 3], 
  [4, 5, 6], 
  [7, 8, 9]
])

# 最大の要素を返す
print(np.max(matrix))

# 各列における最大の要素を返す
print(np.max(matrix, axis=0))

# 各行における最大の要素を返す
print(np.max(matrix, axis=1))

# 最小の要素を返す
print(np.min(matrix))
