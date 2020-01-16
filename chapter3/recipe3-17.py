# 3.17 関数をグループに適用

# 問題
# groupbyメソッドでグループ分けした
# それぞれの行グループに対して、ある関数を適用したい。

import pandas as pd

# URLを作成
url = 'https://tinyurl.com/titanic-csv'

# データをロード
dataframe = pd.read_csv(url)

# 行グループ分けし、関数をグループごとに適用
print(dataframe.groupby('Sex').apply(lambda x: x.count()))
