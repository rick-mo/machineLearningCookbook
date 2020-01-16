# 3.19 DataFrameのマージ

# 問題
# 2つのDataFrameを統合したい。

import pandas as pd

# DataFrameを作成
employee_data = {
  'employee_id': ['1', '2', '3', '4'],
  'name': ['Alex', 'Any', 'Allen', 'Mori'],
}
dataframe_employees = pd.DataFrame(employee_data, columns=['employee_id', 'name'])

# DataFrameを作成
sales_data = {
  'employee_id': ['3', '4', '5', '6'],
  'total_sales': [23456, 2512, 2345, 1455]
}
dataframe_sales = pd.DataFrame(sales_data, columns=['employee_id', 'total_sales'])

# DataFrameをマージ
print(pd.merge(dataframe_employees, dataframe_sales, on='employee_id'))

# mergeはデフォルトではインナージョインを行う。
# howパラメータで結合方法を切り替える。

# DataFrameをマージ:アウタージョイン
print(pd.merge(dataframe_employees, dataframe_sales, on='employee_id', how='outer'))

# DataFrameをマージ:レフトジョイン
print(pd.merge(dataframe_employees, dataframe_sales, on='employee_id', how='left'))

# DataFrameをマージ:マージ対象を指定
print(pd.merge(
  dataframe_employees, 
  dataframe_sales, 
  left_on='employee_id', 
  right_on='employee_id'
))
