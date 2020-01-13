# 1.20 逆行列の算出

# 問題
# 正方行列の逆行列を求めたい。

import numpy as np

# 行列を作成
matrix = np.array([[1, 4], [2, 5]])

# 逆行列を算出
print(np.linalg.inv(matrix))

# 行列とその逆行列を乗算して、正しく計算されているか確認
print(matrix @ np.linalg.inv(matrix))
