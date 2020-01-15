# 3.7 最小値、最大値、合計、平均値、カウント数の算出

# 問題
# DataFrame内の特定の数値列の最小値、最大値、合計、平均値、カウント数を算出したい。

import pandas as pd

# URLを作成
url = 'https://tinyurl.com/titanic-csv'

# データをロード
dataframe = pd.read_csv(url)

# 統計量を計算
print('Maximum:', dataframe['Age'].max())
print('Minimum:', dataframe['Age'].min())
print('Mean:', dataframe['Age'].mean()) # 平均
print('Sum:', dataframe['Age'].sum())
print('Count:', dataframe['Age'].count())

# 各項目のカウント数
print(dataframe.count())
