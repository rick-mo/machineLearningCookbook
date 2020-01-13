# 1.11 行列のフラット化

# 問題
# 行列を1次元の配列に変換したい。

import numpy as np

# 行列を作成
matrix = np.array([
  [1, 2, 3], 
  [4, 5, 6], 
  [7, 8, 9]
])

# 行列をフラット化(1次配列に変換)
print(matrix.flatten())

# reshapeを使って行ベクトルを作ることもできる。
print(matrix.reshape(1, -1))
