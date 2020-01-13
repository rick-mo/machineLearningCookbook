# 1.2 行列の作成

# 問題
# 行列を作りたい。

import numpy as np

# 3行2列の行列を作成
matrix = np.array([[1, 2], [3, 4], [5, 6]])

print(matrix)
print(type(matrix))

# 非推奨のNumpy専用行列データ構造
matrix_object = np.mat([[1, 2], [3, 4], [5, 6]])
print(matrix_object)
print(type(matrix_object))
