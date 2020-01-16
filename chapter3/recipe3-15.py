# 3.15 列に対するループ

# 問題
# ある列の全ての要素に対して、何らかの操作を繰り返して実行したい。

import pandas as pd

# URLを作成
url = 'https://tinyurl.com/titanic-csv'

# データをロード
dataframe = pd.read_csv(url)

# 最初の2つの名前を大文字にして表示
for name in dataframe['Name'][0:2]:
  print(name.upper())

# 内包表記
print([name.upper() for name in dataframe['Name'][0:2]])

# ここではforループを使用しているが、
# pandasのapplyメソッドを用いる方法がある。
