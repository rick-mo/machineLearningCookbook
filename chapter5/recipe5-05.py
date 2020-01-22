# 5.5 不均等なクラスの取り扱い

# 問題
# ターゲットベクトルのクラスごとの出現頻度が大きく異なる。

import numpy as  np
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

iris = load_iris()

# 特徴量行列を作成
features = iris.data

# ターゲットベクトルを作成
target = iris.target

# 最初の40の観測値を削除
features = features[40:,:]
target = target[40:]

# クラス0であるかどうかを示す2値ターゲットベクトルを作成
target = np.where((target == 0), 0, 1)

print(target)

# 重みを作成
weights = { 0: 0.9, 1: 0.1 }

# ランダムフォレストクラス分類器を重みを指定して作成
print(RandomForestClassifier(class_weight=weights))

# ランダムフォレストクラス分類器を重みをbalanceに指定して作成
print(RandomForestClassifier(class_weight='balanced'))

# 別の方法：ダウンサンプリング、アップサンプリング

# それぞれのクラスの観測値のインデックスを取得
i_class0 = np.where(target == 0)[0]
i_class1 = np.where(target == 1)[0]

# それぞれのクラスの観測値数を計算
n_class0 = len(i_class0)
n_class1 = len(i_class1)

# クラス0のそれぞれの観測値に対して、
# ランダムにクラス1から非復元抽出
i_class1_downsampled = np.random.choice(i_class1, size=n_class0, replace=False)

# クラス0のターゲットベクトルと、
# ダウンサンプリングしたクラス1のターゲットベクトルを結合
print(np.hstack((target[i_class0], target[i_class1_downsampled])))

# クラス0の特徴量行列と
# ダウンサンプリングしたクラス1の特徴量行列を結合
print(np.vstack((features[i_class0,:], features[i_class1_downsampled,:]))[0:5])
