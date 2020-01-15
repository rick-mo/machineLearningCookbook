# 3.10 列の削除

# 問題
# DataFrameから列を削除したい。

import pandas as pd

# URLを作成
url = 'https://tinyurl.com/titanic-csv'

# データをロード
dataframe = pd.read_csv(url)

# 現在の列の状態
print(dataframe.head(2))

# 列を削除
print(dataframe.drop('Age', axis=1).head(2))

# 複数の列を削除
print(dataframe.drop(['Age', 'Sex'], axis=1).head(2))

# 列を削除（列名がない場合の対処）
print(dataframe.drop(dataframe.columns[1], axis=1).head(2))

# pandasの多くのメソッドがサポートしている
# inplace=Trueというパラメータは指定しないようにする。
# DataFrameを変更可能なオブジェクトとしてしまうため。
