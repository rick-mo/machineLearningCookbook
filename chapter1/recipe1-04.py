# 1.4 要素の選択

# 問題
# ベクトルや行列から1つ以上の要素を選択したい。

import numpy as np

# 行ベクトルを作成
vector = np.array([0, 1, 2, 3, 4, 5, 6])

print('3つ目の要素を選択')
print(vector[2])

print('全ての要素を選択')
print(vector[:])

print('3番目までの全ての要素を選択(3番目含む)')
print(vector[:3])

print('3番目より後の全ての要素を選択')
print(vector[3:])

print('最後の要素を選択')
print(vector[-1])

# 行列を作成
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print('2行目、2列目を選択')
print(matrix[1, 1])

print('行列から、最初の2つの行の全ての列を選択')
print(matrix[:2,:])

print('全ての行の2列目を選択')
print(matrix[:,1:2])
