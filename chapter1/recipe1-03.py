# 1.3 疎行列の作成

# 問題
# 非ゼロ要素が少ししかないデータを、効率的に表現したい。

import numpy as np
from scipy import sparse

# 行列を作成
matrix = np.array([[0, 0], [0, 1], [3, 0]])

# CSR(copressed sparse row)形式の行列を作成
matrix_sparse = sparse.csr_matrix(matrix)

print(matrix)
print(matrix_sparse)
