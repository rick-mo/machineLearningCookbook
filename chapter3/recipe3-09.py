# 3.9 欠損データの取り扱い

# 問題
# DataFrame中の欠損データを特定したい。

import pandas as pd

# URLを作成
url = 'https://tinyurl.com/titanic-csv'

# データをロード
dataframe = pd.read_csv(url)

# 欠損値を選択し、2つを表示
print(dataframe[dataframe['Age'].isnull()].head(2))

# 値をNaNで置き換えることを試みる 以下エラーとなる。
# dataframe['Sex'] = dataframe['Sex'].replace('male', NaN)

# pandasはNumPyのNaNを用いて欠損値を表すが、
# NaNはpandasにおいて完全にネイティブに実装されているわけではない。

import numpy as np

# 値をNaNで置き換える
print(dataframe['Sex'].replace('male', np.nan))

# 欠損値の表現を指定してデータをロード
dataframe = pd.read_csv(url, na_values=[np.nan, 'NONE', -999])
