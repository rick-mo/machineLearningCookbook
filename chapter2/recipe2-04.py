# 2.4 EXCELファイルの読み込み

# 問題
# EXCELスプレッドシートを読み込みたい。

import pandas as pd

# URLを作成
url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/data.xlsx'

# データセットをロード
dataframe = pd.read_excel(url, sheetname=0, header=1)
# sheetname:シート名やシートの位置を示す番号を指定するパラメータ(複数指定可能)
# header:headerとする行数を指定するパラメータ

# 最初の2行を表示
print(dataframe.head(2))
