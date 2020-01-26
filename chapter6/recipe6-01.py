# 6.1 テキストのクリーニング

# 問題
# 何らかの非構造テキストデータに対して、基本的なクリーニングを行いたい。

# テキストを生成
text_data = [
  '   Interrobang. By Aishwarya Henriette   ',
  'Parking And Going. By Karl Gautier',
  '   Today Is The night. By Jarek Prakash  '
]

# ホワイトスペースを削除
strip_whitespace = [string.strip() for string in text_data]

print(strip_whitespace)

# ピリオドを削除
remove_period = [string.replace('.', '') for string in strip_whitespace]

print(remove_period)

# 関数を定義
def capitalizer(string: str) -> str:
  return string.upper()

# 関数を適用
print([capitalizer(string) for string in remove_period])

# 正規表現を用いて文字列操作を行う。

import re

# 関数を定義
def replace_letters_with_X(string: str) -> str:
  return re.sub(r'[a-zA-Z]', 'X', string)

# 関数を適用
print([replace_letters_with_X(string) for string in remove_period])
