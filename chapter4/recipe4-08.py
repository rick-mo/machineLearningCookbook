# 4.8 特徴量の離散化

# 問題
# 数値特徴量を離散化されたビン(bin:入れ物)に分けたい。

# 方法1:何らかの閾値/スレッショルドで2値化する。

import numpy as np
from sklearn.preprocessing import Binarizer

# 特徴量を作成
age = np.array([[6], [12], [20], [36], [65]])

# 2値化器を作成
binarizer = Binarizer(18)

# 特徴量を変換
print(binarizer.fit_transform(age))

# 方法2:複数の閾値を用いて数値特徴量を分割したい場合に用いる。

# 特徴量を複数のビンに分割
print(np.digitize(age, bins=[20, 30, 64]))
