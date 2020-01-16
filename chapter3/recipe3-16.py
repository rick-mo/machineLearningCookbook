# 3.16 ある列の全ての要素に対して関数を適用する

# 問題
# ある列の全ての要素に対して何らかの関数を実行したい。

import pandas as pd

# URLを作成
url = 'https://tinyurl.com/titanic-csv'

# データをロード
dataframe = pd.read_csv(url)

# 関数を定義
def uppercase(x):
  return x.upper()

print(dataframe['Name'].head(2))

# 関数を適用して、結果の最初の2行を表示
print(dataframe['Name'].apply(uppercase)[0:2])
