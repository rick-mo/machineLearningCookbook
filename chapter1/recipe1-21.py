# 1.21 乱数の生成

# 問題
# 擬似乱数を生成したい。

import numpy as np

# シード値を作成
np.random.seed(0)

# 0.0と1.0の間のランダムな浮動小数点数値を3つ生成する
print(np.random.random(3))

# 1と10の間のランダムな整数値を3つ生成する
print(np.random.randint(0, 11, 3))

# 平均0.0、標準偏差1.0の正規分布から3つの数値を生成する
print(np.random.normal(0.0, 1.0, 3))

# 平均0.0、スケール1.0のロジスティック分布から3つの数値を生成する
print(np.random.logistic(0.0, 1.0, 3))

# 1.0以上で、2.0より小さい3つの数値を生成する
print(np.random.uniform(1.0, 2.0, 3))
