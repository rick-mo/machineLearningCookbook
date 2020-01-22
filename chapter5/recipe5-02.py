# 5.2 順序カテゴリ特徴量の数値化

# 問題
# 順序カテゴリ変数(例：高、中、低)がある。

import pandas as pd

# 特徴量を生成
dataframe = pd.DataFrame({'Score': ['Low', 'Low', 'Medium', 'Medium', 'High']})

# マップを作成
scale_mapper = {'Low': 1, 'Medium': 2, 'High': 3}

# 特徴量の値をマップを使って置換
print(dataframe['Score'].replace(scale_mapper))

# 特徴量を生成
dataframe = pd.DataFrame({'Score': ['Low', 'Low', 'Medium', 'Medium', 'High', 'Barely More Than Medium']})

# マップを作成
scale_mapper = {'Low': 1, 'Medium': 2, 'Barely More Than Medium': 3, 'High': 4}

# 特徴量の値をマップを使って置換
print(dataframe['Score'].replace(scale_mapper))

# これだとLowとMediumの間の距離が、MediumとBarely More Than Mediumの間の距離が同じとなっている。

scale_mapper = {'Low': 1, 'Medium': 2, 'Barely More Than Medium': 2.1, 'High': 3}

print(dataframe['Score'].replace(scale_mapper))
