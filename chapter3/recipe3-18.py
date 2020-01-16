# 3.18 DataFrameの連結

# 問題
# 2つのDataFrameを連結したい。

import pandas as pd

# DataFrameを作成
data_a = {
  'id': ['1', '2', '3'],
  'first': ['Alex', 'Any', 'Allen'],
  'last': ['Anderson', 'Ackerman', 'All']
}
dataframe_a = pd.DataFrame(data_a, columns=['id', 'first', 'last'])

# DataFrameを作成
data_b = {
  'id': ['4', '5', '6'],
  'first': ['Billy', 'Brian', 'Bran'],
  'last': ['Bonder', 'Black', 'Balwner']
}
dataframe_b = pd.DataFrame(data_b, columns=['id', 'first', 'last'])

# 行方向にDataFrameを連結
print(pd.concat([dataframe_a, dataframe_b], axis=0))

# 列方向にDataFrameを連結
print(pd.concat([dataframe_a, dataframe_b], axis=1))

# appendメソッドを用いて、新しい行をDataFrameに追加
row = pd.Series([10, 'Chris', 'Chillon'], index=['id', 'first', 'last'])
print(dataframe_a.append(row, ignore_index=True))
