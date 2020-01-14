# 2.3 CSVファイルのロード

# 問題
# CSV(comma-separated values)ファイルを読み込みたい。

import pandas as pd

# URLを作成
url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/data.csv'

# データセットをロード
dataframe = pd.read_csv(url)
# read_csvには、30以上のパラメータがある。
# sep:区切り文字を指定できるパラメータ
# header:csvファイルにheaderがあるかどうかを指定できるパラメータ

# 最初の2行を表示
print(dataframe.head(2))
