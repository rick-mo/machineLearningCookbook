# 2.1 サンプルデータセットのロード

# 問題
# 既存のサンプルデータセットをロードしたい。

from sklearn import datasets

# digitデータセットをロード
digits = datasets.load_digits()

# 特徴量行列を作成
features = digits.data

# 最初の観測値を表示
print(features[0])

# ターゲットベクトルを作成
target = digits.target

print(target)
