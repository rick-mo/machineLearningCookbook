# 1.14 行列の対角要素の取得

# 問題
# 行列の対角要素を取得したい。

import numpy as np

# 行列を作成
matrix = np.array([
  [1, 2, 3], 
  [2, 4, 6], 
  [3, 8, 9]
])

# 対角要素を返す
print(matrix.diagonal())

# 主対角要素の1つ上の副対角要素を返す
print(matrix.diagonal(offset=1))

# 主対角要素の1つ下の副対角要素を返す
print(matrix.diagonal(offset=-1))
