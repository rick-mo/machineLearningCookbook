# 1.6 要素に対する計算

# 問題
# 配列の複数の要素に対して何らかの関数を適用したい。

import numpy as np

# 行列を作成
matrix = np.array([
  [1, 2, 3], 
  [4, 5, 6], 
  [7, 8, 9]
])

# 引数に100を加える関数を作成
add_100 = lambda i: i + 100

# ベクトル化された関数を作成
vectorized_add_100 = np.vectorize(add_100)

# この関数をmatrixの全ての要素に適用
print(vectorized_add_100(matrix))

# ただしvectorizeは、本質的にforループを行うだけなので、
# 性能は全く向上しないことに注意。

# Numpyでは配列次元が異なる複数の配列に対しても演算を行うことができる。
# これをブロードキャスト(broadcast)と呼ぶ。
print(matrix + 100)
