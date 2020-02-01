# 7.6 曜日の算出

# 問題
# 日付のベクトルに対して、それぞれの日の曜日を知りたい。

import pandas as pd

# 日時データを作成
dates = pd.Series(pd.date_range('2/2/2002', periods=3, freq='M'))

# 曜日を表示
print(dates.dt.weekday_name)

# 曜日を表示(数値)
print(dates.dt.weekday)
