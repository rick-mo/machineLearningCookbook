# 6.3 句読点の除去

# 問題
# テキストデータから句読点(punctuation)を取り除きたい。

import unicodedata
import sys

# テキストを生成
text_data = [
  'Hi!!! I. Love. This. Song....',
  '10000% Agree!!!! #LoveIT',
  'Right!?!?'
]

# 句読点文字を含む辞書を作成
punctuation = dict.fromkeys(
  i for i in range(sys.maxunicode) 
  if unicodedata.category(chr(i)).startswith('P')
)

# それぞれの文字列から、句読点文字を全て除去
print([string.translate(punctuation) for string in text_data])

# 辞書に存在する句読点をNoneに変換することで、除去している。
