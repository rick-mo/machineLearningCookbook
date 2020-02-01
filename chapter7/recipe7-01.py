# 7.1 文字列の日時データへの変換

# 問題
# 日時を表す文字列のベクトルを時系列データに変換したい。

import numpy as np
import pandas as pd

# 文字列を作成
date_strings = np.array([
  '03-04-2005 11:35 PM',
  '23-05-2010 12:01 AM',
  '04-09-2009 09:09 PM',
])

# 日時データに変換
print([pd.to_datetime(date, format='%d-%m-%Y %I:%M %p') for date in date_strings])

error_date_strings = np.array([
  '03-04-2005 11:35 PM',
  '23-05-2010 12:01 AM',
  '04-09-2009 77:09 PM',
])

# エラー時の処理方法の指定(coerce:エラー時にNaT(欠損値)を値にする)
print([pd.to_datetime(date, format='%d-%m-%Y %I:%M %p', errors='coerce') for date in error_date_strings])
