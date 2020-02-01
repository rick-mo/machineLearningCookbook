# 7.2 タイムゾーンの取り扱い

# 問題
# 時系列データに対して、タイムゾーン情報を追加もしくは変更したい。

import pandas as pd

# 日時データを作成
print(pd.Timestamp('2017-05-01 06:00:00', tz='Europe/London'))

date = pd.Timestamp('2017-05-01 06:00:00')

# タイムゾーンを設定
date_in_london = date.tz_localize('Europe/London')

print(date_in_london)

# タイムゾーンを変更
print(date_in_london.tz_convert('Africa/Abidjan'))

# 日時データを3つ作成
dates = pd.Series(pd.date_range('2/2/2002', periods=3, freq='M'))

# タイムゾーンを設定
print(dates.dt.tz_localize('Africa/Abidjan'))

# タイムゾーンの文字列表現は、pytzライブラリを用いることを推奨する
from pytz import all_timezones

print(all_timezones[:2])
