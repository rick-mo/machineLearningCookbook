# 1.8 平均値、分散、標準偏差の計算

# 問題
# 配列の記述統計量を計算したい。

import numpy as np

# 行列を作成
matrix = np.array([
  [1, 2, 3], 
  [4, 5, 6], 
  [7, 8, 9]
])

# 平均値を算出
print(np.mean(matrix))

# 分散を算出
print(np.var(matrix))

# 標準偏差を算出
print(np.std(matrix))

# 各列の平均値を算出
print(np.mean(matrix, axis=0))
