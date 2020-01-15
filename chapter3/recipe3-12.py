# 3.12 重複した行の削除

# 問題
# DataFrameの中の重複した行を削除したい。

import pandas as pd

# URLを作成
url = 'https://tinyurl.com/titanic-csv'

# データをロード
dataframe = pd.read_csv(url)

# 重複した行を削除し、最初の2行を表示
print(dataframe.drop_duplicates().head(2))

# 行数を表示（重複行が削除されていないことを確認）
print('元のDataFrame中の行数:', len(dataframe))
print('重複削除後の行数:', len(dataframe.drop_duplicates()))

# drop_duplicates()は、全ての列が完全に一致している行だけを削除する。

# 一部の列が重複している行を削除
print(dataframe.drop_duplicates(subset=['Sex']))

# 重複している列のうち最初の行が残る。

# 重複している列のうち最後の行を残し、あとは削除する
print(dataframe.drop_duplicates(subset=['Sex'], keep='last'))

# duplicatedメソッドは、個々の行が重複しているかどうかを示す真偽値列を返す。
