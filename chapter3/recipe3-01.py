# 3.1 データフレームの作成

# 問題
# 新しいデータフレームを作りたい。

# データラングリング(data wrangling)とは、
# 生データからゴミを取り去り、使いやすい形に整形すること。
# データラングリングに用いられるデータ構造として広く用いられているのは、
# データフレーム(data Frame)である。

import pandas as pd

# DataFrameを作成
dataframe = pd.DataFrame()

# 列を追加
dataframe['Name'] = ['Jacky Jackson', 'Steven Stevenson']
dataframe['Age'] = [38, 25]
dataframe['Driver'] = [True, False]

# DataFrameを表示
print(dataframe)

# 行を作成
new_person = pd.Series(['Molly Mooney', 40, True], index=['Name', 'Age', 'Driver'])

# 行を追加
dataframe = dataframe.append(new_person, ignore_index=True)

# DataFrameを表示
print(dataframe)
