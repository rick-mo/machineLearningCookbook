# 2.5 JSONファイルの読み込み

# 問題
# JSONファイルを読み込んでデータの前処理を行う必要がある。

import pandas as pd

# URLを作成
url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/data.json'

# データセットをロード
dataframe = pd.read_json(url, orient='columns')
# orient:JSONファイルがどのように構成されているかを指定するパラメータ
#        split, records, index, columns, valuesのいづれかを指定可能

# 最初の2行を表示
print(dataframe.head(2))
