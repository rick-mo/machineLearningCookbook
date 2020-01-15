# 3.6 列の名前を変更

# 問題
# pandasのDataFrameの列の名前を変更したい。

import pandas as pd

# URLを作成
url = 'https://tinyurl.com/titanic-csv'

# データをロード
dataframe = pd.read_csv(url)

# 列名を変更して、最初の2列を表示
print(dataframe.rename(columns={'PClass': 'Passenger Class'}).head(2))

# 複数の列名を変更して、最初の2列を表示
print(dataframe.rename(columns={'PClass': 'Passenger Class', 'Sex': 'Gender'}).head(2))
