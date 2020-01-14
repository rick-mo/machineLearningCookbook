# 2.2 シミュレーションによるデータセットの生成

# 問題
# シミュレーションを用いてデータセットを生成したい。

# 線形回帰に用いる適したデータセットが欲しい場合

from sklearn.datasets import make_regression

# 特徴量行列、ターゲットベクトル、生成に用いた係数の真の値を作成
features, target, coefficients = make_regression(
  n_samples=100,
  n_features=3,
  n_informative=3,
  n_targets=1,
  noise=0.0,
  coef=True,
  random_state=1
)

# 特徴量行列とターゲットベクトルを表示
print('線形回帰')
print('特徴量行列\n', features[:3])
print('ターゲットベクトル\n', target[:3])

# クラス分類のためのデータセットが欲しい場合

from sklearn.datasets import make_classification

# 特徴量行列、ターゲットベクトルを作成
features, target = make_classification(
  n_samples=100,
  n_features=3,
  n_informative=3,
  n_redundant=0,
  n_classes=2,
  weights=[.25, .75],
  random_state=1
)

# 特徴量行列とターゲットベクトルを表示
print('クラス分類')
print('特徴量行列\n', features[:3])
print('ターゲットベクトル\n', target[:3])

# クラスタリングに適するように設計されたデータセットが欲しい場合

from sklearn.datasets import make_blobs

# 特徴量行列、ターゲットベクトルを作成
features, target = make_blobs(
  n_samples=100,
  n_features=2,
  centers=3,
  cluster_std=0.5,
  shuffle=True,
  random_state=1
)

# 特徴量行列とターゲットベクトルを表示
print('クラスタリング')
print('特徴量行列\n', features[:3])
print('ターゲットベクトル\n', target[:3])

import matplotlib.pyplot as plt

# 散布図を表示
plt.scatter(features[:,0], features[:,1], c=target)
plt.show()
